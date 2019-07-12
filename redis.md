# Redis

## Installation

- [Install Redis](https://www.digitalocean.com/community/tutorials/how-to-install-and-secure-redis-on-ubuntu-18-04)
- [Redis cluster](https://gitlab.zalopay.vn/phuctt4/01-system-thinking/tree/master/redis/config-cluster-redis-3-nodes)

## Data Types

### Các kiểu dữ liệu của Redis

- **STRING:** string, integer hoặc float. Redis có thể làm việc với cả string, từng phần của string, cũng như tăng/giảm gía trị của integer, float.
- **LIST:** danh sách liên kết của strings. Redis hỗ trợ các thao tác push, pop từ của 2 phía của list, trim dựa theo offset, đọc 1 hoặc nhiều items của list, tìm kiếm và xóa giá trị.
- **SET:** tập hợp các string (không được sắp xếp). Redis hỗ trợ các thao tác thêm, đọc, xóa từng phần tử, kiểm tra sự xuất hiện của phần tử trong tập hợp. Ngoài ra Redis còn hỗ trợ các phép toán tập hợp, gồm intersect/union/diffrence.
- **HASH:** lưu trữ hash table của các cặp key-value, trong đó key được sắp xếp ngẫu nhiên, không theo thứ tự nào cả. Redis hỗ trợ các thao tác thêm, đọc, xóa từng phàn tử, cũng như đọc tất cả giá trị.
- **ZSET (sorted set):** là 1 danh sách, trong đó mỗi phần tử là map của 1 string(member) và 1 floating-point number (score), danh sách được sắp xếp theo score này. Redis hỗ trợ thao tác thêm, đọc, xóa từng phần tử, lấy ra các phần tử dựa theo range của score hoặc string.

### Các lệnh trong Redis

**Redis Strings:**

```bash
> set mykey somevalue
OK
> get mykey
"somevalue"
```

Lệnh `INCR` có thể chuyển `string` thành `integer`, và tăng nó lên một. Tương tự như `INCR` ta có lệnh `INCRBY`, `DECR` và `DECRBY`

```bash
> set counter 100
OK
> incr counter
(integer) 101
> incr counter
(integer) 102
> incrby counter 50
(integer) 152
```

Khả năng thiết lặp hoặc truy xuất giá trị của nhiều kháo trong một lệnh cũng hữu ích để giảm độ trễ:

```bash
> mset a 10 b 20 c 30
OK
> mget a b c
1) "10"
2) "20"
3) "30"
```

Kiểm tra tồn tại của một khóa và xóa nó:

```bash
> set mykey hello
OK
> exists mykey
(integer) 1
> del mykey
(integer) 1
> exists mykey
(integer) 0
```

Set thời gian hết hạn của một khóa:

```bash
> set key some-value
OK
> expire key 5
(integer) 1
> get key (immediately)
"some-value"
> get key (after some time)
(nil)
```

Kiểm tra thời gian hết hạn của khóa:

```bash
> set key 100 ex 10
OK
> ttl key
(integer) 9
```

**Redis List:**

Có 2 lệnh để push dữ liệu vào `list` trong `redis` là `LPUSH` để push vào đầu của `list` và `RPUSH` để push vào đuôi của `list`:

```bash
> rpush mylist A
(integer) 1
> rpush mylist B
(integer) 2
> lpush mylist first
(integer) 3
> lrange mylist 0 -1
1) "first"
2) "A"
3) "B"
```

Lệnh `LRANGE` để in ra các phần tử trong `list`, index bắt đầu từ 0, có 2 tham số là `start` và `stop`, với `stop` có giá trị là -1 sẽ in toàn bộ `list`, -2 in cho đến phần tử kế cuối.

```bash
> rpush mylist 1 2 3 4 5 "foo bar"
(integer) 9
> lrange mylist 0 -1
1) "first"
2) "A"
3) "B"
4) "1"
5) "2"
6) "3"
7) "4"
8) "5"
9) "foo bar"
```

Tương tự như `LPUSH` và `RPUSH`, `list` cũng có `LPOP` và `RPOP` để lấy phần tử ra ở đầu và cuối.

```bash
> rpush mylist a b c
(integer) 3
> rpop mylist
"c"
> rpop mylist
"b"
> rpop mylist
"a"
```

**Redis Hash:**

Tương tự, hash table thông thường:

`HMSET` và `HMGET` là để `set` và `get` nhiều dữ liệu cùng một lúc. `HSET` và `HGET` để `set` và `get` đơn dữ liệu.

```bash
> hmset user:1000 username antirez birthyear 1977 verified 1
OK
> hget user:1000 username
"antirez"
> hget user:1000 birthyear
"1977"
> hgetall user:1000
1) "username"
2) "antirez"
3) "birthyear"
4) "1977"
5) "verified"
6) "1"
> hmget user:1000 username birthyear no-such-field
1) "antirez"
2) "1977"
3) (nil)
```

Cũng có thể thực hiện tính toán như `Redis String`:

```bash
> hincrby user:1000 birthyear 10
(integer) 1987
> hincrby user:1000 birthyear 10
(integer) 1997
```

**Redis Sets:**

`SADD` để thêm phần tử mới vào `set`.

```bash
> sadd myset 1 2 3
(integer) 3
> smembers myset
1. 3
2. 1
3. 2
```

Kiểm tra một phần tử có trong `set`:

```bash
> sismember myset 3
(integer) 1
> sismember myset 30
(integer) 0
```

**Redis Sorted sets**

Phần tử trong một `sorted sets` được sắp xếp theo thứ tự (vì vậy chúng không được sắp xếp theo thứ tự yêu cầu, thứ tự là một đặc thù của cấu trúc dữ liệu được sử dụng để thể hiện trong `sorted set`). Chúng được sắp xếp theo luật:

- Nếu A và B là hai phần từ có số `score` khác nhau, thì A > B nếu A.score > B.score
- Nếu A và B có `score` bằng nhau, thì A > B nếu chuỗi A lớn hơn về thứ tự từ điển so với chuỗi B. A và B không thẻ bằng nhau, bởi vì `sorted set` chỉ có một giá trị duy nhất.

```bash
> zadd hackers 1940 "Alan Kay"
(integer) 1
> zadd hackers 1957 "Sophie Wilson"
(integer) 1
> zadd hackers 1953 "Richard Stallman"
(integer) 1
> zadd hackers 1949 "Anita Borg"
(integer) 1
> zadd hackers 1965 "Yukihiro Matsumoto"
(integer) 1
> zadd hackers 1914 "Hedy Lamarr"
(integer) 1
> zadd hackers 1916 "Claude Shannon"
(integer) 1
> zadd hackers 1969 "Linus Torvalds"
(integer) 1
> zadd hackers 1912 "Alan Turing"
(integer) 1
```

In tăng dần:

```bash
> zrange hackers 0 -1
1) "Alan Turing"
2) "Hedy Lamarr"
3) "Claude Shannon"
4) "Alan Kay"
5) "Anita Borg"
6) "Richard Stallman"
7) "Sophie Wilson"
8) "Yukihiro Matsumoto"
9) "Linus Torvalds"
```

In giảm dần:

```bash
> zrange hackers 0 -1
1) "Alan Turing"
2) "Hedy Lamarr"
3) "Claude Shannon"
4) "Alan Kay"
5) "Anita Borg"
6) "Richard Stallman"
7) "Sophie Wilson"
8) "Yukihiro Matsumoto"
9) "Linus Torvalds"
```

In ra với số `score`

```bash
> zrangebyscore hackers -inf 1950
1) "Alan Turing"
2) "Hedy Lamarr"
3) "Claude Shannon"
4) "Alan Kay"
5) "Anita Borg"
```

## Pub/Sub

<div align="center">
    <img src="images/pub-sub.png" alt="...">
</div>

Cơ chế hoạt động giống như, khi `subcribe` một channel trên youtube. Khi một producer đăng tải một video lên youtube. Thì tất cả client `subcribe` channel đó, sẽ nhận được thông báo là video đăng được đăng lên.

Subscribe một hoặc nhiều kênh:

```bash
SUBSCRIBE first second
*3
$9
subscribe
$5
first
:1
*3
$9
subscribe
$6
second
:2
```

Khi từ một client khác, `PUSHLISH` đến channels `second`

```bash
> PUBLISH second Hello
```

Ở client đầu tiên sẽ nhận được tin nhắn:

```bash
*3
$7
message
$6
second
$5
Hello
```

Client có thể unsubscribe bằng lệnh `UNSUBCRIBE`

```bash
UNSUBSCRIBE
*3
$11
unsubscribe
$6
second
:1
*3
$11
unsubscribe
$5
first
:0
```

Pattern-matching subscriptions

```bash
PSUBSCRIBE news.*
PUNSUBSCRIBE news.*
```

## Lock

### Cơ bản về Lock

Khóa là cơ chế giúp cho các truy cập đồng thời cùng một shared resource. Ta dùng lock để tránh lost update, dead lock,... 

### Pessimistic

Là chiến lược lcok trước tài nguyên (rows) trước khi end user modify. Giả sử User 1 và User 2 là hai người dùng khác nhau sử dụng Pesimistic locking, cả hai đều cố gắng thay đổi cùng một row:

- User 1 call EmployeeImpl.setSalary(1000) trên một row cụ thể, do đó user 1 ngay lập tức có được khóa trên row đó.
- User 2 call EmployeeImpl.setSalary(2000) trên một row tượng tự, lúc này User 2 sẽ nhận được exception là row này đã bị lock.

Chiến lược `Pessimistic` không cần phải check xem version nào, bởi vì không có khả năng một dòng bị thay đổi bởi một transaction cùng một lúc. Tuy nó chỉ hữu dụng trong môi trường stateful hay connected environment, giống như là luôn giữ kết nối database như kiểu client/server. Trong các application bây giờ số lượng end user càng lớn thì việc giữ connection quá là xa xỉ.

### Optimistic

Là chiến lược chỉ lock tại thời điểm user modifying. Cách này không phải luôn giữ connection với database. Chiến lược này nếu không khéo rất dễ bị lost update. Ví dụ bảng emp có trường name và date_of_birth. Cùng 1 lúc có 2 users A và B query duex liệu record 5 trên application của mình. Sau đó A sửa trường name rồi commit. Tiếp theo B sửa trường date_of_birth rồi cũng commit. Một lát sua A query lại record 5 thấy vẫn là name cũ.

Vậy để tránh lost update có 2 cách:

- Tạo thêm ột column (kiểm interger hoặc date/timestamp) để lưu version của record. Việc maintain "version" column có thể thực hiện manually hoặc auto to thông qua trigger
- Sử dụng checksum hoặc hash function để tính toán ra một giá trị dựa trên dữ liệu gốc.

## Reference

- [Lock](https://en.wikipedia.org/wiki/Lock_(computer_science))
