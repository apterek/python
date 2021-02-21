ip = "192.168.3.1"

ip = ip.replace('.',' ').split()


template = '''

{0:<10}{1:<10}{2:<10}{3:<10}
{0:08b}  {1:08b}  {2:08b}  {3:08b}

'''

print(template.format(int(ip[0]),int(ip[1]),int(ip[2]),int(ip[3])))
