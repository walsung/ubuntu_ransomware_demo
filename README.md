

# Python3 Ransomware Educational Demo - UBUNTU VERSION ⚠️

**❗ WARNING: THIS IS A HIGHLY EXPERIMENTAL DEMO FOR RESEARCH PURPOSES ONLY**  
**By using this code, you acknowledge full responsibility for any consequences** 

The codes have been modified to include additional controls for verifying Linux directories and to display confirmation text when executing the Python 3 script.

---

## 🔍 Overview
This proof-of-concept ransomware demo is designed **exclusively for cybersecurity education**, aiming to:
- Demonstrate modern ransomware implementation mechanisms
- Inspire defense strategies research 
- Promote ethical penetration testing techniques 
- Explore AI-driven security innovations (non-malicious context) 

---

## ⚠️ Critical Requirements Before Execution
1. **Mandatory Environment**  
   ```diff
   + Use isolated VM (VirtualBox/VMWare) 
   + Disable network interfaces
   - Never run on production systems 
   ```

2. **Data Protection**  
   ```bash
   # Create full disk snapshot
   sudo timeshift --create --comments "Pre-ransomware-test"
   ```

3. **System Compatibility**  
   ```diff
   ! Current version targets Ubuntu 22.04 LTS
   ! Requires significant modifications for Windows compatibility 
   ```

---

## 📜 Legal & Ethical Declaration
```text
THIS SOFTWARE IS PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND. 
MISUSE MAY VIOLATE:
- Computer Fraud and Abuse Act (US)
- GDPR Article 32 (EU)
- Cybersecurity Law of China (Article 27)
```
**Developers assume no liability** for unauthorized usage 

---

## 🛠️ Platform-Specific Notes
### For Windows Adaptation
```diff
# Major required modifications:
1. File path conversion (POSIX -> Win32)
2. Crypto API replacement (OpenSSL -> CNG)
3. Service injection mechanism redesign 
```

### Linux Security Features
```bash
# Recommended protection measures:
sudo apt install tripwire rkhunter
echo "inotify.max_user_watches=1048576" >> /etc/sysctl.conf
```

---

## 📚 Reference Implementation Path
```python
# Sample encryption logic (DO NOT DEPLOY)
from cryptography.fernet import Fernet
key = Fernet.generate_key()  # Store this securely!
```

---

## 🌐 Contribution Guidelines
We welcome **ethical security researchers** to improve:
- Defense detection patterns
- Behavior analysis modules
- AI-based attack simulation frameworks 

