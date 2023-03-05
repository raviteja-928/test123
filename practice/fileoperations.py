


ab = open(r"C:\Users\LENOVO\Downloads\data.txt")
# print(ab.read())
print(ab.read(5))

ab = ("data.txt", "r")
for each in ab:
	print(each)

ab = open(r"C:\Users\LENOVO\Downloads\data.txt",'a')
ab.write('red\n')
ab = open(r"C:\Users\LENOVO\Downloads\data.txt",'r')
print(ab.read())
ab = open(r"C:\Users\LENOVO\Downloads\data.txt",'w')
ab.write('yellow')
ab = open(r"C:\Users\LENOVO\Downloads\data.txt",'r')
print(ab.read())



import socket
hostname = socket.gethostname()
ipaddr = socket.gethostbyname(hostname)
print(ipaddr)

import socket
hostname = socket.gethostname()
ipaddr = socket.gethostbyname(hostname)
print(ipaddr)