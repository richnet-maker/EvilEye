# EvilEye

# EVIL EYE

EVIL EYE is a Python-based command-line reconnaissance toolkit designed for educational and learning purposes.  
It provides basic tools for network scanning and information gathering such as port scanning, IP address lookup, and phone number analysis.

---

## Features

### 🔍 Port Scanner
- Scan TCP ports from **20 to 999**
- Detect open ports on a target IP or domain
- Displays scan time and results in real-time

### 🌐 IP Address Information
Fetch detailed IP information using the `ipinfo.io` API:
- IP address
- Hostname
- City & Region
- Country
- GPS location
- Organization (ISP)
- Postal code
- Timezone

### 📱 Phone Number Information
Analyze phone numbers using the `phonenumbers` library:
- Validity check
- Carrier name
- Timezone(s)
- Country parsing

---

## Requirements
bash
```
pip install requirements.txt
```

- Python **3.x**
- Internet connection (required for IP info lookup)
___
## RUN:
Linux
```
python3 EvilEye.py
```

WINDOWS NT
```
python EvilEye.py
```
```bash
pip install requests phonenumbers
