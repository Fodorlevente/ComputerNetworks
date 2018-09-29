import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 10000)   #int(sys.argv[1])
sock.bind(server_address)
sock.listen(1)

connection, client_address = sock.accept()

data = connection.recv(32)
connection.sendall("Hello client!")

print data

sock.close()