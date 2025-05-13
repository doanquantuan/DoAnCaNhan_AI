from collections import deque
import random
import pygame
import sys
import numpy as np
import time

# Logic 8-puzzle
ACTIONS = {
    'UP': -3,
    'DOWN': 3,
    'LEFT': -1,
    'RIGHT': 1
}

def is_valid_move(state, action):
    blank = state.index(0)
    if action == 'UP' and blank < 3: return False
    if action == 'DOWN' and blank > 5: return False
    if action == 'LEFT' and blank % 3 == 0: return False
    if action == 'RIGHT' and blank % 3 == 2: return False
    return True

def apply_action_to_state(state, action):
    if not is_valid_move(state, action):
        return state
    blank = state.index(0)
    delta = ACTIONS[action]
    new_blank = blank + delta
    lst = list(state)
    lst[blank], lst[new_blank] = lst[new_blank], lst[blank]
    return tuple(lst)

def apply_action(belief, action):
    new_belief = set()
    for state in belief:
        new_state = apply_action_to_state(state, action)
        new_belief.add(new_state)
    return frozenset(new_belief)

def get_observation(belief):
    state = random.choice(list(belief))
    return state.index(0)

def filter_belief_by_observation(belief, observation):

    return frozenset(state for state in belief if state.index(0) == observation)

def search_with_partial_observation(initial_belief, partial_goal):
    def is_goal(belief):
        
        for state in belief:
            satisfies_goal = True
            for pos, value in partial_goal.items():
                if state[pos] != value:
                    satisfies_goal = False
                    break
            if satisfies_goal:
                return True
        return False

    queue = deque()
    visited = set()
    queue.append((frozenset(initial_belief), []))
    node_count = 0

    while queue:
        belief, path = queue.popleft()
        node_count += 1
        if belief in visited:
            continue
        visited.add(belief)

        if is_goal(belief):
            return path, node_count

        for action in ACTIONS:
            new_belief = apply_action(belief, action)
            observation = get_observation(new_belief)
            filtered_belief = filter_belief_by_observation(new_belief, observation)
            if filtered_belief and filtered_belief not in visited:
                queue.append((filtered_belief, path + [action]))

    return None, node_count

def random_belief_set(n, k):
    belief_set = set()
    while len(belief_set) < n:
        elements = random.sample(range(9), 9)
        belief_set.add(tuple(elements))
    return belief_set

def draw_state(screen, state, pos_x, pos_y, cell_size, color_cell, color_number, size, title="", is_partial_goal=False, partial_goal=None):
    font = pygame.font.SysFont("Arial", size, bold=True)
    state_matrix = np.array(state).reshape(3, 3)
    for i in range(3):
        for j in range(3):
            idx = i * 3 + j
            x = j * cell_size + pos_x
            y = i * cell_size + pos_y
            rect = pygame.Rect(x, y, cell_size, cell_size)

            pygame.draw.rect(screen, color_cell, rect)
            pygame.draw.rect(screen, "white", rect, 3)

            if is_partial_goal:
                # Chỉ vẽ các ô được xác định trong partial_goal
                if idx in partial_goal:
                    value = partial_goal[idx]
                    if value != 0:
                        text = font.render(str(value), True, color_number)
                        text_rect = text.get_rect(center=rect.center)
                        screen.blit(text, text_rect)
            else:
                value = state_matrix[i, j]
                if value != 0:
                    text = font.render(str(value), True, color_number)
                    text_rect = text.get_rect(center=rect.center)
                    screen.blit(text, text_rect)

    text = font.render(title, True, "black")
    title_rect = text.get_rect(center=(pos_x + cell_size * 1.5, pos_y + cell_size * 3 + 15))
    screen.blit(text, title_rect)

