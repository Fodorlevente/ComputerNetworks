import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 10000)   #int(sys.argv[1])
sock.connect(server_address)

sock.sendall("Hello server!")
data = sock.recv(32)

print data

sock.close()