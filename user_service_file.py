import security_utils
import os

def ensure_users_file_exists():
    if not os.path.exists('users.txt'):
        with open('users.txt', 'w') as f:
            pass

def check_user_exists(username):
        with open('users.txt', 'r') as f:
            for line in f:
                if line.startswith(username + ':'):
                    return True

def register_user(username, plain_password, phone_number,email):
    with open('users.txt', 'r') as f:        
        for line in f:
            if line.startswith(username + ':'):
                print("     [!] User đã tồn tại.")
                return
    is_strong, msg = security_utils.check_password_strong(plain_password)
    if not is_strong:
        print(f"     [!] Lỗi: {msg}")
        return
    user_id = len(open('users.txt').readlines()) + 1
    hashed_password = security_utils.hash_password(plain_password)
    encrypted_phone = security_utils.encrypt_data(phone_number)
    encrypted_email = security_utils.encrypt_data(email)
    with open('users.txt', 'a') as f:
        f.write(f"{username}:{hashed_password.decode('utf-8')}:{encrypted_phone.decode('utf-8')}:{encrypted_email.decode('utf-8')}\n")
        print("     [+] Đăng ký thành công")


def login_user(username, plain_password):
    with open('users.txt', 'r') as f:
        for line in f:
            if line.startswith(username + ':'):
                parts = line.strip().split(':')
                if len(parts) != 4:
                    print("     [!] Dữ liệu người dùng không hợp lệ.")
                    return None
                _, stored_hash, encrypted_phone, encrypted_email = parts
                if security_utils.verify_password(plain_password, stored_hash):
                    print("[+] Đăng nhập thành công")
                    decrypted_phone = security_utils.decrypt_data(encrypted_phone)
                    decrypted_email = security_utils.decrypt_data(encrypted_email)
                    print(f"    SĐT: {decrypted_phone}")
                    print(f"    Email: {decrypted_email}")
                    return username
                else:
                    print("     [!] Sai mật khẩu")
                    return None

    print("     [!] Không tìm thấy người dùng")
    return None
