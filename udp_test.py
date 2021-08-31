import socket

host_name = "127.0.0.1"
host_port = 9997

client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

client.sendto(b"aaaaaa",(host_name,host_port))

data, addr = client.recvfrom(4096)

print(data.decode())
client.close()
