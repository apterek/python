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

vcld_v = {"access" : "Введите влан \n", "trunk" : "Введите номера вланов: \n"}
mode_2 = vcld_v[access_or_trunk]
vlans = input(mode_2)
vclb = {"access" : access_template,"trunk" : trunk_template}
mode = vclb[access_or_trunk]
print('interface{}'.format(interface))
print('\n'.join(mode).format(vlans))



