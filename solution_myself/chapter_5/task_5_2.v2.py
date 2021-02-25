
ip_and_mask = input("Введите Ip и маску в формате Х.Х.Х.Х/Y \n")

ip_mask = ip_and_mask.split('/')

mask = int(ip_mask[1])
mask_in_2 = mask * "1" + (32 - mask) * "0"



ip = ip_mask[0].split('.')

template_ip = '''
Network:
{0:<10}{1:<10}{2:<10}{3:<10}
{0:08b}  {0:08b}  {0:08b}  {0:08b}

'''
template_mask = '''
Mask:
/{0}
{1:<10}{2:<10}{3:<10}{4:<10}
{1:08b}  {2:08b}  {3:08b}  {4:08b}

'''


print(template_ip.format(int(ip[0]),int(ip[1]),int(ip[2]),int(ip[3])))
print(template_mask.format(
    mask,
    int(mask_in_2[:8],2),
    int(mask_in_2[8:16],2),
    int(mask_in_2[16:24],2),
    int(mask_in_2[24:32],2)
))
















