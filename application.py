# -*- coding: utf-8 -*-
# encoding=utf8

#Import required libs
import numpy as np 
from flask import Flask
from flask import  request, redirect, url_for, flash, jsonify, Response, make_response
from flask_cors import CORS, cross_origin

#Define app
application = Flask(__name__)

#Add CORS
cors = CORS(application)
application.config['CORS_HEADERS'] = 'Content-Type'

#Creat app route for training datasheets
@application.route('/auth', methods=['POST'])
@cross_origin()

def getAuth():
	data = request
	import requests
	from requests.structures import CaseInsensitiveDict

	url = "http://stella.unitedwecare.ca/api/auth"

	headers = CaseInsensitiveDict()
	headers["Content-Type"] = "application/json"

	data = """
	{"username":"me", 
	 "password":"Qga8xYmayKYALlWUNVwC"}
	"""


	resp = requests.post(url, headers=headers, data=data)

	print(resp.status_code)
	return resp.text

#Creat app route for training datasheets
@application.route('/chat', methods=['POST'])
@cross_origin()

def getMessage():
	data = request.get_json()

	import requests
	from requests.structures import CaseInsensitiveDict
	import json

	url = "http://stella.unitedwecare.ca/api/chat"

	headers = CaseInsensitiveDict()
	headers["Authorization"] = "Bearer "+data['bearer_token']
	headers["Content-Type"] = "application/json"

	data = json.dumps({"sender":data['sender'],"message":data['message']})


	resp = requests.post(url, headers=headers, data=data)

	print(resp.status_code)
	return resp.text

#Creat app route for training datasheets
@application.route('/ph9test', methods=['POST'])
@cross_origin()

def getTest():
	data = request.get_json()

	import requests
	from requests.structures import CaseInsensitiveDict
	import json
	questions = [
	"Little interest or pleasure in doing things?",
	"Feeling down, depressed, or hopeless?",
	"Trouble falling or staying asleep, or sleeping too much?",
	"Feeling tired or having little energy?",
	"Poor appetite or overeating?",
	"Feeling bad about yourself - or that you are a failure or have let yourself or your family down?",
	"Trouble concentrating on things, such as reading the newspaper or watching television?",
	"Moving or speaking so slowly that other people could have noticed? Or the opposite - being so fidgety or restless that you have been moving around a lot more than usual?",
	"Thoughts that you would be better off dead, or of hurting yourself in some way?"
	]

	answers = [
	"Not at all",
	"Several days",
	"More than half the days",
	"Nearly every day"
	]

	outcomes = ["none", "mild","moderate","moderately severe", "severe"]
	questNum = 0
	sumTotal = 0
	if data['message'] in questions[-1:]:
		questionIndex = questions.index(data['message'])
		possibleAnswers = outcomes

	else:
		for l in data['response']:
			sumTotal = sumTotal +answers.index(response)
		depSeverity = outcomes[(-27//sumTotal)]
		return {'question':'None', 'buttons':'None', 'score':depSeverity}

	return jsonify({'question':questions[questionIndex+1], 'buttons':possibleAnswers})


if __name__ == '__main__':
	application.run(debug=False, threaded=True)
