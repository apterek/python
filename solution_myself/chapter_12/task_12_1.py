import subprocess


def ping_ip_addresses(spisok_ip):
    available = []
    not_available = []
    for ip in spisok_ip:
        reply = subprocess.run(['ping', '-n', '1', ip ], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(reply.returncode)
        if reply.returncode == 0:
            available.append(ip)
            
        else:
            not_available.append(ip)            
    return available, not_available


ip_for_check = ['8.8.8.8', '1.1.1.1', 'ya.ru', '192.168.101.1']

if __name__ == "__main__":  
    print(ping_ip_addresses(ip_for_check))