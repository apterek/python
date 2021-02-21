ospf_route = "      10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"

route = ospf_route.replace(',',' ').replace('[',' ').replace(']',' ')
result = route.split()

template = '''
Prefix             {:30}
AD/Metric          {:30}
Next-Hop           {:30}
Last update        {:30}
Outbound Interface {:30}
'''

print(template.format(result[0],result[1],result[3],result[4],result[5]))



'''

#ANSWER from NATALYA:

ospf_route = "      10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"

output = "\n{:25} {}" * 5

route = ospf_route.replace(",", " ").replace("[", "").replace("]", "")
route = route.split()

print(output.format(
        "Prefix", route[0],
        "AD/Metric", route[1],
        "Next-Hop", route[3],
        "Last update", route[4],
        "Outbound Interface", route[5],
))



'''
