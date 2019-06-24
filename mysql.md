# MySQL

## Data Types

### Numeric Types

- **BIT[(M)]**:
  - Một kiểu bit-value. **M** chỉ ra số bits của mỗi giá trị, từ 1 đến 64. Mặc định là 1 nếu **M** bị bỏ qua
- **TINYINT[(M)] [UNSIGNED] [ZEROFILL]**:
  - Một số nguyên rất nhỏ. Số có dấu -128 đến 127. Số không dấu 0 đến 255
- **BOOL, BOOLEAN**
  - Kiểu dữ liệu này tương đương với **INYINT(1)**. Giá trị 0 được xem là **false**. Giá trị khác 0 được xem **true**. Tuy nhiên, giá trị **TRUE** và **FALSE** tương ứng 1 với 0.

