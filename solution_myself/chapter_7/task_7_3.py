
with open('CAM_table.txt') as f:
    for line in f:
        row = line.split()
        #if row == []: это мой вариант проверки, что в строке что-то есть
        #    continue
        if row and row[0].isdigit():
            print('{:10}{:20}{:20}'.format(row[0],row[1],row[3]))
