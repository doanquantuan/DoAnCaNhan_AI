# 🎓 Đồ Án Cá Nhân - Trí Tuệ Nhân Tạo
# Đoàn Quân Tuấn - 23110354
## 1. Mục tiêu 🎯
###  Bài toán 8-Puzzle là một bài toán cổ điển trong trí tuệ nhân tạo, gồm một bảng có kích thước 3x3 với 8 ô được đánh số từ 1 đến 8 và một ô trống. Các ô có thể được di chuyển bằng cách trượt một trong các ô liền kề vào vị trí ô trống.
###  Mục tiêu của bài toán là từ trạng thái đầu, bảng được sắp xếp lại vị trí các ô sao cho khớp với trạng thái đích mong muốn bằng cách di chuyển ô trống. 
###  Trong bài toán này, chúng ta sử dụng các thuật toán AI để giải bài toán 8 puzzle và so sánh mức độ hiệu quả cũng như hiệu suất của từng thuật toán thông qua các tiêu chí như độ dài lời giải, thời gian thực thi và số trạng thái đã duyệt.
## 2. Nội dung 📚
### 2.1. Các thuật toán Tìm kiếm không có thông tin
#### Tìm kiếm không có thông tin (Uninformed Search) là một nhóm các thuật toán tìm kiếm có chủ đích không dựa vào thông tin bổ sung ước lượng chi phí đến đích mà thay vào đó thuật toán này khám phá không gian tìm kiếm và duyệt qua các trạng thái một cách mù quáng, không đảm bảo tìm được đường đi tối ưu nhất. Các thuật toán thuộc nhóm này bao gồm: 
##### - BFS (Breadth-First Search) – Tìm kiếm theo chiều rộng: mở rộng các nút theo từng lớp (tầng), đảm bảo tìm được lời giải ngắn nhất nếu chi phí đều.
##### - DFS (Depth-First Search) – Tìm kiếm theo chiều sâu: mở rộng sâu theo từng nhánh, ít tốn bộ nhớ nhưng không đảm bảo tìm được lời giải tối ưu.
##### - IDS (Iterative Deepening Search) – Tìm kiếm theo chiều sâu lặp lại: kết hợp DFS và BFS, mở rộng theo từng mức độ sâu giới hạn, vừa tiết kiệm bộ nhớ như DFS, vừa đảm bảo tối ưu như BFS.
##### - UCS (Uniform Cost Search) – Tìm kiếm theo chi phí đồng đều: mở rộng nút có tổng chi phí đường đi thấp nhất, đảm bảo tìm được lời giải có chi phí thấp nhất.
## 3. Kết luận 📝
