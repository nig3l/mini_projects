import socket

'''


# serverside

# Creating TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Binding the socket to a specific address and port
server_address = ('localhost', 12345)
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(1)

print('Server is up and running. Waiting for a connection...')

while True:
    # Wait for a connection
    client_socket, client_address = server_socket.accept()

    print('Received connection from:', client_address)

    # Receive and print data from the client
    data = client_socket.recv(1024)
    print('Received data:', data.decode())

        # Send a response back to the client
    response = 'Server received your message: ' + data.decode()
    client_socket.sendall(response.encode())

    # Close the client socket
    client_socket.close()

'''

# clientside(TCP client)

# Create a TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the server's address and port
server_address = ('localhost', 12345)
client_socket.connect(server_address)

# Send data to the server
message = 'Hello, server!'
client_socket.sendall(message.encode())



