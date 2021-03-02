def get_int_vlan_map(config_filename):
    access_voc = {}
    trunk_voc = {}
    with open(config_filename) as f:

        for line in f:
            if line.startswith('interface'):
                row = line.split()[1]
                # Сразу указываем, что интерфейсу
                # соответствует 1 влан в access_port_dict
                access_voc[row] = 1
            elif 'switchport access vlan' in line:
                # если нашлось другое значение VLAN,
                # оно перепишет предыдущее соответствие
                access_voc[row] = int(line.split()[-1])
            elif 'switchport trunk allowed vlan' in line:
                trunk_voc[row] = [int(row_4) for row_4 in line.split()[-1].split(',')]
                # если встретилась команда trunk allowed vlan
                # надо удалить интерфейс из словаря access_port_dict
                del access_voc[row]
        return access_voc, trunk_voc
print(get_int_vlan_map('config_sw2.txt'))