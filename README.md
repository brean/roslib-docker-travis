# roslib-docker-travis

Run a ROS instance in docker (using **docker-compose**) on travis and connect to it using roslibpy

This basic setup consists of 3 docker container:

- **roscore** the ROS core server.
- **rosnode** a simple ROS node that provides a chatter subscriber and generates something to connect to. has a local ROS installation and connects to *roscore*.
- **test** the external container that does NOT have a local ROS installation. It connects to *roscore* as well and uses that to als subscribe to the rosnode chatter.
