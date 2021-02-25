access_template = [
    "switchport mode access",
    "switchport access vlan {}",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

trunk_template = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan {}",
]

access_or_trunk = input('Введите режим работы интерфейса (access/trunk): \n')
interface = input('Введите тип и номер интерфейса: \n')
vlans = input('Введите номер влан(ов): \n')

vclb = {"access" : access_template,"trunk" : trunk_template}
mode = vclb[access_or_trunk]
print('interface{}'.format(interface))
print('\n'.join(mode).format(vlans))



