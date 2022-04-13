from time import sleep
from flask import Flask
from check_turtlebot import check_turtlebot
import subprocess
app = Flask(__name__)

@app.route('/')
def starting_up():

    # proc_0 = subprocess.Popen(['export', 'TURTLEBOT3_MODEL=waffle'])

    proc = subprocess.Popen(['roslaunch', 'turtlebot3_gazebo', 
    'turtlebot3_stage_1.launch']) 
    
    # stdout=subprocess.DEVNULL, stderr= subprocess.DEVNULL)
    print(proc)

    # if check_turtlebot():
    #     return 'TurtleBot sucessfully run!'
        
    return 'TurtleBot run unsucessfull!'

app.run(debug= True)