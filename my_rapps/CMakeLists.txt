cmake_minimum_required(VERSION 2.8.3)
project(my_rapps)

find_package(catkin REQUIRED geometry_msgs sensor_msgs rocon_apps)

catkin_python_setup()

catkin_package()

#############
## Install ##
#############

