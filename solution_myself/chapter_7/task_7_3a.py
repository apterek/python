row_vlan_list = []
with open('CAM_table.txt') as f:
    for line in f:
        row = line.split()
        
        #if row == []: это мой вариант проверки, что в строке что-то есть
        #    continue
        if row and row[0].isdigit():
            vlan, mac, _, intf = row
            row_vlan_list.append([int(vlan), mac, intf])

for vlan, mac, intf in sorted(row_vlan_list):
    print(f'{vlan:<9}{mac:20}{intf}')
"""
mac_table = []

with open("CAM_table.txt", "r") as conf:
    for line in conf:
        words = line.split()
        if words and words[0].isdigit():
            vlan, mac, _, intf = words
            mac_table.append([int(vlan), mac, intf])

for vlan, mac, intf in sorted(mac_table):
    print(f"{vlan:<9}{mac:20}{intf}")
    Пример решения от Натальи
"""

        
