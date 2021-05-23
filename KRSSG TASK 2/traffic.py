import socket

s=socket.socket()
PORT=5050
s.bind(('localhost',PORT))
# serversocket.bind((SERVER,PORT))
FORMAT = "utf-8"
s.listen(1)
print("Waiting for connections....")
conn,addr=s.accept()
print("Connection Successful!!")

def createstring(stringnumber):
        string ="A Straight \n"*(int(stringnumber[0]))+"A Right \n"*(int(stringnumber[1]))+"B Straight \n"*(int(stringnumber[2]))+"B Right \n"*(int(stringnumber[3]))+"C Straight \n"*(int(stringnumber[4]))+"C Right \n"*(int(stringnumber[5]))+"D Straight\n"*(int(stringnumber[6]))+"D Right\n"*(int(stringnumber[7]))
        return string



# times=int(conn.recv(1).decode('utf-8'))
times=int(conn.recv(1).decode('utf-8'))
Queue=(conn.recv(8).decode('utf-8'))
print(f"Queue after Input : {Queue}")


def Transition(Queue):

    transition_states=["11000000","10000001","10100000","01001000","01010000","00010010","00001010","00000011"
                ,"00000101","00110000","00100100","00001100","10000000","01000000","00100000","00010000"
                ,"00001000","00000100","00000010","00000001"]

    valid_transition=""
    QueueList=[]
    for i in range(0,len(Queue)):
        QueueList.append(int(Queue[i]))

    MaxIndex=QueueList.index(max(QueueList))
    for i in transition_states:
        if int(i[MaxIndex])==1:
            i = i[:MaxIndex] + i[MaxIndex + 1:]
            i=i[:MaxIndex]+"0"+i[MaxIndex:]

            if i.find("1")==-1:
                
                i = i[:MaxIndex] + i[MaxIndex + 1:]
                i=i[:MaxIndex]+"1"+i[MaxIndex:]
                valid_transition=i
                string=createstring(valid_transition)
                break
            else:
                if(QueueList[i.index("1")]):
                    
                    i=i[:MaxIndex] + i[MaxIndex + 1:]
                    i=i[:MaxIndex]+"1"+i[MaxIndex:]
                    valid_transition=i
                    string=createstring(valid_transition)
                    break
               
    int_Queue=int(Queue)
    int_valid_transition=(int(valid_transition))
    int_newQueue=int_Queue-int_valid_transition       
    Queue=str(int_newQueue)
    extra=8-len(Queue)
    Queue="0"*extra+Queue 
    print(string)
    print(f"Queue after traffic removal : {Queue}")
    return Queue

takes=1
while not(Queue == "00000000"):

    print(f"Time Step : {takes}")
    takes+=1
    Queue=Transition(Queue)
    if times>1:

        # Queue_add=input("Enter the cars incoming : " )
        # Queue_add=Queue_add.replace(" ","")
        # print(len(Queue_add))
        Queue_add=(conn.recv(8).decode('utf-8'))
        int_final=int(Queue_add)+int(Queue)
        Queue=str(int_final)
        extra=8-len(Queue)
        Queue="0"*extra+Queue
        print(f"Queue after Input : {Queue}")
        times-=1

conn.close()
print("Traffic Removed!!!")

            






