#!/usr/bin/env python3
# license removed for brevity
import rospy
#import git
from std_msgs.msg import String

# def git_push_change(path):
#    repo = git.Repo(path)
#    current = repo.head.commit
#    repo.remotes.origin.push()

def talker():
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        strg_msg = "test"
        pub.publish(strg_msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass