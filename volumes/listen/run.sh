#!/bin/bash
source "/opt/catkin_ws/devel/setup.bash"
cd /opt/catkin_ws && catkin build
source "/opt/catkin_ws/devel/setup.bash"
cd /opt/catkin_ws/src/listen && roslaunch listen start.launch