import socket
FORMAT='utf-8'
PORT=5050
c=socket.socket()
c.connect(('localhost',PORT))
FORMAT = "utf-8"
times=(input("Number of times cars will be coming : "))
c.send(times.encode(FORMAT))
Queue=input("Enter the cars incoming : ")
Queue=Queue.replace(" ","")
c.send(Queue.encode(FORMAT))
for i in range(1,int(times)):
	Queue_add=input("Enter the cars incoming : " )
	Queue_add=Queue_add.replace(" ","")
	c.send(Queue_add.encode(FORMAT))
