import socket
import threading
import random
import time
rounds=0
SERVER = socket.gethostbyname(socket.gethostname())
PORT = 10006
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind((SERVER,PORT))
FORMAT = "utf-8"
r=1
def card(i):
	r=int((i-1)/13)
	
	if(r==0):
		s=" of Diamond"
	elif(r==1):
		s=" of Hearts"
	elif(r==2):
		s=" of Spades"
	elif(r==3):
		s=" of Clubs"
	r=(i%13)
	if(r==0):
		s2="King"
	elif(r==12):
		s2="Queen"
	elif(r==11):
		s2="Jack"
	elif(r==1):
		s2="Ace"
	else:
		s2=str(r)

	return (s2+s)
def d_cards(i,cardL,coN):

    S=f"{card(cardL[3*i])} \n{card(cardL[3*i+1])} \n{card(cardL[3*i+2])}"
    coN.send(S.encode(FORMAT))
    k=1
    k=int(coN.recv(1024).decode(FORMAT))
    MaxCards[i]=cardL[(k-1+(3*i))]
    MaxCards[i]=(MaxCards[i]-1)%13

# Start of func Game
def game(r,cardL,connL,no):
    
    if not(r==rounds+1):
        threads=[None]*no
        for i in range(0,no):
            threads[i]=threading.Thread(target=d_cards,args=(i,cardL,connL[i]))
            threads[i].start()

        ti=0
        while(None in MaxCards and ti<50):
            time.sleep(1)
            ti=ti+1
        while(None in MaxCards):
            n=MaxCards.index(None)
            MaxCards[n]=-1

        Max=MaxCards[0]
        WinIndex=[0]
        send_st=f"The winner(s) of round {round_char}{r} is/are \n"
        #send_st=f"The winner(s) of round {r} is/are \n"
        for i in range(1,no):
            if(MaxCards[i]>Max):
                WinIndex.clear()
                WinIndex.append(i)
                Max=MaxCards[i]
            elif(MaxCards[i]==Max):
                WinIndex.append(i)
        print(f"The winner(s) of round {round_char}{r} is/are ")
        #print(f"The winner(s) of round {r} is/are ")
        for i in WinIndex:
            WinCount[i]=WinCount[i]+(1/len(WinIndex))
            print(Name[i])  
            send_st+=f"{Name[i]}\n"
        zcon.send(send_st.encode(FORMAT))
        print("")
    else:
        st=f"The winner(s) of Round {round_char} is/are: \n"
        #st=f"The winner(s) of Round is/are: \n"
        Max=WinCount[0]
        WinIndex=[0]
        for j in range (1,no):
            if(WinCount[j]>Max):
                WinIndex.clear()
                WinIndex.append(j)
                Max=WinCount[j]
            elif(WinCount[j]==Max):
                WinIndex.append(j)
        for j in WinIndex:
            st+=f"{Name[j]}\n"
        zcon.send(st.encode(FORMAT))
        print(st)
        for i in connL:
            i.send(st.encode(FORMAT))
        
 
 #All Functions Finish Here

serversocket.listen(1)
print("Waiting for connections...")
zcon,zadd=serversocket.accept()
print("Connecion Succesful!!")
no=int(zcon.recv(1).decode('utf-8'))
rounds=int(zcon.recv(1).decode('utf-8'))
WinCount=[0]*no
MaxCards=[None]*no
connL=[]
buffer = no
round_char="A"
Name=[]
serversocket.listen(no)
while (buffer>0):
    
    conn,addr = serversocket.accept()
    nm=conn.recv(1024).decode('utf-8')
    Name.append(nm)
    conn.send(f"{rounds}".encode(FORMAT))
    conn.send(f"{buffer}".encode(FORMAT))
    if buffer>1:
        print(f"{no-buffer+1} Players Connected!!")
        conn.send(bytes((f"Hey {Name[no-buffer]}! Welcome to Birmingham Gamblers!! \nWaiting for {buffer-1} player(s) to join"),'utf-8'))
    else:
        print("Lets Begin!!")
        conn.send((f"Hey {Name[no-buffer]}! Welcome to Birmingham Gamblers!! \nLet's begin the game!!\n").encode(FORMAT))

    
    for j in connL :
        if(buffer>1):
            j.send(bytes((f"Waiting for {buffer-1} player(s) to join"),'utf-8'))
        else:
            j.send((f"Let's begin the game!!\n").encode(FORMAT))

    if(buffer>1):
        zcon.send(bytes((f"Waiting for {buffer-1} player(s) to join"),'utf-8'))
    else:
        zcon.send((f"Let's begin the game!!\n").encode(FORMAT))

    connL.append(conn)

    buffer=buffer-1

while r<=rounds+1 :

    MaxCards=[None]*no
    cardL = random.sample(range(1,53),3*no)
    game(r,cardL,connL,no)
    
    if r==rounds+1:
        A=zcon.recv(2).decode(FORMAT)
        if A == "Y":
            r = 0
            WinCount.clear()
            WinCount=[0]*no
            p=ord(round_char)
            p+=1
            round_char=chr(p)
        for i in connL:
            i.send(A.encode(FORMAT)) 
    r=r+1
   
zcon.close()
for j in connL:
    j.close()
