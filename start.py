from time import sleep
from flask import Flask
from check_turtlebot import check_turtlebot
import subprocess
app = Flask(__name__)

@app.route('/')
def starting_up():
    proc = subprocess.Popen(['roslaunch', 'turtlebot3_gazebo', 
    'turtlebot3_stage_1.launch'], stdout=subprocess.DEVNULL, stderr= subprocess.DEVNULL)


    if check_turtlebot():
        return 'TurtleBot sucessfully run!'

    
        
    return 'TurtleBot run unsucessfull!'

@app.route('/move')
def move_bot():
    return "Moving bot"
app.run(debug= True)