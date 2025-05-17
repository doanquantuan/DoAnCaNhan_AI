# 🎓 Đồ Án Cá Nhân - Trí Tuệ Nhân Tạo  
### 👨‍💻 Đoàn Quân Tuấn - MSSV: 23110354  

---

## 🎯 1. Mục Tiêu

Bài toán **8-Puzzle** là một bài toán cổ điển trong Trí tuệ nhân tạo. Nó gồm một bảng 3x3 với 8 ô được đánh số từ `1 → 8` và **1 ô trống**.  
Mỗi bước đi thực hiện bằng cách **trượt một ô liền kề vào ô trống**.

🎯 **Mục tiêu:**  
Từ một **trạng thái ban đầu**, di chuyển các ô để đạt đến **trạng thái đích** đúng thứ tự.  

Trong đồ án này, ta sử dụng các **thuật toán tìm kiếm AI** để giải bài toán và so sánh hiệu suất giữa các thuật toán dựa trên:
- Độ dài lời giải
- Thời gian thực thi
- Số trạng thái đã duyệt

---

## 📚 2. Nội Dung

### 2.1. 🔍 Các Thuật Toán Tìm Kiếm Không Có Thông Tin (Uninformed Search)

Uninformed Search là nhóm thuật toán **không sử dụng thông tin ước lượng** từ trạng thái hiện tại đến đích. Chúng **duyệt không gian trạng thái một cách mù quáng** và không đảm bảo hiệu quả cao.

#### 🧠 Các thuật toán được áp dụng:
- 🔹 **BFS (Breadth-First Search)**:  
  Mở rộng các node theo tầng → tìm được lời giải ngắn nhất (nếu chi phí bằng nhau).  
- 🔹 **DFS (Depth-First Search)**:  
  Mở rộng theo nhánh sâu nhất trước → tiết kiệm bộ nhớ, nhưng dễ lặp vô hạn, không tối ưu.
- 🔹 **IDS (Iterative Deepening Search)**:  
  Lặp DFS với độ sâu tăng dần → kết hợp ưu điểm của BFS và DFS.
- 🔹 **UCS (Uniform Cost Search)**:  
  Mở rộng node có tổng chi phí nhỏ nhất → tối ưu về chi phí nếu bước đi có trọng số.

#### 🧩 Cấu trúc bài toán 8-Puzzle:
- **Không gian trạng thái**: Tất cả các cấu hình có thể của bảng 3x3.
- **Trạng thái đầu**: Cấu hình ban đầu của ô số.
- **Trạng thái đích**: Cấu hình đúng thứ tự mong muốn.
- **Hành động**: Di chuyển ô trống (↑ ↓ ← →).
- **Chi phí**: Tổng chi phí tích lũy để đi từ trạng thái đầu đến trạng thái đích (nếu có trọng số tùy vào bài toán có đặt hay không).
#### 🛠️ Giải pháp chung:
1. Khởi tạo trạng thái ban đầu và đích  
2. Duyệt không gian trạng thái bằng thuật toán đã chọn  
3. Lưu vết trạng thái đã đi qua để tránh vòng lặp  
4. Khi đạt đến trạng thái đích → trả về lời giải  

---

### 📊 2.2. Đánh Giá Hiệu Suất Thuật Toán

#### ✅ Một vài nhận xét:
| Thuật toán | Tối ưu | Bộ nhớ | Tốc độ | Nhận xét |
|------------|--------|--------|--------|----------|
| **BFS**    | ✅     | ❌     | ✅     | Tìm ra lời giải ngắn nhất, số node duyệt qua ít nhất và thời gian thực thi ngắn nhất => Hiệu suất tốt nhất |
| **DFS**    | ❌     | ❌     | ❌     | Tìm ra lời giải dài nhất, số node duyệt qua nhiều nhất và thời gian thực thi dài nhất và không tối ưu, không đảm bảo tìm ra lời giải (nếu không kiểm soát độ sâu) => Hiệu suất kém nhất. |
| **IDS**    | ✅     | ❌     | ✅     | Lời giải ngắn (do kết hợp BFS và DFS), tốn thời gian do lặp đi lặp lại nhiều lần các node cùng cấp độ. vẫn chậm trong các trường hợp lời giải sâu. |
| **UCS**    | ✅     | ❌     | ✅     | Lời giải tối ưu dựa trên tổng chi, thời gian tốt hơn IDS và tiết kiệm không gian lưu trữ => Hiệu quả khi các bước có chi phí không đồng đều.
 |

---

## 📝 3. Kết Luận

---

> 📁 *Đồ án này được thực hiện phục vụ môn học Trí tuệ nhân tạo. Mọi đóng góp hoặc phản hồi xin gửi qua GitHub.*

