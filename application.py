# -*- coding: utf-8 -*-
# encoding=utf8

#Import required libs
import numpy as np 
from flask import Flask
from flask import  request, redirect, url_for, flash, jsonify, Response, make_response
from flask_cors import CORS, cross_origin
from datetime import datetime
import json

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

	data = json.dumps(
	{"username":"me", 
	 "password":"Qga8xYmayKYALlWUNVwC"})



	resp = requests.post(url, headers=headers, data=data)

	print(resp.status_code)
	return resp.text

#Creat app route for chatting with bot
@application.route('/chat', methods=['POST'])
@cross_origin()

def getMessage():
	data = request.get_json()

	import requests
	from requests.structures import CaseInsensitiveDict
	import json
	from rasaxutils import getTest

	senderID = data['sender']+str(datetime.today().strftime('%Y-%m-%d')).replace("-","")

	url = "http://stella.unitedwecare.ca/api/conversations/"+senderID+"/messages?environment=production"
	#url = "http://stella.unitedwecare.ca/api/chat"

	headers = CaseInsensitiveDict()
	headers["Authorization"] = "Bearer "+data['bearer_token']
	headers["Content-Type"] = "application/json"

	send_data = {"message":data['responses'][-1]}


	resp_text = requests.post(url, headers=headers, data=json.dumps(send_data))
	resp_to_return = resp_text.json()[0]
	print(resp_to_return)
	resp_to_return['type'] = 'message'
	resp_to_return['buttons'] = []

	metadata_url = "http://stella.unitedwecare.ca/api/conversations/"+"me"+"?format=full_conversation&since=1611116400.9448216&environment=production"

	if bool(data['questions']) == True:
		if data['questions'][-1] in getTest.getQuestions():
			resp_to_return = getTest(data['questions'], data['responses'])
			resp_to_return['sender'] = data['sender']
			return resp_to_return

	resp_metadata = requests.get(metadata_url, headers=headers)

	print(resp_metadata.json())
	if bool(resp_metadata.json()['latest_message']['intent'])==True:
		myIntent = resp_metadata.json()['latest_message']['intent']['name']
		if myIntent == 'utter_DepressionOne':
			resp_to_return = getTest.getFirstQuestion()
			resp_to_return['sender'] = data['sender']

	print(resp_text.status_code)

	return resp_to_return


if __name__ == '__main__':
	application.run(debug=False, threaded=True)
