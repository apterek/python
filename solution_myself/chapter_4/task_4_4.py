vlans = [10, 20, 30, 1, 2, 100, 10, 30, 3, 4, 10]


vlans = list(set(vlans))
result = sorted(vlans)

print(result,type(result))
