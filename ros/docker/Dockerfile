ARG ROS_DISTRO
FROM ros:${ROS_DISTRO}
# Install rosbridge
RUN apt-get update && apt-get install -y \
    ros-${ROS_DISTRO}-rosbridge-suite \
    ros-${ROS_DISTRO}-rosbridge-server \
    ros-${ROS_DISTRO}-ros-tutorials \
    python-pip python-twisted python-openssl \
    python-autobahn python-tornado \
    python-bson \
    cmake iputils-ping \
    --no-install-recommends \
    # Clear apt-cache to reduce image size
    && rm -rf /var/lib/apt/lists/*

RUN pip install -U wheel
RUN pip install -U catkin_tools service_identity

# Copy entrypoint
COPY ./ros_entrypoint.sh /

SHELL [ "bash", "-c" ]

RUN source /opt/ros/$ROS_DISTRO/setup.bash
RUN mkdir -p /opt/catkin_ws/src
RUN cd /opt/catkin_ws && catkin init

# for roslib
EXPOSE 9090

ENTRYPOINT ["/ros_entrypoint.sh"]
CMD ["/bin/bash"]
