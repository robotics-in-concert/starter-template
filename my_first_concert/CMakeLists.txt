cmake_minimum_required(VERSION 2.8.3)
project(my_first_concert)


####################################################
# Catkin
####################################################

find_package(catkin REQUIRED COMPONENTS
  concert_master
  concert_service_admin
  concert_service_teleop
)

catkin_package()

####################################################
# Installs
####################################################

install(DIRECTORY solutions
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)
