access_template = [
    "switchport mode access",
    "switchport access vlan",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

trunk_template = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan",
]

access = {"0/12": "10", "0/14": "11", "0/16": "17", "0/17": "150"}
trunk = {"0/1": ["add", "10", "20"], "0/2": ["only", "11", "30"], "0/4": ["del", "17"]}

for intf, vlan in access.items():
    print("interface FastEthernet" + intf)
    for command in access_template:
        if command.endswith("access vlan"):
            print(f" {command} {vlan}")
        else:
            print(f" {command}")


for intf_t, value in trunk.items():
    print("interface FastEthernet" + intf)
    action = value[0]

  
    vlans_2 = ",".join(value[1:]) 


    if action == 'add':
        for command_t in trunk_template:
            if command_t.endswith("allowed vlan"):
                print(f" {command_t} {action} {vlans_2}")
            else:
                print(f" {command_t}") 
    elif action == 'only':
        for command_t in trunk_template:
            if command_t.endswith("allowed vlan"):
                print(f" {command_t} {vlans_2}")
            else:
                print(f" {command_t}")
    elif action == 'del':
        for command_t in trunk_template:
            if command_t.endswith("allowed vlan"):
                print(f" {command_t} remove {vlans_2}")

