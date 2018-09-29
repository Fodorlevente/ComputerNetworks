

import socket
import sys
import struct

# Ugly but works...
def operations(operator, lhs, rhs):
    if operator == "+":
        return int(lhs + rhs)
    if operator == "-":
        return int(lhs - rhs)
    if operator == "*":
        return int(lhs * rhs)
    if operator == "/":
        return int(lhs / rhs)
    else:
        raise Exception('Operator must be [+,-,*,/] and other two arguments must be number types!')


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 10000)   #int(sys.argv[1])
sock.bind(server_address)
sock.listen(1)

connection, client_address = sock.accept()

unpacker = struct.Struct('f f s')


data1 = connection.recv(32)
unpacked_data1 = unpacker.unpack(data1)
msg = operations(unpacked_data1[2],unpacked_data1[0],unpacked_data1[1])
connection.sendall("Result: " + str(msg))

data2 = connection.recv(32)
unpacked_data2 = unpacker.unpack(data2)
msg = operations(unpacked_data2[2], unpacked_data2[0], unpacked_data2[1])
connection.sendall("Result: " + str(msg))
 
data3 = connection.recv(32)
unpacked_data3 = unpacker.unpack(data3)
msg = operations(unpacked_data3[2], unpacked_data3[0], unpacked_data3[1])
connection.sendall("Result: " + str(msg))
 
data4 = connection.recv(32)
unpacked_data4 = unpacker.unpack(data4)
msg = operations(unpacked_data4[2], unpacked_data4[0], unpacked_data4[1])
connection.sendall("Result: " + str(msg))

sock.close()