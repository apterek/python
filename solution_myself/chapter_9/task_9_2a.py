trunk_mode_template = [
    "switchport mode trunk",
    "switchport trunk native vlan 999",
    "switchport trunk allowed vlan",
]

trunk_config = {
    "FastEthernet0/1": [10, 20, 30],
    "FastEthernet0/2": [11, 30],
    "FastEthernet0/4": [17],
}

trunk_config_2 = {
    "FastEthernet0/11": [120, 131],
    "FastEthernet0/15": [111, 130],
    "FastEthernet0/14": [117],
}

def generate_trunk_config(intf_vlan_mapping, trunk_template):
    trunk_voc = {}
    for intf, vlans in intf_vlan_mapping.items():
        reslt = []
        for line in trunk_template:
            if line.endswith('allowed vlan'):
#                vlans_str = ",".join([str(vl) for vl in vlans]) Вариант от Наташи
#                reslt.append(f"{line} {vlans_str}") #это две строки от неё
                reslt.append(f"{line}{str(vlans).replace('[',' ').replace(']', '')}")
            else:
                reslt.append(f"{line}") 
        trunk_voc[intf] = reslt
    return trunk_voc
print(generate_trunk_config(trunk_config,trunk_mode_template))