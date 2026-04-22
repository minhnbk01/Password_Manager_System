# Personal Password Manager (Hệ Thống Quản Lý Mật Khẩu Cá Nhân)

Đây là một ứng dụng dòng lệnh (CLI) bằng Python giúp quản lý mật khẩu cá nhân một cách an toàn. Dự án được thiết kế với các tính năng bảo mật cao, bao gồm mã hóa dữ liệu, bàn phím ảo chống keylogger, và băm mật khẩu.

## Các tính năng chính

- **Quản lý người dùng**: Đăng ký và đăng nhập hệ thống an toàn.
- **Lưu trữ linh hoạt**: Hỗ trợ hai chế độ lưu trữ:
  - **File Text Cục Bộ**: Lưu trữ dữ liệu trên các file `.txt`.
  - **Cơ Sở Dữ Liệu MySQL**: Lưu trữ dữ liệu an toàn và có tổ chức trên cơ sở dữ liệu MySQL.
- **Bảo mật mạnh mẽ**:
  - **Băm mật khẩu Master**: Sử dụng thuật toán `bcrypt` để băm mật khẩu đăng nhập của người dùng.
  - **Mã hóa dữ liệu**: Sử dụng thuật toán mã hóa đối xứng AES (thông qua `cryptography.fernet`) để mã hóa mật khẩu các dịch vụ trước khi lưu trữ.
- **Bàn phím ảo (Virtual Keyboard)**: Cung cấp bàn phím ảo bằng giao diện đồ họa (Tkinter) để nhập mật khẩu, giúp chống lại các phần mềm theo dõi thao tác bàn phím (Keylogger). Hỗ trợ trộn (shuffle) vị trí các phím.
- **Tạo mật khẩu tự động**: Tích hợp công cụ sinh mật khẩu ngẫu nhiên, độ phức tạp cao.
- **Kiểm tra độ mạnh mật khẩu**: Yêu cầu mật khẩu phải có ít nhất 8 ký tự, bao gồm chữ hoa, chữ thường, số và ký tự đặc biệt.

## Yêu cầu hệ thống

- Python 3.x
- Thư viện Python: `bcrypt`, `cryptography`, `mysql-connector-python`
- MySQL Server (Nếu muốn sử dụng chế độ lưu trữ MySQL)

## Cài đặt

1. **Cài đặt các thư viện cần thiết:**

   Mở terminal và chạy lệnh:
   ```bash
   pip install bcrypt cryptography mysql-connector-python
   ```

2. **Cấu hình hệ thống:**
   
   Mở file `config.py` và cập nhật các thông tin theo môi trường của bạn:
   - Thay đổi thông số kết nối MySQL (`DB_CONFIG`) nếu bạn dùng Database.
   - `SECRET_KEY`: Có thể tạo khóa mới để bảo mật cao hơn.

3. **Khởi tạo cơ sở dữ liệu (Nếu dùng MySQL):**

   Chạy file setup để tạo database và các bảng cần thiết:
   ```bash
   python database_setup.py
   ```

## Cấu trúc thư mục

- `main.py`: File chạy chính của ứng dụng. Điểm khởi đầu của chương trình.
- `config.py`: Chứa các cấu hình về Database, Secret Key, và đường dẫn file lưu trữ.
- `database_setup.py`: Script để khởi tạo cấu trúc CSDL MySQL.
- `security_utils.py`: Các hàm tiện ích về bảo mật (Băm mật khẩu, mã hóa/giải mã, tạo/kiểm tra độ mạnh mật khẩu).
- `virtual_keyboard.py`: Giao diện bàn phím ảo bằng Tkinter.
- `user_service_file.py` / `password_service_file.py`: Logic quản lý dữ liệu sử dụng File `.txt`.
- `user_service_db.py` / `password_service_db.py`: Logic quản lý dữ liệu sử dụng MySQL.
- `users.txt` / `passwords.txt`: (Tự tạo khi chạy) Nơi lưu trữ dữ liệu nếu chọn chế độ File cục bộ.

## Hướng dẫn sử dụng

1. Khởi chạy ứng dụng:
   ```bash
   python main.py
   ```

2. Ứng dụng sẽ hỏi bạn muốn sử dụng chế độ lưu trữ nào (File hay MySQL).
3. Đăng ký tài khoản nếu chưa có, hoặc đăng nhập bằng tài khoản đã tạo.
4. (Tùy chọn) Sử dụng chức năng **Bàn phím ảo** khi được hỏi để nhập mật khẩu an toàn hơn.
5. Sau khi đăng nhập, bạn có thể thực hiện các thao tác: Thêm, Xem, Sửa, Xóa mật khẩu cho các dịch vụ khác nhau.
