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

## Important
In the code, there are lines with a hashtag (#) that are commented out. These are intended to use the RockYou wordlist to expand the set of usernames and passwords for guessing. By uncommenting these lines, you can load this list and increase the likelihood of a successful SSH login. This is particularly useful for penetration testing, as it allows for the use of a more extensive set of credentials.
