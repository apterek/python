def get_int_vlan_map(config_filename):
    access_voc = {}
    trunk_voc = {}
    with open(config_filename) as f:

        for line in f:
            if line.startswith('interface'):
                row = line.split()[1]
            elif 'access vlan' in line:
                access_voc[row] = int(line.split()[-1])
            elif 'allowed vlan' in line:
                #row_3 = line.split()[-1]
                trunk_voc[row] = [int(row_4) for row_4 in line.split()[-1].split(',')]          
        return access_voc, trunk_voc

print(get_int_vlan_map('config_sw1.txt'))
