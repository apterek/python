import ipaddress

'''
def convert_ranges_to_ip_list(ip_addresses):
    ip_list = []
    for ip_address in ip_addresses:
        if "-" in ip_address:
            start_ip, stop_ip = ip_address.split("-")
            if "." not in stop_ip:
                stop_ip = ".".join(start_ip.split(".")[:-1] + [stop_ip])
            start_ip = ipaddress.ip_address(start_ip)
            stop_ip = ipaddress.ip_address(stop_ip)
            for ip in range(int(start_ip), int(stop_ip) + 1):
                ip_list.append(str(ipaddress.ip_address(ip)))
        else:
            ip_list.append(str(ip_address))
    return ip_list
'''


def convert_ranges_to_ip_list(ip_addresses):
    result = []
    for ip_range in ip_addresses:
        if '-' in ip_range:
            first_octet, second_octet = ip_range.split('-')
            if '.' not in second_octet:
                second_octet = '.'.join(first_octet.split('.')[:-1] + [second_octet])
            first_octet = ipaddress.ip_address(first_octet)
            second_octet = ipaddress.ip_address(second_octet)
            for i in range(int(first_octet), int(second_octet)):
                result.append(str(ipaddress.ip_address(i)))
        else:
            result.append(str(ip_range))
    return result






range_ip_address = ['10.10.10.97-100', '172.16.0.0', '192.168.1.0-192.168.1.8']

if __name__ == '__main__':
    print(convert_ranges_to_ip_list(range_ip_address))