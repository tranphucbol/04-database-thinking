# MySQL

## Storage Engine

### InnoDB

*Ưu điểm:*

- Là một Storage Engine transaction-safe (tuân thủ ACID) có các commit, rollback, và khả năng khôi phục dữ liệu người dùng.
- Row-level locking của InnoDB và kiểu nonblocking read của Oracle-style làm tăng sự đồng thời và hiệu suất của người dùng.
- InnoDB lưu trữ dữ liệu người dùng trong các clustered indexes để giảm I/O cho các truy vấn thông thường dựa trên các primary key.
- Hỗ trợ ràng buộc toàn vẹn Foreign Key.

*Nhược điểm:*

- Tính ràng buộc cao
- Truy vấn sẽ phức tạp nếu như ràng buộc quá cao, liên kết nhiều bảng dẫn đến hiệu năng kém
- Khó cài đặt, khó sử dụng cho người mới bắt đầu.

### MyISAM

*Ưu điểm:*

- Đơn giản dễ sử dụng
- Gọn nhẹ, phù hợp cho các công việc read-only, hoặc read-mostly trong các cấu hình Web và lưu trữ dữ liệu

*Nhược điểm:*

- Table-level locking giới hạn hiệu suất read/write dữ liệu

### Memory

*Ưu điểm:*

- Lưu trữ dữ liệu trên RAM, nên có thể truy cập dữ liệu nhanh chóng

*Nhược điểm:*

- Do lưu trong RAM nên dữ liệu sẽ bị mất, khi MySQL Server tắt hoặc khởi động lại.
- Không thể chứa các cột **BLOB** hay **TEXT**

### CSV

*Ưu điểm:*

- Cấu trúc đơn giản, các trường được ngăn cách nhau bởi dấu phẩy.
- Có thể trao đổi dữ liệu, nhập xuất dữ liệu.
- Có thể đọc và viết bằng Microsoft Excel hoặc StarOffice Calc.

*Nhược điểm:*

- Không hỗ trợ ràng buộc

### Federated

*Ưu điểm:*

- Khả năng scalable lớn, do có thể truy cập nhiều MySQL Server từ nhiều remote server khác nhau.

*Nhược điểm:*

- Không hỗ trợ transaction
- Không hoạt động với query cache
- Việc join có thể rất phức tạp

## Data Types

### Numeric Types

- **BIT[(M)]**
  - Một kiểu bit-value. **M** chỉ ra số bits của mỗi giá trị, từ 1 đến 64. Mặc định là 1 nếu **M** bị bỏ qua
- **TINYINT[(M)] [UNSIGNED] [ZEROFILL]**
  - Một số nguyên rất nhỏ. Số có dấu -128 đến 127. Số không dấu 0 đến 255
- **BOOL, BOOLEAN**
  - Kiểu dữ liệu này tương đương với **TINYINT(1)**. Giá trị 0 được xem là **'false'**. Giá trị khác 0 được xem **'true'**. Tuy nhiên, giá trị **TRUE** và **FALSE** tương ứng 1 với 0.
- **SMALLINT[(M)] [UNSIGNED] [ZEROFILL]**
  - Số nguyên nhỏ. kích thước 2 byte.
- **MEDIUMINT[(M)] [UNSIGNED] [ZEROFILL]**
  - Số nguyên với kích thước 3 byte.
- **INT[(M)] [UNSIGNED] [ZEROFILL]**
  - Kích thước thông thường 4 byte
- **INTEGER[(M)] [UNSIGNED] [ZEROFILL]**
  - Tương đương **INT**
- **BIGINT[(M)] [UNSIGNED] [ZEROFILL]**
  - Số nguyên lớn, kích thước 8 byte
  - **SERIAL** là thay thế cho **BIGINT UNSIGNED NOT NULL AUTO_INCREMENT UNIQUE**
- **DECIMAL[(M[,D])] [UNSIGNED] [ZEROFILL]**
  - **M** là tổng chữ số (độ chính xác) và D là số chữ đố sau dấu thập phân. Dấu thập phân và dấu âm (-) không được tính bằng **M**. Nếu **D** bằng 0, các giá trị không có dấu phận phân hoặc phần thập phân. Số chữ số tối đa **M** cho **DECIMAL** là 65. Số thập phân **D** được hỗ trợ tối đa là 30. Nếu **D** bị bỏ qua, mặc định là 0. Nếu **M** bị bỏ qua, mặc đinh là 10.
