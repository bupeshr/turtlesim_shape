#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist

def rectangle():
	pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=15)
	rospy.init_node('rectangle_node', anonymous=False)
	rate= rospy.Rate(1)
	vel = Twist()

	
	rate.sleep()
	#this part is for the different motion , so this code snip id for triangle
	for i in range(2):
		#forward action
		vel.linear.x=5
		vel.angular.y=0
		vel.angular.z=0
		pub.publish(vel)
		print('munnadi poren da!')
		rate.sleep()

		#turn/angular action
		vel.linear.x=0
		vel.angular.z=1.59
		print('valayren da!')
		pub.publish(vel)
		rate.sleep()

		#upward/downward action
		vel.linear.x=2
		vel.angular.z=0
		pub.publish(vel)
		print('mela/keela poren da!')
		rate.sleep()

		#turn/angular action
		vel.linear.x=0
		vel.angular.z=1.58
		print('valayren da!')
		pub.publish(vel)
		rate.sleep()

if __name__ == '__main__':
	rectangle()