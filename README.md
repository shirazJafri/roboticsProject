# autonomous-driving-turtlebot-with-reinforcement-learning
Implementation of Q-learning algorithm and Feedback control for the mobile robot (turtlebot3_burger) in ROS.

https://user-images.githubusercontent.com/72970001/98344388-78516600-2013-11eb-9de5-367b9a867d10.jpeg

Content:

    Log_learning -> folder containing data and parameters from the learning phase, as well as the Q-table 
    
    rqt_graphs -> folder containing rqt graphs in ROS

    Control.py -> functions for robot control, Odometry message processing and setting robot's initial position

    Lidar.py -> functions for Lidar message processing and discretization

    Qlearning.py -> functions for Q-learning algorithm

    Plots.py -> plotting the data from learning phase and Q-table

    scan_node.py -> initializing the node for displaying the Lidar measurements and the current state of the agent

    learning_node.py -> initializing the node for learning session

    control_node.py -> initializing the node for applying the Q-learning algorithm combined with Feedback control

To run the code in gazebo simulator, export the model (burger) and roslaunch turtlebot3_world.launch file.

To run the code live on a physical TurtleBot, the ROS_MASTER_URI and ROS_HOSTNAME need to be set via the terminal by editing the ~/.bashrc script.

After setting up the environment, rosrun the desired nodes!

Link to video: https://www.youtube.com/watch?v=zw1BCfku1Dc&t=3s
