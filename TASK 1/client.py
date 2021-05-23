import socket
PORT = 10006
SERVER = socket.gethostbyname(socket.gethostname())
# SERVER="localhost"
FORMAT = "utf-8"

client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# name=input("Please Enter your name: ")

client.connect((SERVER,PORT))
no=1 
rounds=2
while (rounds%no==0):
	print("Ensure rounds is not a multiple of Players ")
	no=int(input("Enter Number of Players : "))
	rounds=int(input("Enter Number of Rounds : "))

#i.send(string.encode(FORMAT))
# nm=c.recv(1024).decode('utf-8')

client.send((str(no)).encode(FORMAT))
client.send((str(rounds)).encode(FORMAT))
rounds=rounds+1

for j in range (0,no):
		print(client.recv(1024).decode('utf-8'))
while True:
	for j in range(0,rounds):
		print(client.recv(1024).decode('utf-8'))
	#print(client.recv(1024).decode('utf-8'))	
	print("Do you wish to play again. \n Y for Yes \n N for No")
	A=input("ANSWER :")
	print("")
	client.send((A).encode(FORMAT))	
	if(A=="N"):
		break