import socket

host = input('Host~$ ')
portinp = input('Port~$ ')
port = int(portinp)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

while True:
    s.send(input('Cmd~$ ').encode())