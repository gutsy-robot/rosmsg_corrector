#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from sensor_msgs.msg import NavSatFix

class publishGPS(object):

	def __init__(self):
		rospy.loginfo("Initialising GPS publishing")
		self.gps_sub=rospy.Subscriber('/GPS_talker_1',String, self.callback, queue_size=1)
		self.lastMsg=None
		self.gps_pub=rospy.Publisher('/gps_new', NavSatFix, queue_size=1)
		rospy.sleep(5)
		rospy.loginfo("initialised")

	def callback(self, data):
		self.lastMsg=data

	def do_work(self):
		self.splitStrings= str(self.lastMsg).split(",")
		gpsmsg=NavSatFix()
		gpsmsg.header.stamp = rospy.Time.now()
		gpsmsg.header.frame_id = "sensors_link"
		#rospy.loginfo(self.splitStrings[1])
		gpsmsg.latitude=float(self.splitStrings[1][4:])
		gpsmsg.longitude=float(self.splitStrings[2][5:-5])
		self.gps_pub.publish(gpsmsg)

	def run(self):
		r=rospy.Rate(1)
		while not rospy.is_shutdown():
			self.do_work()
			r.sleep()

if __name__=='__main__':
	rospy.init_node('pubgps')
	obj=publishGPS()
	obj.run()
