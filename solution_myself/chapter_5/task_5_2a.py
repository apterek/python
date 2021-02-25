ip_and_mask = input("Введите адрес и маску в формате Х.Х.Х.Х/Y \n")

ip_and_mask = ip_and_mask.split('/')

ip = ip_and_mask[0].split('.')
mask = int(ip_and_mask[1])

mask_in_2 = mask * "1" + (32 - mask) * "0"

ip_in_2 = '{0:08b}{1:08b}{2:08b}{3:08b}'.format(int(ip[0]), int(ip[1]), int(ip[2]), int(ip[3]))
ip_in_2 = ip_in_2.replace('0b', '')
network_address = ip_in_2[:mask] + (32 - mask) * "0"

template_ip = '''
Network:

{0:<10}{1:<10}{2:<10}{3:<10}

{0:08b}  {1:08b}  {2:08b}  {3:08b}

'''
template_mask = '''
Mask:
/{0}
{1:<10}{2:<10}{3:<10}{4:<10}
{1:08b}  {2:08b}  {3:08b}  {4:08b}

'''


print(template_ip.format(
    int(network_address[0:8],2),
    int(network_address[8:16],2),
    int(network_address[16:24],2),
    int(network_address[24:32],2)
))

print(template_mask.format(
    mask,
    int(mask_in_2[:8],2),
    int(mask_in_2[8:16],2),
    int(mask_in_2[16:24],2),
    int(mask_in_2[24:32],2)
))


