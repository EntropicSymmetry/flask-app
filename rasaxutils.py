def getTest(message, response):
	data = {}
	data['questions'] = message
	data['response'] = response

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
	def getFirstQuestion():
		return {'text':questions[0], 'buttons':answers, 'type':"PHQuestions"}
	def getQuestions():
		return questions

	answers = [
	"Not at all",
	"Several days",
	"More than half the days",
	"Nearly every day"
	]

	outcomes = ["none", "mild","moderate","moderately severe", "severe"]
	questNum = 0
	sumTotal = 0
	if data['questions'][-1] in questions[-1:]:
		questionIndex = questions.index(data['message'])
		possibleAnswers = outcomes

	else:
		for l in data['response']:
			try:
				sumTotal = sumTotal +answers.index(response)
			except Exception as e:
				pass
		depSeverity = outcomes[(-27//sumTotal)]
		return {'question':'None', 'buttons':'None', 'score':depSeverity}

	return jsonify({'text':questions[questionIndex+1], 'buttons':possibleAnswers, 'type':'PHQuestions'})
