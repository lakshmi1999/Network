import socket
udpip="10.1.24.121"
udpport=6002
Message=("hii")
bytesToSend=str.encode(Message)
clientSock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
clientSock.sendto(bytesToSend,(udpip,udpport))
