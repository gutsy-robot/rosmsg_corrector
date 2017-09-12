#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from sensor_msgs.msg import Imu
# #from sensor_msgs.import NavSatFix

class publishIMU(object):

	def __init__(self):
		rospy.loginfo("Initialising IMU publishing")
		self.imu_sub=rospy.Subscriber('/IMU_talker_1',String, self.callback, queue_size=1)
		self.lastMsg=None
		self.imu_pub=rospy.Publisher('/imu_new', Imu, queue_size=1)
		rospy.sleep(8)
		rospy.loginfo("initialised")

	def callback(self, data):
		self.lastMsg=data

	def do_work(self):
		self.splitStrings= str(self.lastMsg).split(",")
		imumsg= Imu()
		imumsg.header.stamp = rospy.Time.now()
		imumsg.header.frame_id='imu'
		imumsg.orientation.x=float(self.splitStrings[1][2:])
		imumsg.orientation.y=float(self.splitStrings[2][2:])
		imumsg.orientation.z=float(self.splitStrings[3][2:])
		imumsg.orientation.w=float(self.splitStrings[4][2:])
		rospy.loginfo(self.splitStrings[1])
		self.imu_pub.publish(imumsg)

	def run(self):
		r=rospy.Rate(1)
		while not rospy.is_shutdown():
			self.do_work()
			r.sleep()

if __name__=='__main__':
	rospy.init_node('pub_imu')
	obj=publishIMU()
	obj.run()
