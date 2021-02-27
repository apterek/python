

with open("config_sw1.txt") as f:
    for line in f:
        line = line.strip()
        if line.startswith('!'):
            pass
        else:
            print(line)