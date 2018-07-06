# Network
import socket
udpip="10.1.24.121"
udpport=6002
serverSock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
serverSock.bind((udpip,udpport))
print("server is waiting")
while True:
  data,addr=serverSock.recvfrom(1024)
  print("Message",data)
