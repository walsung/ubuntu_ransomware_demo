import os
import sys
import getpass
from cryptography.fernet import Fernet

# === UBUNTU-SPECIFIC SAFEGUARDS ===
LINUX_EXCLUDED_DIRS = {'/bin', '/usr', '/lib', '/proc', '/sys', '/dev', '/boot'}
LINUX_EXCLUDED_EXT = {'.sh', '.py', '.key', '.so', '.a'}
MAX_FILE_SIZE = 1024 * 1024  # 1MB limit for safety

def linux_security_check(path):
    """Ubuntu-specific protection layer"""
    real_path = os.path.realpath(path)
    
    # Prevent system directory access
    if any(real_path.startswith(dir) for dir in LINUX_EXCLUDED_DIRS):
        print(f"BLOCKED system path: {real_path}")
        return False
        
    # Check file extension
    if any(real_path.endswith(ext) for ext in LINUX_EXCLUDED_EXT):
        print(f"BLOCKED extension: {real_path}")
        return False
        
    # Size protection
    try:
        if os.path.getsize(path) > MAX_FILE_SIZE:
            print(f"BLOCKED large file: {real_path}")
            return False
    except:
        return False
        
    return True

def generate_key():
    """Store key in user's home directory"""
    key = Fernet.generate_key()
    key_path = os.path.expanduser("~/DECRYPTION_KEY.key")
    with open(key_path, 'wb') as f:
        f.write(key)
    print(f"Key saved to {key_path}")
    return key

def encrypt_file(key, file_path):
    if not linux_security_check(file_path):
        return
        
    try:
        fernet = Fernet(key)
        
        with open(file_path, 'rb+') as f:
            data = f.read()
            if data.startswith(b'encrypted'):
                print(f"Already encrypted: {file_path}")
                return
                
            encrypted = fernet.encrypt(data)
            f.seek(0)
            f.write(b'encrypted')  # Header for identification
            f.write(encrypted)
            f.truncate()
            
        print(f"Success: {file_path}")
    except Exception as e:
        print(f"ERROR: {file_path} - {str(e)}")

def linux_batch_encrypt(key, test_dir):
    """Ubuntu-safe directory traversal"""
    if not os.path.exists(test_dir):
        print(f"Creating test directory: {test_dir}")
        os.makedirs(test_dir, exist_ok=True)
        
        # Create safe test files
        for i in range(3):
            test_file = os.path.join(test_dir, f"test_{i}.txt")
            with open(test_file, 'w') as f:
                f.write(f"Ubuntu test file {i} - Safe for demonstration")
                
    for root, dirs, files in os.walk(test_dir):
        # Remove excluded directories from traversal
        dirs[:] = [d for d in dirs if linux_security_check(os.path.join(root, d))]
        
        for file in files:
            file_path = os.path.join(root, file)
            encrypt_file(key, file_path)

if __name__ == "__main__":
    # === UBUNTU SAFETY CHECKS ===
    if getpass.getuser() == 'root':
        sys.exit("NEVER run as root/sudo!")
        
    test_dir = os.path.expanduser("/home/ubuntu/Downloads/test_encrypt")
    print(f"""\n
    [UBUNTU SAFETY PROTOCOL]
    1. Test directory: {test_dir}
    2. Max file size: {MAX_FILE_SIZE} bytes
    3. Excluded system directories: {LINUX_EXCLUDED_DIRS}
    """)
    
    confirm = input("Type 'UBUNTU TEST' to continue: ").strip()
    if confirm != "UBUNTU TEST":
        sys.exit("Cancelled by user")
        
    key = generate_key()
    linux_batch_encrypt(key, test_dir)
    
    print(f"""
    [VERIFICATION]
    1. Check files in {test_dir}:
       cat ~/encryption_test/test_0.txt
       (Should show encrypted binary data)
       
    2. Check key file:
       ls -l ~/DECRYPTION_KEY.key
    """)
