import socket
import time
PORT = 10006
SERVER = socket.gethostbyname(socket.gethostname())
FORMAT = "utf-8"

c=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

name=input("Please Enter your name: ")

c.connect((SERVER,PORT))

c.send(name.encode(FORMAT))
#i.send(string.encode(FORMAT))
# nm=c.recv(1024).decode('utf-8')
rounds=int(c.recv(1).decode('utf-8'))
buffer=int(c.recv(1).decode('utf-8'))

for j in range (0,buffer):
	print(c.recv(1024).decode('utf-8'))

while True:
    for j in range(0,rounds):
        print(c.recv(1024).decode('utf-8'))
        i=input("Please Enter Card number: ")
        c.send(i.encode(FORMAT))
        print("")

        
    print(c.recv(1024).decode('utf-8'))
    A=c.recv(1).decode('utf-8')
    if A=="N":
        break