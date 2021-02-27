output = "\n{:25} {}" *5


with open('ospf.txt') as f:
    for line in f:
        line = line.split()
        print(output.format(
            "Prefix:",line[1],
            "AD/Metric:",line[2].replace('[','').replace(']',''),
            "Next-Hop:",line[4].replace(',',''),
            "Last update:",line[5].replace(',',''),
            "Outbound Interface",line[6]    
        ))
        
