#!/usr/bin/env python

import os
import rospy
import cv_bridge
import cv2
import sensor_msgs.msg as sensor_msgs
import geometry_msgs.msg as geometry_msgs

class DummyTeleop(object):
    '''
        Dummy Teleoperation Implementation which simulates video stream from robot, and litens to Twist msg
        Please refer turtlebot_rapps/video_teleop for real implementation example
    '''

    def __init__(self):
        self._pub_video = rospy.Publisher('compressed_image',sensor_msgs.CompressedImage, latch=True)
        self._sub_cmd_vel = rospy.Subscriber('cmd_vel', geometry_msgs.Twist, self._process_cmd_vel)

        image_src = os.path.join(os.path.dirname(__file__), 'chimek.jpg')
        self._image = self._load_image_as_compressed(image_src)

    def _load_image_as_compressed(self, src):

        msg = sensor_msgs.CompressedImage()
        msg.header.stamp = rospy.Time.now()
        msg.format = "jpeg"

        # Data itself is already compressed format 
        msg.data = open(src, "rb").read()
        return msg

    def _process_cmd_vel(self, msg):
        self.loginfo(str(msg))

    def spin(self):
        self._pub_video.publish(self._image)
        rospy.spin()

    def loginfo(self, msg):
        rospy.loginfo("%s : %s"%(rospy.get_name(), msg))

if __name__ == '__main__':

    rospy.init_node('dummy_video_teleop')

    dum = DummyTeleop() 
    dum.loginfo("Initalised")
    dum.spin()
    dum.loginfo("Bye Bye")
