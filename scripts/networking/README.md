<Salute!! nigel here, somewhat new to networking ?
here are some explanations of the methods used in the scripts above >

The socket.socket() function is used to create a new socket object. It takes two parameters:



socket.AF_INET: This parameter specifies the address family for the socket. In this case, AF_INET refers to the IPv4 address family.

socket.SOCK_STREAM: This parameter specifies the socket type. In this case, SOCK_STREAM indicates a TCP socket, which provides a reliable, stream-oriented connection between the client and server

By combining socket.AF_INET and socket.SOCK_STREAM, we create a TCP/IP socket that can be used for network communication over IPv4 using the TCP protocol.



