#!/usr/bin/env python

import rospy
from nav_msgs.msg import Odometry


class FrameRepair(object):
	def __init__(self):

		rospy.loginfo("Initialising objects for tf frame repair for vo..")
		self.vo_sub = rospy.Subscriber('/zed/odom', Odometry, self.odom_cb, queue_size=1)
		self.last_odom = None
		self.vo_pub = rospy.Publisher('/vo_new', Odometry, queue_size=1)
		rospy.sleep(2)
		rospy.loginfo("objects initialised for tf repair....")
		rospy.loginfo("repair tf started..")



	def odom_cb(self, data):
		self.last_odom = data

	def do_work(self):
		self.last_odom.header.frame_id = "zed_initial_frame"
		self.vo_pub.publish(self.last_odom)

	def run(self):
		r = rospy.Rate(10)
		while not rospy.is_shutdown():
			self.do_work()
			r.sleep()


if __name__ == '__main__':
	rospy.init_node('frame_repairer')
	obj = FrameRepair()
	obj.run()


