command1 = "switchport trunk allowed vlan 1,2,3,5,8"
command2 = "switchport trunk allowed vlan 1,3,8,9"



result = set((command1.split()[-1]).split(',')) & set((command2.split()[-1]).split(',')) 
print(result)

