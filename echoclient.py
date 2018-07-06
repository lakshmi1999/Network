import socket
udpip="10.1.24.122"
udpport=6789
Message=("hii from client")
bytesToSend=str.encode(Message)
clientSock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
clientSock.sendto(bytesToSend,(udpip,udpport))
data=clientSock.recvfrom(1024)
print(data)
       
