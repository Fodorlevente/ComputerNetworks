import socket
import sys
import struct 

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 10000)   #int(sys.argv[1])
sock.connect(server_address)

value = (15.0, 2.5, '+')
value2 = (5.0, 2.5, '-')
value3 = (10, 25, '*')
value4 = (20, 5, '/')

packer = struct.Struct('f f s')

packed_data1 = packer.pack(*value)
sock.sendall(packed_data1)
data1 = sock.recv(32)

packed_data2 = packer.pack(*value2)
sock.sendall(packed_data2)
data2 = sock.recv(32)

packed_data3 = packer.pack(*value3)
sock.sendall(packed_data3)
data3 = sock.recv(32)

packed_data4 = packer.pack(*value4)
sock.sendall(packed_data4)
data4 = sock.recv(32)

print (data1 + "\n" +  data2 + "\n" + data3 + "\n" + data4 + "\n")

sock.close()