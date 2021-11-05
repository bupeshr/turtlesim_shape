# turtlesim_shape
Different shapes using turtlesim

OS: Ubuntu 20.04 LTS
Distro: Noetic
Python3

To play with Turtlesim

Start the roscore:

$ roscore

To install and start the turtlesim in noetic:

$ sudo apt-get install ros-noetic-turtlesim

Run turtlesim:

$ rosrun turtlesim turtlesim_node

Create a pkg for running launch files and scripts

$cd ~/catkin_ws/src
$catkin_create_pkg <pkg name> rospy roscpp std_msgs
$cd ~/catkin_ws/
$source devel/setup.bash
  
Rosrun turtle nodes

$rosrun <pkg name> <node.py>
  
Experiment with different shapes
  
Happy turtle play!!
  

  
