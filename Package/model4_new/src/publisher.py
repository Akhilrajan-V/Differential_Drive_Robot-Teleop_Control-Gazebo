#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64
 
def talker():
     #pub_steer = rospy.Publisher('/turn', Float64, queue_size=10) 
     pub_move = rospy.Publisher('/speed', Float64, queue_size=10)
     
     rospy.init_node('talker', anonymous=True)
     rate = rospy.Rate(1) # 1hz
     while not rospy.is_shutdown():
         #control_turn = 30*3.14/180
         control_speed = 20
         print('Speed: ', control_speed)
         #print('Turn angle: ', control_turn)
         #pub_steer.publish(control_turn)
         pub_move.publish(control_speed)
         rate.sleep()
 
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
