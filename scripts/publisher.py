#!/usr/bin/env python3
# license removed for brevity
from sys import stdout
import rospy
from std_msgs.msg import String
import subprocess

def talker():
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    # speed of message e.g 1 is 1 message per second
    rate = rospy.Rate(0.1)
    while not rospy.is_shutdown():
        p1 = subprocess.check_output(['git remote show origin'], shell=True).decode('utf-8')
        pub.publish(p1)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass