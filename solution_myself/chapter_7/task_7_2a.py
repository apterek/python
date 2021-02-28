#from sys import argv

ignore = ["duplex","alias","configuration"]
#filename = argv[1]
#with open(filename) as f:
with open('config_sw1.txt') as f:
    for line in f:
        word = line.split()

        correct = set(word) & set(ignore)
        if not line.startswith('!') and not correct:
            print(line.rstrip())
            
