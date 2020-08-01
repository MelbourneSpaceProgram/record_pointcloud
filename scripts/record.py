#!/usr/bin/env python
import rospy
from sensor_msgs.msg import PointCloud2
import sensor_msgs.point_cloud2 as pc2
import numpy as np
import os
import process_pointcloud

msgs = []

def callback(data):
    data = pc2.read_points(data, field_names=['x', 'y', 'z', 'rgb'], skip_nans=True)
    unpacked_data = np.asarray(list(data))
    msgs.append(unpacked_data)
    print(unpacked_data)
    
def listener():
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("/camera/depth/points", PointCloud2, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

    np.save(os.path.join("data", "gazebo_pointcloud"), np.stack(msgs))
    process_pointcloud.main()

if __name__ == '__main__':
    listener()