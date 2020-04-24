# roslib-docker-travis

Run a ROS instance in docker (using **docker-compose**) on travis and connect to it using roslibpy

This basic setup consists of 5 docker container:

- **roscore** the ROS core server.
- **listener** a simple ROS node that provides a the hello world subscriber, it has a local ROS installation and connects to *roscore*.
- **talker** a simple ROS node that provides a the hello world publisher, it has a local ROS installation and connects to *roscore*.
- **rosbridge** a simple ROS node also running on the ROS installation from the listener/talker example that allows us to connect to our roscore using the rosbridge.
- **roslib** the external container that does NOT have a local ROS installation but the minimal default python 3.7. It connects to *roscore* as well but through the rosbridge, also listens to the chatter of the talker.
