import ipaddress
addr=input("Enter the ip ")
#input("Enter the prefix")
ip=addr.split("/")
print(ip[1])
print(addr)
n=ipaddress.IPv4Network('145.0.0.0/8')
first,last=n[0],n[-1]
print(first)
print(last)
