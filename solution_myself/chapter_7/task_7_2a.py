#from sys import argv

ignore = ["duplex","alias","configuration"]
#filename = argv[1]
#with open(filename) as f:
with open('config_sw1.txt') as f:
    for line in f:
        line = line.split()
        if line.startswith('!'):
            pass
        elif ignore[0] in line:
            pass
        elif ignore[1] in line:
            pass
        elif ignore[2] in line:
            pass
        else:
            print(line)
