#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist

def first():
	pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=15)
	rospy.init_node('n1', anonymous=False)
	rate= rospy.Rate(1)
	vel = Twist()

	
	rate.sleep()
	#this part is for the different motion , so this code snip id for triangle
	for i in range(3):
		vel.linear.x=4
		vel.angular.y=0
		vel.angular.z=0
		pub.publish(vel)
		print('munnadi poren da!')
		rate.sleep()


		vel.linear.x=0
		vel.angular.z=2.11



		first_det="Sendingc Node1"
		print('valayren da!')
		pub.publish(vel)
		rate.sleep()

if __name__ == '__main__':
	first()