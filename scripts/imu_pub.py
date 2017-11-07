#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from sensor_msgs.msg import Imu
# #from sensor_msgs.import NavSatFix

class publishIMU(object):

	def __init__(self):
		rospy.loginfo("Initialising IMU publishing")
		self.imu_sub=rospy.Subscriber('/IMU_talker_1',String, self.callback, queue_size=1)
		self.imu_sub2=rospy.Subscriber('/IMU_talker_2',String, self.callback2, queue_size=1)
		self.lastMsg=None
		self.lastMsg2 = None
		self.imu_pub=rospy.Publisher('/imu_new', Imu, queue_size=1)
		self.imu_pub2=rospy.Publisher('/imu_new2', Imu, queue_size=1)
		rospy.sleep(3)
		rospy.loginfo("initialised")

	def callback(self, data):
		self.lastMsg=data

	def callback2(self, data):
		self.lastMsg2=data

	def do_work(self):
		self.splitStrings= str(self.lastMsg).split(",")
		self.splitStrings2= str(self.lastMsg2).split(",")
		imumsg= Imu()
		imumsg.header.stamp = rospy.Time.now()
		imumsg.header.frame_id='sensors_link'
		imumsg.orientation.x=float(self.splitStrings[1][2:])
		imumsg.orientation.y=float(self.splitStrings[2][2:])
		imumsg.orientation.z=float(self.splitStrings[3][2:])
		imumsg.orientation.w=float(self.splitStrings[4][2:])

		
		imumsg2= Imu()
		imumsg2.header.stamp = rospy.Time.now()
		imumsg2.header.frame_id='sensors_link'
		imumsg2.orientation.x=float(self.splitStrings2[1][2:])
		imumsg2.orientation.y=float(self.splitStrings2[2][2:])
		imumsg2.orientation.z=float(self.splitStrings2[3][2:])
		imumsg2.orientation.w=float(self.splitStrings2[4][2:])
		rospy.loginfo(self.splitStrings[1])
		self.imu_pub.publish(imumsg)
		self.imu_pub2.publish(imumsg2)

	

	def run(self):
		r=rospy.Rate(10)
		while not rospy.is_shutdown():
			self.do_work()
			r.sleep()

if __name__=='__main__':
	rospy.init_node('pub_imu')
	obj=publishIMU()
	obj.run()
