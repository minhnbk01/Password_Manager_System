# Hệ Thống Quản Lý Mật Khẩu Cá Nhân

Một ứng dụng dòng lệnh (CLI) bằng Python giúp quản lý mật khẩu cá nhân một cách an toàn. Dự án được thiết kế với các tính năng bảo mật cao, bao gồm mã hóa dữ liệu, bàn phím ảo chống keylogger, và băm mật khẩu.

## Mục Lục

- [Tính Năng](#tính-năng)
- [Yêu Cầu Hệ Thống](#yêu-cầu-hệ-thống)
- [Cài Đặt](#cài-đặt)
- [Cấu Trúc Dự Án](#cấu-trúc-dự-án)
- [Hướng Dẫn Sử Dụng](#hướng-dẫn-sử-dụng)
- [Cấu Hình](#cấu-hình)
- [Bảo Mật](#bảo-mật)

## Tính Năng

### Tính Năng Chung
- **Quản lý người dùng**: Đăng ký và đăng nhập an toàn.
- **Quản lý mật khẩu (CRUD)**: Thêm, xem danh sách, xem chi tiết, cập nhật và xóa mật khẩu của các dịch vụ khác nhau.
- **Lưu trữ linh hoạt**: Hỗ trợ lưu trữ dữ liệu bằng file `.txt` cục bộ hoặc trên cơ sở dữ liệu `MySQL`.

### Tính Năng Bảo Mật
- **Bàn phím ảo (Virtual Keyboard)**: Giao diện đồ họa (Tkinter) để nhập mật khẩu, hỗ trợ xáo trộn phím (shuffle) nhằm chống lại phần mềm theo dõi thao tác bàn phím (Keylogger).
- **Tạo mật khẩu tự động**: Sinh mật khẩu ngẫu nhiên có độ phức tạp cao.
- **Kiểm tra độ mạnh mật khẩu**: Yêu cầu mật khẩu phải từ 8 ký tự trở lên, gồm chữ hoa, chữ thường, số và ký tự đặc biệt.

## Yêu Cầu Hệ Thống

- **Python**: 3.x trở lên
- **Thư viện Python**: `bcrypt`, `cryptography`, `mysql-connector-python`
- **Cơ sở dữ liệu**: MySQL Server (Nếu dùng chế độ lưu trữ MySQL)
- **Giao diện**: Yêu cầu hỗ trợ Tkinter (thường đi kèm mặc định với Python) để hiển thị bàn phím ảo.

## Cài Đặt

### 1. Cài đặt các thư viện cần thiết
Mở terminal/command prompt và chạy lệnh:
```bash
pip install bcrypt cryptography mysql-connector-python
```

### 2. Khởi tạo cơ sở dữ liệu (Nếu sử dụng MySQL)
Mở file `config.py` và điều chỉnh thông tin kết nối, sau đó chạy lệnh để tự động tạo database và bảng:
```bash
python database_setup.py
```

## Cấu Trúc Dự Án

```
ATTT/
    ├── README.md                 # Tệp này - Hướng dẫn dự án
    ├── config.py                 # File cấu hình chung (DB, Secret Key)
    ├── database_setup.py         # Script khởi tạo cơ sở dữ liệu MySQL
    ├── main.py                   # Điểm vào của ứng dụng (Khởi động menu chính)
    │
    ├── security_utils.py         # Xử lý băm mật khẩu, mã hóa, sinh mật khẩu
    ├── virtual_keyboard.py       # Cung cấp giao diện bàn phím ảo (Tkinter)
    │
    ├── user_service_file.py      # Logic quản lý user (Lưu File)
    ├── password_service_file.py  # Logic quản lý mật khẩu (Lưu File)
    │
    ├── user_service_db.py        # Logic quản lý user (Lưu MySQL)
    ├── password_service_db.py    # Logic quản lý mật khẩu (Lưu MySQL)
    │
    ├── users.txt                 # File lưu trữ user cục bộ (tự sinh)
    └── passwords.txt             # File lưu trữ mật khẩu cục bộ (tự sinh)
```

## Hướng Dẫn Sử Dụng

### Khởi Động Ứng Dụng

Trong terminal, chạy:
```bash
python main.py
```

### Quá Trình Đăng Nhập / Đăng Ký

Hệ thống sẽ hỏi bạn chọn chế độ lưu trữ:
```
=== CHỌN CHẾ ĐỘ LƯU TRỮ ===
1. Lưu bằng File cục bộ (.txt)
2. Lưu bằng Database (MySQL)
Lựa chọn của bạn (1-2) [Mặc định là 1]: 
```

Tiếp theo là Menu Đăng Nhập:
```
=== HỆ THỐNG QUẢN LÝ MẬT KHẨU CÁ NHÂN ===
1. Đăng ký
2. Đăng nhập
3. Thoát
Chọn chức năng (1-3): 
```
*Lưu ý: Bạn có thể chọn sử dụng Bàn phím ảo để nhập mật khẩu an toàn hơn khi được hỏi.*

### Menu Quản Lý Mật Khẩu
Sau khi đăng nhập thành công:
```
=== QUẢN LÝ MẬT KHẨU ===
1. Xem danh sách dịch vụ đã lưu
2. Xem mật khẩu của một dịch vụ
3. Thêm mật khẩu mới
4. Cập nhật mật khẩu
5. Xóa mật khẩu
6. Đăng xuất
```

## Cấu Hình

Chỉnh sửa file `config.py` để thay đổi các thông số cài đặt mặc định:

```python
# Cấu hình kết nối MySQL Database
DB_CONFIG = {
    'host': 'localhost',
    'port': '3306',
    'user': 'root',
    'password': '[PASSWORD]',
    'database': 'secure_app_db'
}

# Khóa bí mật dùng để mã hóa mật khẩu dịch vụ (Nên thay đổi bằng khóa của bạn)
SECRET_KEY = b''

# Tên file lưu trữ cục bộ
USERS_FILE = 'users.txt'
PASSWORDS_FILE = 'passwords.txt'
```

## Bảo Mật

- **Băm mật khẩu Master**: Mật khẩu của người dùng được băm bằng `bcrypt` với `salt` tự động sinh để chống lại tấn công Rainbow Table.
- **Mã hóa mật khẩu dịch vụ**: Sử dụng mã hóa đối xứng AES (thông qua `cryptography.fernet`). Dữ liệu lưu trong database/file là dữ liệu đã được mã hóa không thể đọc trực tiếp.
- **Chống Keylogger**: Cung cấp `virtual_keyboard.py` để nhập mật khẩu bằng cách click chuột, đặc biệt hữu ích khi thiết bị có nguy cơ bị cài phần mềm gián điệp.


