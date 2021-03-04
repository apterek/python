from os import subprocess


#def ping_ip_addresses(spisok_ip):
#    result = []
#    for ip in spisok_ip:
#        result = 



#    return result

result = subprocess.run(['ping','8.8.8.8'])

print(result)