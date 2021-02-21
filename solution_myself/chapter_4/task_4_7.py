mac = "AAAA:BBBB:CCCC"
mac = mac.replace(':','')
result = int(mac , 16)


print('{:8b}'.format(result))
