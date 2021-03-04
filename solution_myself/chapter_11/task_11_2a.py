from task_11_2 import create_network_map
from draw_network_graph import draw_topology

infiles = [
    'sh_cdp_n_sw1.txt',
    'sh_cdp_n_r1.txt',
    'sh_cdp_n_r2.txt',
    'sh_cdp_n_r3.txt'
]

#def unique_network_map(topology_dict):
#    unique_topology = {}
#    
#    for key, value in topology_dict.items():
#        if not unique_topology.get(value) == key:
#            unique_topology[key] = value
#    return unique_topology

    #Второй вариант
def unique_network_map(topology_dict):
    network_map = {}
    for key, value in topology_dict.items():
       key, value = sorted([key, value])
       network_map[key] = value
    return network_map

result = draw_topology(unique_network_map(create_network_map(infiles)))
print(result)