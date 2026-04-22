import security_utils
import os

def ensure_passwords_file_exists():
    if not os.path.exists('passwords.txt'):
        with open('passwords.txt', 'w', encoding='utf-8') as f:
            pass

def add_password(user_id, service_name, account_username, plain_password):
    ensure_passwords_file_exists()
    
    # Check if service already exists
    with open('passwords.txt', 'r', encoding='utf-8') as f:
        for line in f:
            parts = line.strip().split(':')
            if len(parts) == 4 and parts[0] == str(user_id) and parts[1] == service_name:
                print(f"     [!] Bạn đã lưu mật khẩu cho dịch vụ '{service_name}' rồi.")
                return False

    encrypted_password = security_utils.encrypt_data(plain_password)
    with open('passwords.txt', 'a', encoding='utf-8') as f:
        f.write(f"{user_id}:{service_name}:{account_username}:{encrypted_password.decode('utf-8')}\n")
        print(f"     [+] Đã lưu mật khẩu cho dịch vụ '{service_name}' thành công.")
    return True

def get_passwords(user_id):
    ensure_passwords_file_exists()
    passwords = []
    with open('passwords.txt', 'r', encoding='utf-8') as f:
        for line in f:
            parts = line.strip().split(':')
            if len(parts) == 4 and parts[0] == str(user_id):
                passwords.append({
                    'service_name': parts[1],
                    'account_username': parts[2]
                })
    
    if not passwords:
        print("     [i] Bạn chưa lưu mật khẩu nào.")
        return []
        
    print("\n--- DANH SÁCH DỊCH VỤ ĐÃ LƯU ---")
    for idx, pw in enumerate(passwords, 1):
        print(f"{idx}. {pw['service_name']} (Tài khoản: {pw['account_username']})")
    print("---------------------------------")
    return passwords

def get_password(user_id, service_name):
    ensure_passwords_file_exists()
    with open('passwords.txt', 'r', encoding='utf-8') as f:
        for line in f:
            parts = line.strip().split(':')
            if len(parts) == 4 and parts[0] == str(user_id) and parts[1] == service_name:
                account_username = parts[2]
                encrypted_password = parts[3]
                
                decrypted_password = security_utils.decrypt_data(encrypted_password)
                print(f"\n[+] Thông tin dịch vụ: {service_name}")
                print(f"    Tài khoản: {account_username}")
                print(f"    Mật khẩu:  {decrypted_password}")
                return decrypted_password
                
    print(f"     [!] Không tìm thấy dịch vụ '{service_name}'.")
    return None

def update_password(user_id, service_name, new_plain_password):
    ensure_passwords_file_exists()
    lines = []
    found = False
    
    with open('passwords.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    with open('passwords.txt', 'w', encoding='utf-8') as f:
        for line in lines:
            parts = line.strip().split(':')
            if len(parts) == 4 and parts[0] == str(user_id) and parts[1] == service_name:
                found = True
                encrypted_password = security_utils.encrypt_data(new_plain_password)
                f.write(f"{user_id}:{service_name}:{parts[2]}:{encrypted_password.decode('utf-8')}\n")
            else:
                f.write(line)
                
    if found:
        print(f"     [+] Đã cập nhật mật khẩu cho '{service_name}' thành công.")
        return True
    else:
        print(f"     [!] Không tìm thấy dịch vụ '{service_name}'.")
        return False

def delete_password(user_id, service_name):
    ensure_passwords_file_exists()
    lines = []
    found = False
    
    with open('passwords.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    with open('passwords.txt', 'w', encoding='utf-8') as f:
        for line in lines:
            parts = line.strip().split(':')
            if len(parts) == 4 and parts[0] == str(user_id) and parts[1] == service_name:
                found = True
                # Skip writing this line to delete it
            else:
                f.write(line)
                
    if found:
        print(f"     [+] Đã xóa dịch vụ '{service_name}' thành công.")
        return True
    else:
        print(f"     [!] Không tìm thấy dịch vụ '{service_name}'.")
        return False