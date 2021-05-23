#!/usr/bin/env python3
#!/usr/bin/env python3


# from RRT_connect import Curr_nodes
import cv2 as cv
import numpy as np
import random
import matplotlib.pyplot as plt
import time
La_SolEdges=[]
def signum(i):
    if(i>0):
        return 1
    else: return -1

def resize_frame(frame,scale):
    resized_dimensions=(int(frame.shape[0]*scale),int(frame.shape[1]*scale))
    return cv.resize(frame,resized_dimensions,interpolation=cv.INTER_AREA)
def resize_frame2(frame):
    resized_dimensions=(int(500),int(500))
    return cv.resize(frame,resized_dimensions,interpolation=cv.INTER_AREA)
STARTCOLOR=(27,216,17)
ENDCOLOR=(13,13,243)
Obs_Color=(243,226,207)
img=cv.imread("photo2.png")
# cv.imshow("image",img)
# cv.waitKey(0)
img=resize_frame(img,2)
img2=img.copy()
Shape=(img.shape[1],img.shape[0]) ##Shape tuple first element is Columns(Width) Second is Rows(Height)
print(Shape)
# plt.show()
#SNodes and ENodes store the list of the start and end nodes as well as their diameters 
SNodes=[]
ENodes=[]
Curr_nodes_st=[]
Curr_nodes_end=[]
# def change_weight(li,change):
#     if(li==None):
#         return
#     for i in li:
#         i.weight=i.weight-change
#         change_weight(i.NextNodes,change)

class Node:
 
    def __init__(self,x1,y1):
        
        self.x=x1
        self.y=y1
        self.PrevNode=None
        self.PrevEdge=None
        # self.NextNodes=None ##List
        self.NextNodes=[]
        self.weight=0
        self.type=0
    def isTraversable(self):
        if(abs(img[self.y,self.x][0]-Obs_Color[0])<50 and abs(img[self.y,self.x][1]-Obs_Color[1])<50 and abs(img[self.y,self.x][2]-Obs_Color[2])<50):
            return False
        else: return True
    
    def colorNode(self,color):
        cv.rectangle(img,(self.x-2,self.y-2),(self.x+2,self.y+2),color,thickness=-1)


    
    def isEndNode(self):
        if(((self.x-CENTRE_END[1])**2+(self.y-CENTRE_END[0])**2)<=(dE/2)**2):
            return True
        else :return False
    # def isStartNode(self):
    #     if(abs(self.x-CENTRE_START[1])<(dS/2) and abs(self.y-CENTRE_START[0])<(dS/2)):
    #         return True
    #     else :return False

    def Compare(self,node):
        if self==None or node==None:
            return False
        else :
            return ((self.x==node.x) and (self.y==node.y))
#all(test_list[i] <= test_list[i + 1] for i in range(len(test_list)-1))
    def isTraversable2(Node1,Node2,noss):

        # if(isTraversable2.counter==2):
        #     isTraversable2.counter=0
        #     return True 
        Bol=True 
        x_curr=Node1.x
        y_curr=Node1.y
        # print("Hlo")
        if(x_curr==Node2.x and y_curr==Node2.y):
            return False 

        if not (Node2.x==Node1.x):
            const=abs((Node2.y-Node1.y)/(Node2.x-Node1.x))

        while (not (x_curr==Node2.x and y_curr==Node2.y)):
            if(all(abs(img[y_curr,x_curr][i]-Obs_Color[i])<70 for i in range(0,3))):
                Bol=False 
                break 
            if(Node2.x==x_curr):
                y_curr+=signum((Node2.y-y_curr))
                continue 
            v=abs((Node2.y-Node1.y)/(Node2.x-Node1.x))
            if(v>const):
                y_curr+=signum(Node2.y-y_curr)
            else:
                x_curr+=signum(Node2.x-x_curr)
        # if(Bol==False):
            # print("No")
        if(noss==1):
            return Bol 

        if Bol:
            return (Node.isTraversable2(Node2,Node1,1))

        return False 
        


