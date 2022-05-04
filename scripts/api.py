from flask import Flask,request, jsonify
import requests
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
app.config['DEBUG'] = True
def setJson(inp):
    global json
    json = inp
    print("In set json",json)
# def setReward(inp):
#     global reward
#     reward = inp
#     print("In set json",reward)
json = ""
# reward = ""
@app.route("/",methods=["POST", "GET", "OPTIONS"])
def hello_world():
    if request.method == "POST":
        print(request.form.keys()[0])
        setJson(request.form.keys()[0])
        print(json)
        return "runnning"
    if request.method == "GET":
        if json is not "":
            js = json
            print(json)
            setJson("")
            return js

        else:
            return "-1"
# @app.route("/get",methods=["POST", "GET", "OPTIONS"])
# def getReward():
#     if request.method == "POST":
#         print("Request Data:",request.json['reward'])
#         setReward(request.json['reward'])
#         # setJson(request.form.keys()[0])
#         # print(json)
#         return "runnning"
#     if request.method == "GET":
#         if reward is not "":
#             js = reward
#             print(reward)
#             setReward("")
#             return js

#         else:
#             return "-1"
if __name__ == "__main__":
    app.run()