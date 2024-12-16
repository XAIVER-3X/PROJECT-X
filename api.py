# -*- coding : utf-8 -*-
# Name   : flask api for hide method
# Author : HADI ANHAF AIMAN
# Create : 15 DECEMBER 2024 11:32PM

import os
import re
import sys
import uuid
import json
import flask
import requests
from flask import Flask,jsonify,request

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def default_screen():
    if request.method == "GET":
        return jsonify({'HEY':'USER'})
    elif request.method == "POST":
        return jsonify({'error':'no data,headers found !'})

@app.route("/auth:<token>",methods=["GET"])
def auth_user(token):
    try:
        original_raw = requests.get("https://www.example.com").text
        if token.upper() in original_raw:
            return jsonify({
                "status":"success",
                "user_verified":True,
                "session_key":str(uuid.uuid4().hex[:40]),
                "access_token":token.upper(),
            }),200
        else:
            return jsonify({
                "status":"failed",
                "user_verified":False,
                "session_key":str(uuid.uuid4().hex[:40]),
                "error":"license not found",
            }),200
    except Exception:
        return jsonify({
            "error":"no internet connection.try again.."
        })

@app.route("/auth",methods=["GET","POST"])
def fb_auth_login():
    # data = request.data
#     headers = request.headers
    if request.method == "GET":
        return jsonify({"{'error':'only post request allowed'}"})
    elif request.method == "POST":
        email = data.get("email")
        password = data.get("password")
        auth_tok = headers.get("access_token")
        ugen_fba = headers.get("Uger-Agent")
        try:
            datas = None
            headers = None
            url = None
            requ = requests.post(url).json()
            if "access_token" in requ:
                return jsonify({
                    "status":"success",
                    "uid":str(requ["uid"]) if str(requ["uid"]) else email,
                    "pas":password,
                    "coki":cokies,
                })
            elif "www.facebook.com" in requ["error"]["message"]:
                return jsonify({
                    "status":"checkpoint",
                })
            else:pass
        except:pass


if __name__ == "__main__":
    app.run(debug=True)