# Hàm vẽ nút Bắt đầu
def draw_start_button(screen, x, y, width, height, font, active):
    color = (0, 255, 0) if active else (150, 150, 150)
    pygame.draw.rect(screen, color, (x, y, width, height))
    pygame.draw.rect(screen, (0, 0, 0), (x, y, width, height), 2)
    text = font.render("START", True, (0, 0, 0))
    text_rect = text.get_rect(center=(x + width // 2, y + height // 2))
    screen.blit(text, text_rect)

def main(partial_goal_tuple):
    # Khởi tạo Pygame
    pygame.init()
    tile_size = 80
    grid_width = tile_size * 3
    margin = 50
    width = 5 * grid_width + 6 * margin
    height = 2 * (grid_width + margin) + 110
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Partial Observation with Partial Goal")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont('arial', 30)

    initial_belief = random_belief_set(5, 9)
    current_belief = frozenset(initial_belief)
    initial_belief_states = list(initial_belief)
     

    partial_goal = {i: val for i, val in enumerate(partial_goal_tuple) if val != 0}
    plan = None
    plan_index = 0
    started = False
    exe_time = 0
    node_count = 0
    plan = []

    button_x = margin
    button_y = height - 50
    button_width = 100
    button_height = 40

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and not started:
                mouse_pos = event.pos
                if button_x <= mouse_pos[0] <= button_x + button_width and \
                   button_y <= mouse_pos[1] <= button_y + button_height:
                    started = True
                    
                    start_time = time.time()
                    plan, node_count = search_with_partial_observation(initial_belief, partial_goal)
                    end_time = time.time()
                    exe_time = end_time - start_time
                 
                    if plan is None:
                        text = font.render("No Solution", True, (0, 0, 0))
                        screen.blit(text, (1000, 20))
                        pygame.quit()
                        sys.exit()
            elif event.type == pygame.KEYDOWN and started:
                if event.key == pygame.K_SPACE and plan_index < len(plan):
                    action = plan[plan_index]
                    current_belief = apply_action(current_belief, action)
                    observation = get_observation(current_belief)
                    current_belief = filter_belief_by_observation(current_belief, observation)
                    plan_index += 1
                elif event.key == pygame.K_r:
                    current_belief = frozenset(initial_belief_states)
                    plan_index = 0

        screen.fill((255, 255, 255))

        goal_x = (width - grid_width) // 2
        goal_y = margin
        
        dummy_state = [0] * 9
        draw_state(screen, dummy_state, goal_x, goal_y, tile_size, (200, 200, 200), (0, 0, 255), 30, 
                  "Partial Goal", is_partial_goal=True, partial_goal=partial_goal)


        current_states = list(current_belief)[:5]
        for i in range(5):
            belief_x = margin + i * (grid_width + margin)
            belief_y = 2 * margin + grid_width
            if i < len(current_states):
        
                satisfies_goal = True
                for pos, value in partial_goal.items():
                    if current_states[i][pos] != value:
                        satisfies_goal = False
                        break
                color_cell = (0, 255, 0) if satisfies_goal else (200, 200, 200)
                draw_state(screen, current_states[i], belief_x, belief_y, tile_size, color_cell, (0, 0, 255), 30, f"Belief {i+1}")
            else:
                draw_state(screen, (0, 0, 0, 0, 0, 0, 0, 0, 0), belief_x, belief_y, tile_size, (200, 200, 200), (0, 0, 255), 30, f"Belief {i+1}")

        
        draw_start_button(screen, button_x, button_y, button_width, button_height, font, not started)

        time_text = font.render(f"Time: {exe_time:.4f} giây", True, (0, 0, 0))
        cost_text = font.render(f"Nodes: {node_count}", True, (0, 0, 0))
        plan_text = font.render(f"Steps: {len(plan)}", True, (0, 0, 0))
        screen.blit(time_text, (20, 20))
        screen.blit(cost_text, (20, 50))
        screen.blit(plan_text, (20, 80))
        if started:
            instruction_text = font.render("SPACE: Next, R: Reset", True, (255, 0, 0))
            screen.blit(instruction_text, (margin + button_width + 20, height - 50))
        else:
            instruction_text = font.render("Click START to Solve", True, (255, 0, 0))
            screen.blit(instruction_text, (margin + button_width + 20, height - 50))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

def run_partial_observation(partial_goal_tuple):
    main(partial_goal_tuple)