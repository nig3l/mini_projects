import socket

# Creating TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Binding the socket to a specific address and port
server_address = ('localhost', 12345)
server_socket.bind(server_address)