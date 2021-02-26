mac = ["aabb:cc80:7000", "aabb:dd80:7340", "aabb:ee80:7000", "aabb:ff80:7000"]
mac_ciscoo = []

for mac_cisco in mac:
    mac_ciscoo.append(mac_cisco.replace(':', '.'))

print(mac_ciscoo)
