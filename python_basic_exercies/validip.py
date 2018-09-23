import socket
addr = '127.0.0.1111'
try:
    socket.inet_aton(addr)
    print('Valid IP')
except socket.error:
    print('Invalid IP')
