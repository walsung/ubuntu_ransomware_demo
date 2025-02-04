import os
from cryptography.fernet import Fernet

# === DECRYPTION SAFEGUARDS ===
DECRYPT_HEADER = b'encrypted'  # Must match encryption header
LINUX_EXCLUDED_DIRS = {'/bin', '/usr', '/lib', '/proc', '/sys', '/dev', '/boot'}

def linux_decrypt_file(key_path, file_path):
    """Safe Ubuntu decryption with verification"""
    try:
        with open(key_path, 'rb') as key_file:
            key = key_file.read()
        fernet = Fernet(key)
        
        with open(file_path, 'rb+') as f:
            data = f.read()
            
            if not data.startswith(DECRYPT_HEADER):
                print(f"Not encrypted: {file_path}")
                return
                
            encrypted_data = data[len(DECRYPT_HEADER):]
            decrypted = fernet.decrypt(encrypted_data)
            
            f.seek(0)
            f.write(decrypted)
            f.truncate()
            
        print(f"Decrypted: {file_path}")
    except Exception as e:
        print(f"DECRYPT ERROR: {file_path} - {str(e)}")

def batch_decrypt_ubuntu(key_path='~/DECRYPTION_KEY.key', target_dir='~/encryption_test'):
    """Safe directory decryption"""
    key_path = os.path.expanduser(key_path)
    target_dir = os.path.expanduser(target_dir)
    
    if not os.path.exists(key_path):
        sys.exit("ERROR: Missing decryption key")
        
    for root, dirs, files in os.walk(target_dir):
        # Skip system directories
        dirs[:] = [d for d in dirs if not os.path.realpath(os.path.join(root, d)) in LINUX_EXCLUDED_DIRS]
        
        for file in files:
            file_path = os.path.join(root, file)
            linux_decrypt_file(key_path, file_path)

if __name__ == "__main__":
    print("""
    [UBUNTU DECRYPTION PROTOCOL]
    1. Requires DECRYPTION_KEY.key in home directory
    2. Only decrypts files from test directory
    3. Verifies encryption header first
    """)
    
    confirm = input("Type 'DECRYPT TEST' to continue: ").strip()
    if confirm != "DECRYPT TEST":
        sys.exit("Cancelled by user")
        
    batch_decrypt_ubuntu('~/DECRYPTION_KEY.key', '/home/ubuntu/Downloads/test_encrypt')
    
    print("""
    [VERIFICATION STEPS]
    1. Check file contents:
       cat ~/encryption_test/test_0.txt
       
    2. Verify file type:
       file ~/encryption_test/test_0.txt
       (Should show 'ASCII text')
    """)

