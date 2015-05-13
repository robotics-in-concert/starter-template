cmake_minimum_required(VERSION 2.8.3)
project(my_robot_launcher)

####################################################
# Catkin
####################################################
find_package(catkin REQUIRED COMPONENTS
  rocon_app_manager
  rocon_apps
)

catkin_package()

####################################################
# Installs
####################################################

#install(DIRECTORY launch 
#  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
#)
