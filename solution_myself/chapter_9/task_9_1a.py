access_mode_template = [
    "switchport mode access",
    "switchport access vlan",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

port_security_template = [
    "switchport port-security maximum 2",
    "switchport port-security violation restrict",
    "switchport port-security",
]

access_config = {"FastEthernet0/12": 10, "FastEthernet0/14": 11, "FastEthernet0/16": 17}


def generate_access_config(intf_vlan_mapping, access_template, psecurity = None):
    access_config = []
    for intf, vlan in intf_vlan_mapping.items():
        access_config.append(f"{intf}")
        for line in access_template:
            if line.endswith('access vlan'):
                access_config.append(f"{line}{vlan}")
            else:
                access_config.append(f"{line}")
        if psecurity:
            access_config.extend(psecurity)
    return access_config

print(generate_access_config(access_config, access_mode_template,port_security_template ))