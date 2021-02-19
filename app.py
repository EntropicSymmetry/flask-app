# -*- coding: utf-8 -*-
# encoding=utf8

#Import required libs
import numpy as np 
from flask import Flask
from flask import  request, redirect, url_for, flash, jsonify, Response, make_response
from flask_cors import CORS, cross_origin
from datetime import datetime
import json, pymongo

#Define app
app = Flask(__name__)

#Add CORS
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

client = pymongo()

#Creat app route for training datasheets
@app.route('/auth', methods=['POST'])
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
@app.route('/chat', methods=['POST'])
@cross_origin()

def getMessage():
	data = request.get_json()

	import requests
	from requests.structures import CaseInsensitiveDict
	import json
	from rasaxutils import getTest, getFirstQuestion, getQuestions

	senderID = data['sender']+str(datetime.today().strftime('%Y-%m-%d')).replace("-","")

	url = "http://stella.unitedwecare.ca/api/conversations/"+senderID+"/messages?environment=production"
	#url = "http://stella.unitedwecare.ca/api/chat"

	headers = CaseInsensitiveDict()
	headers["Authorization"] = "Bearer "+data['bearer_token']
	headers["Content-Type"] = "application/json"

	send_data = {"message":data['responses'][-1]}

	try:
		resp_text = requests.post(url, headers=headers, data=json.dumps(send_data))
		resp_to_return = resp_text.json()[0]
		print(resp_to_return)
		resp_to_return['type'] = 'message'
		resp_to_return['buttons'] = []
	except Exception as e:
		pass

	metadata_url = "http://stella.unitedwecare.ca/api/conversations/"+senderID+"?format=full_conversation&since=1611116400.9448216&environment=production"

	if bool(data['questions']) == True:
		if data['questions'][-1] in getQuestions('PHQuestions') or data['questions'][-1] in getQuestions('RelationshipQuestions')  or data['questions'][-1] in getQuestions('Y-BOC') or  data['questions'][-1] in getQuestions('PHQ-15'):
			
			if data['questions'][-1] in getQuestions('RelationshipQuestions'):
				resp_to_return = getTest(data['questions'], data['responses'], "RelationshipQuestions")
				resp_to_return['sender'] = data['sender']
				return resp_to_return

			elif data['questions'][-1] in getQuestions('PHQuestions'):
				resp_to_return = getTest(data['questions'], data['responses'], "PHQuestions")
				resp_to_return['sender'] = data['sender']
				return resp_to_return

			elif data['questions'][-1] in getQuestions('PHQ-15'):
				resp_to_return = getTest(data['questions'], data['responses'], "PHQ-15")
				resp_to_return['sender'] = data['sender']
				return resp_to_return

			elif data['questions'][-1] in getQuestions('Y-BOC'):
				resp_to_return = getTest(data['questions'], data['responses'], "Y-BOC")
				resp_to_return['sender'] = data['sender']
				return resp_to_return

			elif data['questions'][-1] in getQuestions('GAD-7'):
				resp_to_return = getTest(data['questions'], data['responses'], "GAD-7")
				resp_to_return['sender'] = data['sender']
				return resp_to_return

			elif data['questions'][-1] in getQuestions('Socrates'):
				resp_to_return = getTest(data['questions'], data['responses'], "Socrates")
				resp_to_return['sender'] = data['sender']
				return resp_to_return

			elif data['questions'][-1] in getQuestions('PSS'):
				resp_to_return = getTest(data['questions'], data['responses'], "PSS")
				resp_to_return['sender'] = data['sender']
				return resp_to_return

			elif data['questions'][-1] in getQuestions('SPIN'):
				resp_to_return = getTest(data['questions'], data['responses'], "SPIN")
				resp_to_return['sender'] = data['sender']
				return resp_to_return

	resp_metadata = requests.get(metadata_url, headers=headers)

	print(resp_metadata.json())

	if bool(resp_metadata.json()['latest_message']['intent'])==True:
		
		#Store in mongo
		client.Stella.KeyWords.update_one({"_id":sender_id}, {"$push":{"intentList":resp_metadata.json()['latest_message']['intent']})
		
		myIntent = resp_metadata.json()['latest_message']['intent']['name']
		if myIntent == 'Gen_Depression':
			resp_to_return = getFirstQuestion('PHQuestions')
			resp_to_return['sender'] = data['sender']

		if myIntent == 'Gen_RelationshipIssues':
			resp_to_return = getFirstQuestion('RelationshipQuestions')
			resp_to_return['sender'] = data['sender']

		if myIntent == 'gen_OCD':
			resp_to_return = getFirstQuestion('Y-BOC')
			resp_to_return['sender'] = data['sender']

		if myIntent == 'gen_StressBody':
			resp_to_return = getFirstQuestion('PHQ-15')
			resp_to_return['sender'] = data['sender']

		if myIntent == 'gen_Anxious':
			resp_to_return = getFirstQuestion('GAD-7')
			resp_to_return['sender'] = data['sender']

		if myIntent == 'gen_Addiction':
			resp_to_return = getFirstQuestion('Socrates')
			resp_to_return['sender'] = data['sender']

		if myIntent == 'gen_StressMind':
			resp_to_return = getFirstQuestion('PSS')
			resp_to_return['sender'] = data['sender']

		if myIntent == 'gen_StressMind':
			resp_to_return = getFirstQuestion('PSS')
			resp_to_return['sender'] = data['sender']

	print(resp_text.status_code)

	return resp_to_return


if __name__ == '__main__':
	app.run(debug=False, threaded=True)
