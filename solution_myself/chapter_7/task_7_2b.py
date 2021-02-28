#from sys import argv

ignore = ["duplex","alias","configuration"]
#filename = argv[1]
#filename_2 = argv[2]
#with open(filename) as f:
with open('config_sw1.txt') as src, open('result.txt','w') as dest:
    
    for line in src:
        word = line.split()

        correct = set(word) & set(ignore)
        if not line.startswith('!') and not correct:
            dest.write(line.rstrip() + '\n')
            