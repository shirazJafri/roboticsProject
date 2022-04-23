# Setup

1. roslaunch rosbridge_server rosbridge_websocket.launch
2. roscd to turtlebot3_gazebo/launch/turtlebot3_stage_1.launch file and update your launch file accordingly.
3. https://github.com/oKermorgant/calibration_gazebo/blob/master/sdf/perspective.sdf. Add this file(perspective.sdf) to turtlebot3_gazebo/models folder.
4. python3 server.py from the project's root directory.
