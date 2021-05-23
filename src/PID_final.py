#!/usr/bin/env python3
#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from math import pow, atan2, sqrt
PI = 3.1415926535897
dim=11.08889
from RRT_FINALLT import * 
Listx=[]
Listy=[] 
for i in La_SolEdges:
  X=i.edge[0].x*dim/Shape[0]
  Listx.append(X)
  Y=(Shape[1]-i.edge[0].y)*dim/Shape[1]
  Listy.append(Y)

# Listx.append(CENTRE_END[0]*dim/Shape[0])
# Listy.append((Shape[1]-CENTRE_END[1])*dim/Shape[1])   
class TurtleBot:
 
  def __init__(self):
           # Creates a node with name 'turtlebot_controller' and make sure it is a
           # unique node (using anonymous=True).
    rospy.init_node('turtlebot_controller', anonymous=True)
   
           # Publisher which will publish to the topic '/turtle1/cmd_vel'.
    self.velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
   
           # A subscriber to the topic '/turtle1/pose'. self.update_pose is called
           # when a message of type Pose is received.
    self.pose_subscriber = rospy.Subscriber('/turtle1/pose',Pose, self.update_pose)
   
    self.pose = Pose()
    self.rate = rospy.Rate(10)
    self.ang_error=None
    self.lin_error=None
    self.lin_Integral=0
    self.ang_Integral=0
  def update_pose(self, data):
#"""Callback function which is called when a new message of type Pose is
#received by the subscriber."""
    self.pose = data
    self.pose.x = round(self.pose.x, 4)
    self.pose.y = round(self.pose.y, 4)
   
  def euclidean_distance(self, goal_pose):
           #"""Euclidean distance between current pose and the goal."""
    return sqrt(pow((goal_pose.x - self.pose.x), 2) +pow((goal_pose.y - self.pose.y), 2))
   
  def linear_vel(self, goal_pose, P=1.5,I=0.0003,D=1.00,Integralmax=0.02):
           
    if(self.lin_error ==None):
      preverror=self.euclidean_distance(goal_pose)
    else:
      preverror=self.lin_error
    self.lin_error=self.euclidean_distance(goal_pose)
    Proportional= P * self.lin_error
    if self.lin_Integral<Integralmax:
      self.lin_Integral=self.lin_Integral +I*self.lin_error
    else:
      self.lin_Integral=Integralmax
    Derivative=D*(self.lin_error-preverror)

    Total=Proportional+self.lin_Integral+Derivative

    return Total
   
  def steering_angle(self, goal_pose):
    
    # if(goal_pose.x - self.pose.x>=0):
    #   return atan2(goal_pose.y - self.pose.y, goal_pose.x - self.pose.x)
    # else:
    return  (atan2(goal_pose.y - self.pose.y, goal_pose.x - self.pose.x))

    
   
  def angular_vel(self, goal_pose, P=3.000000,I=0.0003,D=1.0,Integralmax=0.002):
           
    if(self.ang_error ==None):
      preverror=(self.steering_angle(goal_pose) - self.pose.theta)
    else:
      preverror=self.ang_error
    self.ang_error=(self.steering_angle(goal_pose) - self.pose.theta)
    Proportional= P * self.ang_error
    if self.ang_Integral<Integralmax:
      self.ang_Integral=self.ang_Integral +I*self.ang_error
    else:
      self.ang_Integral=Integralmax
    Derivative=D*(self.ang_error-preverror)

    Total=Proportional+self.ang_Integral+Derivative

    return Total
   
  def move2goal(self):
           #"""Moves the turtle to the goal."""
    goal_pose = Pose()
   
           # Get the input from the user.
    goal_pose.x = Listx[w]
    goal_pose.y = Listy[w]
 
         # Please, insert a number slightly greater than 0 (e.g. 0.01).
    #distance_tolerance = float(input("Set your tolerance: "))
    distance_tolerance =0.1
    angle_tolerance=0.005

 
    vel_msg = Twist()

    while abs(self.steering_angle(goal_pose)- self.pose.theta) >= angle_tolerance:

      vel_msg.linear.x = 0
      vel_msg.linear.y = 0
      vel_msg.linear.z = 0
 
             # Angular velocity in the z-axis.
      vel_msg.angular.x = 0
      vel_msg.angular.y = 0
      vel_msg.angular.z = self.angular_vel(goal_pose)

         # Publishing our vel_msg
      self.velocity_publisher.publish(vel_msg)
      
 
             # Publish at the desired rate.
      self.rate.sleep()
 

    # print(1) 
    while self.euclidean_distance(goal_pose) >= distance_tolerance:
 
             # Linear velocity in the x-axis.
      vel_msg.linear.x = self.linear_vel(goal_pose)
      vel_msg.linear.y = 0
      vel_msg.linear.z = 0
 
             # Angular velocity in the z-axis.
      vel_msg.angular.x = 0
      vel_msg.angular.y = 0
      vel_msg.angular.z = 0
 
           # Publishing our vel_msg
      self.velocity_publisher.publish(vel_msg)
      
 
             # Publish at the desired rate.
      self.rate.sleep()
 
         # Stopping our robot after the movement is over.
    vel_msg.linear.x = 0
    vel_msg.angular.z = 0
    self.velocity_publisher.publish(vel_msg)
 
         # If we press control + C, the node will stop.
    #rospy.spin()

w=0
if __name__ == '__main__':
  try:
    for w in range(0,len(Listy)):
      
      x = TurtleBot()
      x.move2goal()
        

  except rospy.ROSInterruptException:
    pass