class Edge:
    def __init__(self,Node1,Node2):
        self.edge =[Node1,Node2]
    def colorEdge(self,color,tcc):
        Scord=(self.edge[0].x,self.edge[0].y)
        Ecord=(self.edge[1].x,self.edge[1].y)
        cv.line(img, Scord, Ecord, color, thickness=tcc)

    def Compare(self,Ed):

    	return ((self.edge[0].x==Ed.edge[0].x and self.edge[0].y==Ed.edge[0].y and self.edge[1].x==Ed.edge[1].x and self.edge[1].y==Ed.edge[1]) or (self.edge[1].x==Ed.edge[0].x and self.edge[1].y==Ed.edge[0].y and self.edge[0].x==Ed.edge[1].x and self.edge[0].y==Ed.edge[1].y))


# STARTCOLOR=(27,216,17)
# ENDCOLOR=(13,13,243)
# img=cv.imread("photo1.PNG")

def resize_frame(frame,scale):
    resized_dimensions=(int(frame.shape[0]*scale),int(frame.shape[1]*scale))
    return cv.resize(frame,resized_dimensions,interpolation=cv.INTER_AREA)

def distance(x1,y1,x2,y2):
	return ((x2-x1)**2+(y2-y1)**2)**0.5
 
# Curr_nodes=[]
sT=0
dm=0
# Bol=False
# dm=0
# for i in range(0,Shape[1]):
#     for j in range(0,Shape[0]):
#         if(abs(img2[i,j][0]-STARTCOLOR[0])<30) and (abs(img2[i,j][1]-STARTCOLOR[1])<30) and (abs(img2[i,j][2]-STARTCOLOR[2])<30):
#             sT=i
#             dm=0

#             while(abs(img2[sT,j][0]-STARTCOLOR[0])<50) and (abs(img2[sT,j][1]-STARTCOLOR[1])<50) and (abs(img2[sT,j][2]-STARTCOLOR[2])<50):
#                 dm+=1
#                 sT+=1

#             tup=(j,int((sT+i-1)/2),dm)
#             SNodes.append(tup)
#             node=Node(tup[0],tup[1])
#             node.type=1
#             Curr_nodes_st.append(node)
#             # print(tup[0],tup[1])
#             cv.circle(img2,(int(tup[0]),int(tup[1])),int((dm+10)/2),(0,0,0),thickness=-1)
#             # print(f"dm start={dm}")
#             # cv.imshow("image",img2)
#             # cv.waitKey(0)
#             # time.sleep(100)

#         if (abs(img2[i,j][0]-ENDCOLOR[0])<30) and (abs(img2[i,j][1]-ENDCOLOR[1])<30) and (abs(img2[i,j][2]-ENDCOLOR[2])<30):
#             sT=i 
#             dm=0
#             while (abs(img2[sT,j][0]-ENDCOLOR[0])<30) and (abs(img2[sT,j][1]-ENDCOLOR[1])<30) and (abs(img2[sT,j][2]-ENDCOLOR[2])<30):
#                 dm+=1
#                 sT+=1
#             tupl=(j,int((sT+i-1)/2),dm)
#             node=Node(tupl[0],tupl[1])
#             node.type=2
#             Curr_nodes_end.append(node)
#             cv.circle(img2,(int(tupl[0]),int(tupl[1])),int((dm+10)/2),(0,0,0),thickness=-1)
            
# dS=tup[2]
# dE=tupl[2]
# print(dS,dE)
# 56 72
# 187 72
# 57 655
# 713 272
# 698 774
# 399 792

