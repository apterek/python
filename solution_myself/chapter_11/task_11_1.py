def parse_cdp_neighbors(command_output):
    parser_dict = {}
    for line in command_output.split('\n'):
        columns = line.split()
        if ">" in line:
            hostname = line.split(">")[0] 
        elif len(columns) >= 5 and columns[3].isdigit():
            r_router, t_intf_l, n_intf_l, *other, t_intf_r, n_intf_r = columns
            parser_dict[hostname,t_intf_l + n_intf_l] = (r_router, t_intf_r + n_intf_r)
    return parser_dict

if __name__ == "__main__":
    with open('sh_cdp_n_sw1.txt') as f:
        print(parse_cdp_neighbors(f.read()))
