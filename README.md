# Ping-Port-Scan-SSH

## Overview
**Ping-Port-Scan-SSH** is a Python script that checks if a target IP is online, scans for open ports, and tries to log in via SSH with common credentials.

## Features
- Ping a target IP to check availability.
- Scan common TCP ports (22, 80, 443, etc.).
- Attempt SSH login using a list of usernames and passwords.

## Installation
1. Clone the repository:
      git clone https://github.com/LuliPuli/Ping-Port-Scan-SSH.git
      cd Ping-Port-Scan-SSH
2. Install the required libraries:
      pip install scapy paramiko 

## Usage
sudo python/python3 ping_port_scan_ssh.py


If port 22 (SSH) is open, the program can be enhanced by incorporating the RockYou wordlist to increase the list of usernames and passwords for brute-forcing login attempts. This can be done by uncommenting the following lines in the code:
if 22 in open_ports:  # check if port SSH is open
    usernames = []
    passwords = []
    with open('/usr/share/wordlists/rockyou.txt', 'r', encoding='latin-1') as f:
        usernames = f.read().splitlines()
    with open('/usr/share/wordlists/rockyou.txt', 'r', encoding='latin-1') as f:
        passwords = f.read().splitlines()
By using the RockYou wordlist, the script can access a more extensive collection of commonly used credentials, thereby improving the chances of successfully logging into the target via SSH. This enhancement is particularly valuable for penetration testing, as it allows for a more comprehensive approach to identifying potential vulnerabilities in the system.