node=Node(56,72)
Curr_nodes_end.append(node)
node=Node(187,72)
Curr_nodes_end.append(node)
node=Node(57,655)
Curr_nodes_end.append(node)
node=Node(713,272)
Curr_nodes_st.append(node)
node=Node(698,774)
Curr_nodes_st.append(node)
node=Node(399,792)
Curr_nodes_st.append(node)
inp=int(input("Enter start node :\n1.Top left\n2.Top Right\n3.Bottom Left\nInput:  "))
StartNode=Curr_nodes_end[inp-1]
inp=int(input("Enter End node :\n1.Top Right\n2.Bottom Right\n3.Bottom Left\nInput:  "))
# print(Curr_nodes_end,"\n",Curr_nodes_st)
# for i in range(0,3):
#     print(Curr_nodes_end[i].x,Curr_nodes_end[i].y)

# for i in range(0,3):
#     print(Curr_nodes_st[i].x,Curr_nodes_st[i].y)


EndNode=Curr_nodes_st[inp-1]
CENTRE_END=(EndNode.y,EndNode.x)
# print(EndNode.x,EndNode.y)
CENTRE_START=(StartNode.y,StartNode.x)
# print(CENTRE_START)

class rrtstar:
    
    def __init__(self,Start,EndNode,Iter,Step_Len,prob_value,radius):
        
        
        self.StartNode=Start
        self.StartNode.type=1
        self.curr_list_st=[self.StartNode]
        self.End=EndNode
        self.End.type=2
        self.curr_list_end=[self.End]
        self.length=Step_Len
        self.NodeSets=[[None for i in range(Shape[0])] for j in range(Shape[1])]   #---> alag se in RRT*  
        self.NodeSets[self.StartNode.y][self.StartNode.x]=self.StartNode 
        self.NodeSets[self.End.y][self.End.x]=self.End        
        self.prob_num=prob_value    
        self.Radius=radius
        self.iter=Iter       
    def change_weight(self,li,change):
        if(li==None):
            return
        for i in li:
            self.NodeSets[i.y][i.x].weight=self.NodeSets[i.y][i.x].weight-change
            rrtstar.change_weight(self,i.NextNodes , change)

    def solution(self):
        SolEdges=[]
        # shrey=False
        kushaz=self.prob_num
        SolWeight=1000000
        counter=2*self.iter
        
        # for i in range(0,self.iter):
        while(counter>0):
            shrey=False
            
            p_st=random.randint(0,9)
            if(p_st<kushaz):
                Rand=(random.randint(CENTRE_END[1]-20,CENTRE_END[1]+20),random.randint(CENTRE_END[0]-20,CENTRE_END[0]+20))
            else :
                Rand=(random.randint(0,Shape[0]-1),random.randint(0,Shape[1]-1))
            MinDist=1000000
            ClosestNode=None
            X=0
            Y=0
            for j in self.curr_list_st:
                PresentDist=((Rand[0]-j.x)**2+(Rand[1]-j.y)**2)**0.5
                if PresentDist<MinDist:
                    ClosestNode=j
                    MinDist=PresentDist
            # print(ClosestNode.x," ",ClosestNode.y)
            if MinDist:
                X=int(ClosestNode.x+int(self.length*(Rand[0]-ClosestNode.x)/MinDist))
                Y=int(ClosestNode.y+int(self.length*(Rand[1]-ClosestNode.y)/MinDist))
                if X>=Shape[0]:
                    X=(Shape[0]-1)
                elif X<0:
                    X=0
                if Y>=Shape[1]:
                    Y=(Shape[1]-1)
                elif Y<0:
                    Y=0
            
                # print(X," ",Y)
                NewNode=Node(X,Y)
                NewNode.type=1
                
                # OtherNode=None
                #Adding parent node to NewNode
                #shrey is false
                if(Node.isTraversable(NewNode) and self.NodeSets[NewNode.y][NewNode.x]==None):
                    shrey=True  
                    x_coord=None 
                    y_coord=None 
                    minimum=10000
                    ## TASK 1-FINDING BEST POSSIBLE PARENT NODE
                    for j in self.curr_list_st:
                        # for k in range((-self.Radius),int((self.Radius+1))):
                        # if(j+NewNode.y<Shape[1] and k+NewNode.x<Shape[0] and j+NewNode.y>=0 and k+NewNode.x>=0):
                            # if(self.NodeSets[j+NewNode.y][k+NewNode.x]!=None and self.NodeSets[j+NewNode.y][k+NewNode.x].type==1):
                        if(distance(j.x,j.y,NewNode.x,NewNode.y)<=self.Radius and minimum>distance(NewNode.x,NewNode.y,j.x,j.y)+self.NodeSets[j.y][j.x].weight and Node.isTraversable2(NewNode,j,0)):
                            minimum=distance(NewNode.x,NewNode.y,j.x,j.y)+self.NodeSets[j.y][j.x].weight
                            x_coord=j.x
                            y_coord=j.y

                    if(x_coord==None):
                        # continue
                        shrey=False
                        # print(i,shrey)

                if(shrey==True):
                    counter-=1
                    # print(i,shrey)
                    Node.colorNode(NewNode,(0,255,255))
                    NewNode.weight=minimum
                    self.curr_list_st.append(NewNode)
                    self.NodeSets[NewNode.y][NewNode.x]=NewNode
                    self.NodeSets[y_coord][x_coord].NextNodes.append(NewNode)
                    NewNode.PrevNode=(self.NodeSets[y_coord][x_coord])
                    t=Edge(NewNode,NewNode.PrevNode)
                    Edge.colorEdge(t,(60,20,220),2)
	 				
                		#I feel the love and I feel it burn down this river, every turn, Hope is r 4 letter word 
                    ##TASK 2-FINDING IF THIS NEW NODE CAN BE A BETTER PARENT NODE FOR OTHER NODES
                    for j in self.curr_list_st:
                        # for k in range((-self.Radius),int((self.Radius+1))):
                            # if(j+NewNode.y<Shape[1] and k+NewNode.x<Shape[0] and j+NewNode.y>=0 and k+NewNode.x>=0):
                                # if(self.NodeSets[j+NewNode.y][k+NewNode.x]!=None and self.NodeSets[j+NewNode.y][k+NewNode.x].type==1):
                        if(distance(NewNode.x,NewNode.y,j.x,j.y)<=(self.Radius) and (NewNode.weight+distance(NewNode.x,NewNode.y,j.x,j.y))<self.NodeSets[j.y][j.x].weight and Node.isTraversable2(NewNode,j,0)):
                            previous=self.NodeSets[j.y][j.x].PrevNode
                            change=self.NodeSets[j.y][j.x].weight-(NewNode.weight+distance(NewNode.x,NewNode.y,j.x,j.y))

                            for l in range(0,len(previous.NextNodes)):
                                if(j.PrevNode.NextNodes[l].x==(j.x)) and (j.PrevNode.NextNodes[l].y==(j.y)):
                                    self.NodeSets[j.y][j.x].PrevNode.NextNodes.pop(l)
                                    break 

                            self.NodeSets[j.y][j.x].PrevNode=NewNode
                            self.NodeSets[j.y][j.x].weight=(NewNode.weight+distance(NewNode.x,NewNode.y,j.x,j.y))
                            NewNode.NextNodes.append(self.NodeSets[j.y][j.x])
                            rrtstar.change_weight(self,self.NodeSets[j.y][j.x].NextNodes,change)
                            color=(60,20,220)
                            tc=2
                            for l in SolEdges:
                                if Edge.Compare(l,Edge(self.NodeSets[j.y][j.x].PrevNode,previous)):
                                    color=(245,105,65)
                                    tc=4
                            Edge.colorEdge(Edge(NewNode,self.NodeSets[j.y][j.x]),color,tc)
                            Edge.colorEdge(Edge(previous,self.NodeSets[j.y][j.x]),(0,0,0),tc)

                    #TASK-3
                    min_x=None
                    min_y=None                 
                    for j in self.curr_list_end:
                        # for k in range((-self.Radius),int((self.Radius+1))):
                            # if(j+NewNode.y<Shape[1] and k+NewNode.x<Shape[0] and j+NewNode.y>=0 and k+NewNode.x>=0):
                                # if(self.NodeSets[j+NewNode.y][k+NewNode.x]!=None and self.NodeSets[j+NewNode.y][k+NewNode.x].type==2):
                        if(distance(j.x,j.y,NewNode.x,NewNode.y)<=self.Radius and SolWeight>(NewNode.weight+self.NodeSets[j.y][j.x].weight+distance(NewNode.x,NewNode.y,j.x,j.y)) and Node.isTraversable2(j,NewNode,0)):
                            SolWeight=(NewNode.weight+self.NodeSets[j.y][j.x].weight+distance(NewNode.x,NewNode.y,j.x,j.y))
                            kushaz=-1
                            min_x=j.x
                            min_y=j.y
                                       

                    if(min_x!=None):
                        ConnecT=Edge(self.NodeSets[min_y][min_x],NewNode)
                        Edge.colorEdge(ConnecT,(245,105,65),4)

                        for i in SolEdges:
                            Edge.colorEdge(i,(0,0,0),4)
                            Edge.colorEdge(i,(60,20,220),2)

                        SolEdges.clear()
                        
                        PresentNode1=self.NodeSets[min_y][min_x]

                        while(not(PresentNode1.PrevNode==None)):
                            # print("Hlo")
                            Dedge1=Edge(PresentNode1.PrevNode,PresentNode1)
                            SolEdges.append(Dedge1)
                            Edge.colorEdge(Dedge1,(245,105,65),4)
                            PresentNode1=PresentNode1.PrevNode
                        SolEdges.reverse()
                        SolEdges.append(ConnecT)
                        PresentNode2=NewNode
                        while(not(PresentNode2.PrevNode==None)):
                            Dedge2=Edge(PresentNode2,PresentNode2.PrevNode)
                            SolEdges.append(Dedge2)
                            Edge.colorEdge(Dedge2,(245,105,65),4)
                            PresentNode2=PresentNode2.PrevNode


            p_st=random.randint(0,9)
            if(p_st<kushaz):
                Rand=(random.randint(CENTRE_START[1]-20,CENTRE_START[1]+20),random.randint(CENTRE_START[0]-20,CENTRE_START[0]+20))
            else :
                Rand=(random.randint(0,Shape[0]-1),random.randint(0,Shape[1]-1))
            MinDist=100000 
            ClosestNode=None
            X=0
            Y=0
            for j in self.curr_list_end:
                PresentDist=((Rand[0]-j.x)**2+(Rand[1]-j.y)**2)**0.5
                if PresentDist<MinDist:
                    ClosestNode=j
                    MinDist=PresentDist
            if MinDist:
                X=int(ClosestNode.x+int(self.length*(Rand[0]-ClosestNode.x)/MinDist))
                Y=int(ClosestNode.y+int(self.length*(Rand[1]-ClosestNode.y)/MinDist))
                if X>=Shape[0]:
                    X=(Shape[0]-1)
                elif X<0:
                    X=0
                if Y>=Shape[1]:
                    Y=(Shape[1]-1)
                elif Y<0:
                    Y=0
           

                NewNode=Node(X,Y)
                NewNode.type=2
                
                # OtherNode=None
                #Adding parent node to NewNode
                if(Node.isTraversable(NewNode) and self.NodeSets[NewNode.y][NewNode.x]==None):
                    
                    
                    x_coord=None 
                    y_coord=None 
                    minimum=10000
                    ## TASK 1-FINDING BEST POSSIBLE PARENT NODE
                    # print(NewNode.x,NewNode.y)
                    for j in self.curr_list_end:
                        # for k in range((-self.Radius),int((self.Radius+1))):
                            # if(j+NewNode.y<Shape[1] and k+NewNode.x<Shape[0] and j+NewNode.y>=0 and k+NewNode.x>=0):
                                # if(self.NodeSets[j+NewNode.y][k+NewNode.x]!=None and self.NodeSets[j+NewNode.y][k+NewNode.x].type==2):
                        if(distance(j.x,j.y,NewNode.x,NewNode.y)<=self.Radius and minimum>distance(NewNode.x,NewNode.y,j.x,j.y)+self.NodeSets[j.y][j.x].weight and Node.isTraversable2(NewNode,j,0)):
                            minimum=distance(NewNode.x,NewNode.y,j.x,j.y)+self.NodeSets[j.y][j.x].weight
                            x_coord=j.x
                            y_coord=j.y
                    if(x_coord==None):
                        continue 
                    counter-=1
                    Node.colorNode(NewNode,(0,255,255))
                    NewNode.weight=minimum
                    self.curr_list_end.append(NewNode)
                    self.NodeSets[NewNode.y][NewNode.x]=NewNode
                    self.NodeSets[y_coord][x_coord].NextNodes.append(NewNode)
                    NewNode.PrevNode=(self.NodeSets[y_coord][x_coord])
                    Edge.colorEdge((Edge(NewNode,NewNode.PrevNode)),(0,255,0),2)
	 				
                		#I feel the love and I feel it burn down this river, every turn, Hope is r 4 letter word 
                    ##TASK 2-FINDING IF THIS NEW NODE CAN BE A BETTER PARENT NODE FOR OTHER NODES
                    for j in self.curr_list_end:
                        # for k in range((-self.Radius),int((self.Radius+1))):
                            # if(j+NewNode.y<Shape[1] and k+NewNode.x<Shape[0] and j+NewNode.y>=0 and k+NewNode.x>=0):
                                # if(self.NodeSets[j+NewNode.y][k+NewNode.x]!=None and self.NodeSets[j+NewNode.y][k+NewNode.x].type==2):
                        if(distance(NewNode.x,NewNode.y,j.x,j.y)<=self.Radius and (NewNode.weight+distance(NewNode.x,NewNode.y,j.x,j.y))<self.NodeSets[j.y][j.x].weight and Node.isTraversable2(NewNode,j,0)):
                            previous=self.NodeSets[j.y][j.x].PrevNode
                            change=self.NodeSets[j.y][j.x].weight-(NewNode.weight+distance(NewNode.x,NewNode.y,j.x,j.y))

                            for l in range(0,len(previous.NextNodes)):
                                if(previous.NextNodes[l].x==j.x and previous.NextNodes[l].y==j.y):
                                    self.NodeSets[j.y][j.x].PrevNode.NextNodes.pop(l)
                                    break 

                            self.NodeSets[j.y][j.x].PrevNode=NewNode
                            self.NodeSets[j.y][j.x].weight=(NewNode.weight+distance(NewNode.x,NewNode.y,j.x,j.y))
                            NewNode.NextNodes.append(self.NodeSets[j.y][j.x])
                            rrtstar.change_weight(self,self.NodeSets[j.y][j.x].NextNodes,change)
                            color=(0,255,0)
                            tc=2
                            for l in SolEdges:
                                if Edge.Compare(l,Edge(self.NodeSets[j.y][j.x].PrevNode,previous)):
                                    color=(245,105,65)
                                    tc=4
                            Edge.colorEdge(Edge(NewNode,self.NodeSets[j.y][j.x]),color,tc)
                            Edge.colorEdge(Edge(previous,self.NodeSets[j.y][j.x]),(0,0,0),tc)

                    #TASK-3
                    min_x=None
                    min_y=None 
                    for j in self.curr_list_st:
                        # for k in range((-self.Radius),int((self.Radius+1))):
                        #     if(j+NewNode.y<Shape[1] and k+NewNode.x<Shape[0] and j+NewNode.y>0 and k+NewNode.x>0):
                        #         if(self.NodeSets[j+NewNode.y][k+NewNode.x]!=None and self.NodeSets[j+NewNode.y][k+NewNode.x].type==1):
                        if(distance(NewNode.x,NewNode.y,j.x,j.y)<=self.Radius and SolWeight>(NewNode.weight+self.NodeSets[j.y][j.x].weight+distance(NewNode.x,NewNode.y,j.x,j.y)) and Node.isTraversable2(j,NewNode,0)):
                            kushaz=-1
                            min_x=j.x
                            min_y=j.y
                            SolWeight=NewNode.weight+self.NodeSets[j.y][j.x].weight+distance(NewNode.x,NewNode.y,j.x,j.y)
                                       

                    if(min_x!=None):
                        # print(Node.isTraversable2(self.NodeSets[min_y][min_x],NewNode))
                        ConnecT=Edge(NewNode,self.NodeSets[min_y][min_x])
                        Edge.colorEdge(ConnecT,(245,105,65),4)
                        for i in SolEdges:

                            Edge.colorEdge(i,(0,0,0),4)
                            Edge.colorEdge(i,(0,255,0),2)

                        SolEdges.clear()
                        temp=[]
                        PresentNode1=NewNode
                        while(not(PresentNode1.PrevNode==None)):
                            # print("Hlo")
                            Dedge1=Edge(PresentNode1.PrevNode,PresentNode1)
                            SolEdges.append(Dedge1)
                            Edge.colorEdge(Dedge1,(245,105,65),4)
                            PresentNode1=PresentNode1.PrevNode

                        SolEdges.reverse()
                        SolEdges.append(ConnecT)

                        PresentNode2=self.NodeSets[min_y][min_x]  
                        while(not(PresentNode2.PrevNode==None)):
                            Dedge2=Edge(PresentNode2,PresentNode2.PrevNode)
                            SolEdges.append(Dedge2)
                            Edge.colorEdge(Dedge2,(245,105,65),4)
                            PresentNode2=PresentNode2.PrevNode

                    #After this we need to check in the circle for a opp(green or .type=2) and make bonds and copy for red then backtracking and then chill
