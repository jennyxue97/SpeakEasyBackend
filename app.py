from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os
import users, speech

app = Flask(__name__)
CORS(app)

#============== USER ================#
@app.route("/post_user", methods=["POST"])
def route_post_user():
    user_name = request.form["user_name"]
    return jsonify(users.post_user(user_name))

@app.route("/get_user", methods=["GET"])
def route_get_user():
    user_name = request.args["user_name"]
    return jsonify(users.get_user(user_name))


#=============== SPEECH ================#
@app.route("/post_speech", methods=["POST"])
def route_post_speech():
    """
    user_name: str
    speech_name: str
    """
    category = request.form["category"]
    return jsonify(speech.post_speech(request.form, category))
    
@app.route("/get_speech_details", methods=["GET"])
def route_get_speech_details():
    user_name = request.args["user_name"]
    speech_name = request.args["speech_name"]
    category = request.args["category"]
    return jsonify(speech.get_speech_details(speech_name, user_name, category))

@app.route("/get_all_speeches", methods=["GET"])
def route_get_all_speeches():
    user_name = request.args["user_name"]
    return jsonify(speech.get_all_speeches(user_name))

if __name__ == "__main__":
    app.run(port=5000)