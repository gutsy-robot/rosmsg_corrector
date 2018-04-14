# rosmsg_corrector
Package for creating usable rosmsgs for ROS localization from the data sent from the sensors.

This package includes scripts for parsing the data stream being received from the sensors present on the car, which include a GPS sensor and an IMU.
The bags directory contains rosbags on which these scripts can be tested. To run all of these scripts together, just do a
  
    roslaunch all_correctors.launch