#--------------------------------------------Done Till here------------------------------------------------------------------------------------------------------------------------------------------------------------------
                
    # What doesn't kills you makes you stronger..................
    #Sharp edges have concequences 

                cv.imshow("image",img)
                cv.waitKey(1)
        tempN=Node(CENTRE_START[1],CENTRE_START[0])
        elem=0
        Ball=True
        # La_SolEdges=[]
        while (not (tempN.x==CENTRE_END[1] and tempN.y==CENTRE_END[0])):
            Ball=True
            if(Node.isTraversable2(tempN,SolEdges[elem].edge[0],0)):
                La_SolEdges.append(Edge(tempN,SolEdges[elem].edge[0]))
                tempN=SolEdges[elem].edge[0]
                elem=0
                Ball=False

            if Ball:
                elem+=1

        game_winn=Edge(La_SolEdges[len(La_SolEdges)-1].edge[1],EndNode)
        La_SolEdges.append(game_winn)
        # test_list=[]
        for i in SolEdges:
            # print(i.edge[0].x,i.edge[0].y)
            # print(distance(i.edge[0].x,i.edge[0].y,CENTRE_START[1],CENTRE_START[0]))
            # test_list.append(distance(i.edge[0].x,i.edge[0].y,CENTRE_END[1],CENTRE_END[0]))
            # print(i.edge[1].x,i.edge[1].y)
            Edge.colorEdge(i,(0,0,0),4)

        # flag = 0
        # if(all(test_list[i] <= test_list[i + 1] for i in range(len(test_list)-1))):
        #     flag = 1
        # print(flag)

        for i in La_SolEdges:
            Edge.colorEdge(i,(245,105,65),5)

        img2=resize_frame2(img)
        # print(img.shape[0]," ",img.shape[1])
        cv.imshow("final",img2)
        cv.waitKey(0)

# def __init__(self,Start,EndNode,Iter,Step_Len,prob_value,radius):
ITERATIONS=int(input("NUMBER OF ITERATIONS : "))
# STARTNODE=Node(CENTRE_START[1],CENTRE_START[0])

RRT = rrtstar(StartNode,EndNode,ITERATIONS,23,3,45)
rrtstar.solution(RRT)
# print(La_SolEdges)




