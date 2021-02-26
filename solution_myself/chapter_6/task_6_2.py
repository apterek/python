ip = input("Веедите Ip адрес в формате x.x.x.x \n" )

ip = ip.split('.')
broadcast = ['255', '255', '255', '255']

print(ip,type(ip))


if int(ip[0]) >= 1 and int(ip[0]) <= 223:
    print("unicast")
elif int(ip[0]) >= 224 and int(ip[0]) <= 239:
    print("multicast")
elif ip == broadcast:
    print("local broadcast")
elif ip == ['0', '0', '0', '0']:
    print("unassigned")
else:
    print("unused")
