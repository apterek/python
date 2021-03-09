import ipaddress
from tabulate import tabulate

reachable = ['1.1.1.1', '8.8.8.8']

unreachable = ['10.10.1.1', '192.168.11.1']

def print_ip_table(reach_ip, unreach_ip):
    table = {"Reachable": reach_ip, "Unreachable": unreach_ip}
    print(tabulate(table, headers="keys"))


print_ip_table(reachable, unreachable)
