#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64

def callback1(data):
    rospy.loginfo("Speed = %s", data.data)
    pub_move1 = rospy.Publisher('/model4_new/drive_wheel1_controller/command', Float64, queue_size=10)
    pub_move2 = rospy.Publisher('/model4_new/drive_wheel2_controller/command', Float64, queue_size=10)
    pub_move3 = rospy.Publisher('/model4_new/drive_wheel3_controller/command', Float64, queue_size=10)
    pub_move4 = rospy.Publisher('/model4_new/drive_wheel4_controller/command', Float64, queue_size=10)
    pub_move1.publish(-data.data)
    pub_move2.publish(data.data)
    pub_move3.publish(-data.data)
    pub_move4.publish(data.data)

#def callback2(data):
    #rospy.loginfo("Turn angle = %s", data.data)
    #pub_steer = rospy.Publisher('/model4_new/steering_controller/command', Float64, queue_size=10)
    #pub_steer.publish(data.data)
    
def listener():

    rospy.init_node('listener')

    rospy.Subscriber("/speed", Float64, callback1)
    #rospy.Subscriber("/turn", Float64, callback2)
    
    rospy.spin()

 
if __name__ == '__main__':
    listener()
    
