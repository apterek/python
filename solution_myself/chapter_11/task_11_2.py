from task_11_1 import parse_cdp_neighbors

infiles = [
    'sh_cdp_n_sw1.txt',
    'sh_cdp_n_r1.txt',
    'sh_cdp_n_r2.txt',
    'sh_cdp_n_r3.txt'
]

def create_network_map(filenames):
    dict_back = {}
    for line in filenames:
        with open(line) as f:
            dict_parse = parse_cdp_neighbors(f.read()) #считывание файла построчно
        dict_back.update(dict_parse)
    return dict_back
    
if __name__ == "__main__":
    topology = create_network_map(infiles)
    print(topology)
