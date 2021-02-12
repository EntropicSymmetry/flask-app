def getTest(message, response, questionaire):
	data = {}
	data['questions'] = message
	data['response'] = response

	import json

	if questionaire == 'PHQuestions':
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

	elif questionaire == 'RelationshipQuestions':
		questions = ["How well does your partner meet your needs?","In general, how satisfied are you with your relationship?",
		"How good s your relationship compared to most?","How often do you wish you hadn't gotten into this relationship?",
		"To what extent has your relationship met your original expectations?","How much do you love your partner?","How many problems are there in your relationship?"]
		answers = ["Low", "Average","High"]
		outcomes = ["Low Satisfaction", "High Satisfaction"]

	elif questionaire == 'PHQ-15':
		questions = ['Over the last week, how often have you been bothered by stomach pain?', 'Over the last week, how often have you been bothered by back pain?', 'Over the laast week, how often have you been bothered by pain in you arms, legs or joints (knees, hips, etc.)?', 'Over the last week, how often have you been bothered by menstural cramps or other problems with your periods?', 'Over the last week, how often have you been bothered by headaches?', 'Over the last week, how often have you been bothered by dizziness?', 'Over the last week, how often have you been bothered by feeling your heart pound or race?', 'Over the last week, how often have you been bothered by shortness or breath?', 'Over the last week, how often have you been bothered by pain or problems during sexual intercourse?', 'Over the alst week, how often have you been bthered by constipation, loos bowels or diarrhea?', 'Over the last week, how often have you been bothered by nausea, gas or indigestion?', 'Over the last week, how often have you been bothered by feeling tired or having low energy?', 'Over the last week, how often have you been bothered by trouble sleeping?', 'Over the last week, how often have you been bothered by chest pain?', 'Over the last week, how often have you been bothered by fainting spells?']
		answers = ["Not at all","Bothered a little","Bothered a lot"]
		outcomes = ["Low", "Medium", "High Somatic Symptom Severity"]

	elif questionaire == "Y-BOC":
		questions = ['how much of your time is occupied by obsessive thoughts?', "How much do your obsessive thoughts interfere with your work, school, social or other important role functioning? Is there anything that you don't do because of them?", 'How much distress do your obsessive thoughts cause you?', 'How much of an effort do you make to resist the obsessive thoughts? How often fo you try to disregard or turn your attention away from these thoughts as they enter your mind?', 'How much control do you have over your obsessive thoughts? How sucessful are you in stopping or diverting your obsessive thinking? Can you dismiss them?', 'How much time do you spend performing compulsive behaviors? How much long than most people does it take to complete routine activity because of your rituals? How frequently do you do rituals?', 'How much do your compulsive behaviors interfere with your work, school, social or other important role functioning? Is there anything your don;t do because of the compulsions?', 'How would you feel if prevented from prforming your compulsion (s)? how anxious would you become?', 'how much of an effort do you make to resist the compulsions?', 'How strong is the drive to perform the compulsive behavior? How much control do you have over the compulsions?']
		answers = answers = [
		"Not at all/minimal",
		"Observable time and interference",
		"Several times and causes high interference in day-to-day life",
		"Taking a high toll on life and compulsive"
		]
		outcomes = ["Mild", "Moderate", "Severe", "Extreme"]

	elif questionaire == 'GAD-7':
		questions = ['Over the last 2 weeks', ' how often have you been bothered by any of the following problems?', 'Feeling nervous', ' anxious or on edge?', 'Not being able to stop or control worrying?', 'Worrying too much about different things?', 'Trouble relaxing?', 'Being so restless that it si hard to sit still?', 'Becoming easily annoyed or irritable?', 'Feeling afraid as if something awful might happen?']
		answers = ['Not at all', 'Some days', 'Most days', "Almost every day"]
		outcomes= ["Mild", "Moderate", "Severe"]

	elif questionaire = 'Socrates':
		questions	=	['I really want to make changes in my drinking.', 'Sometimes I wonder if I am an alcoholic.', "If I don't change my drinking soon, my problems are going to get worse/", 'I have already started making some changes in my drinking.', "I was drinking too much at one time, but I've managed to change my drinking.", 'Sometimes I wonder if my drinking is hurting other people.', 'I am a problem drinker.', "I'm not just thinking about changing my drinking, I'm already doing something about it.", 'I have already changed my drinking, and I am looking for ways to keep from slipping back to my old pattern.', 'I have serious problems with drinking.', 'Sometimes I wonder if I am in control of my drinking.', 'My drinking is cauasing a lot of harm.', 'I am actively doing things now to cut down or stop drinking.', 'I want help to keep from going back to the drinking problems that I had before.', 'I know that I have a drinking problem.', 'There are times when I wonder if I drink too much.', 'I am an alcoholic.', 'I am working hard to change my drinking.', 'I have made some changes in my drinking, and I want some help to keep from going back to the way I used to drink.']
		answers = ["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"]
		outcomes = []

	elif questionaire == 'PSS':
		questions = ['In the last month, how often have you been upset because of something that happened unexpectedly?', 'In the last month, how often have you felt that you were unable to control the important things in your life?', 'In the last month, how often have you felt nervous and “stressed”?', 'In the last month, how often have you felt confident about your ability to handle your personal problems?', 'In the last month, how often have you felt that things were going your way?', 'In the last month, how often have you found that you could not cope with all the things that you had to do?', 'In the last month, how often have you been able to control irritations in your life?', 'In the last month, how often have you felt that you were on top of things?', 'In the last month, how often have you been angered because of things that were outside of your control?', 'In the last month, how often have you felt difficulties were piling up so high that you could not overcome them?.']
		answers = ["Never", "Almost never", "Sometimes", "Fairly often", "Very often"]
		outcomes = ["Low stress", "Moderate stress", "High stress"]

	elif questionaire = 'SPIN':
		questions = ['I am afraid of people in authority', 'I am bothered by blushing in front of people', 'Parties and social events scare me', "I avoid talking to people i don't know", 'Being criticized scares me a lot.', 'I avoid doing things or speaking to people for fear of embarrassment', 'Sweating in front of people causes me distress', 'I avoid going to parties', 'I avoid activities in which i am the center of attention', 'Talking to strangers scares me', 'I avoid having to gve speeches', 'I would do anything to avoid being criticized', 'Heart palpitations bother me when i am aroudn people', 'I am afraid of doing things when people might be watching', 'Being embarrassed of looking stupid are among my worst fears', 'I avoid speaking to anyone in authority', 'Trembling or shaking in front of others is distressing to me']
		answers = ["Not at all", "A little bit", "Somewhat", "Very much", "Extremely"]
		outcomes = []


	questNum = 0
	sumTotal = 0
	if data['questions'][-1] in questions:
		questionIndex = questions.index(data['questions'][-1])
		possibleAnswers = answers
		if data['questions'][-1]  == questions[-1]:
			count = 0
			for l in range(len(data['questions'])):
				if data['questions'][l] == questions[0]:
					count = 1
				if count == 1:
					try:
						sumTotal = sumTotal +answers.index(data['response'][l])+1
					except Exception as e:
						pass
			if questionaire == 'PHQuestions':
				depSeverity = outcomes[-(27//sumTotal)]
			if questionaire == 'RelationshipQuestions':
				depSeverity = outcomes[int(sumTotal/11)]
			if questionaire == 'PHQ-15':
				depSeverity = outcomes[round(sumTotal/5,0)]
			if questionaire == 'Y-BOC':
				depSeverity = outcomes[round(sumTotal/2.5-0.5,0)]
			if questionaire == 'GAD-7':
				depSeverity = outcomes[round(sumTotal/3.333,0)]
			if questionaire == 'Socrates':
				depSeverity = int(sumTotal/10)
			if questionaire == 'PSS':
				depSeverity = outcomes[round(sumTotal/3.333,0)]
			if questionaire == 'SPIN':
				depSeverity = int(sumTotal/3.4)*5


			return {'question':[], 'buttons':[], 'score':depSeverity}

	return {'text':questions[questionIndex+1], 'buttons':possibleAnswers, 'type':questionaire}

def getFirstQuestion(typeOf):
	questionaire = typeOf
	if typeOf== 'PHQuestions':
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

	elif typeOf == 'RelationshipQuestions':
		questions = ["How well does your partner meet your needs?","In general, how satisfied are you with your relationship?",
		"How good s your relationship compared to most?","How often do you wish you hadn't gotten into this relationship?",
		"To what extent has your relationship met your original expectations?","How much do you love your partner?","How many problems are there in your relationship?"]
		answers = ["Low", "Average","High"]
		outcomes = ["Low Satisfaction", "High Satisfaction"]

	elif questionaire == 'PHQ-15':
		questions = ['Over the last week, how often have you been bothered by stomach pain?', 'Over the last week, how often have you been bothered by back pain?', 'Over the laast week, how often have you been bothered by pain in you arms, legs or joints (knees, hips, etc.)?', 'Over the last week, how often have you been bothered by menstural cramps or other problems with your periods?', 'Over the last week, how often have you been bothered by headaches?', 'Over the last week, how often have you been bothered by dizziness?', 'Over the last week, how often have you been bothered by feeling your heart pound or race?', 'Over the last week, how often have you been bothered by shortness or breath?', 'Over the last week, how often have you been bothered by pain or problems during sexual intercourse?', 'Over the alst week, how often have you been bthered by constipation, loos bowels or diarrhea?', 'Over the last week, how often have you been bothered by nausea, gas or indigestion?', 'Over the last week, how often have you been bothered by feeling tired or having low energy?', 'Over the last week, how often have you been bothered by trouble sleeping?', 'Over the last week, how often have you been bothered by chest pain?', 'Over the last week, how often have you been bothered by fainting spells?']
		answers = ["Not at all","Bothered a little","Bothered a lot"]
		outcomes = ["Low", "Medium", "High Somatic Symptom Severity"]

	elif questionaire == "Y-BOC":
		questions = ['how much of your time is occupied by obsessive thoughts?', "How much do your obsessive thoughts interfere with your work, school, social or other important role functioning? Is there anything that you don't do because of them?", 'How much distress do your obsessive thoughts cause you?', 'How much of an effort do you make to resist the obsessive thoughts? How often fo you try to disregard or turn your attention away from these thoughts as they enter your mind?', 'How much control do you have over your obsessive thoughts? How sucessful are you in stopping or diverting your obsessive thinking? Can you dismiss them?', 'How much time do you spend performing compulsive behaviors? How much long than most people does it take to complete routine activity because of your rituals? How frequently do you do rituals?', 'How much do your compulsive behaviors interfere with your work, school, social or other important role functioning? Is there anything your don;t do because of the compulsions?', 'How would you feel if prevented from prforming your compulsion (s)? how anxious would you become?', 'how much of an effort do you make to resist the compulsions?', 'How strong is the drive to perform the compulsive behavior? How much control do you have over the compulsions?']
		answers = answers = [
		"Not at all/minimal",
		"Observable time and interference",
		"Several times and causes high interference in day-to-day life",
		"Taking a high toll on life and compulsive"
		]
		outcomes = ["Mild", "Moderate", "Severe", "Extreme"]
	elif questionaire == 'GAD-7':
		questions = ['Over the last 2 weeks', ' how often have you been bothered by any of the following problems?', 'Feeling nervous', ' anxious or on edge?', 'Not being able to stop or control worrying?', 'Worrying too much about different things?', 'Trouble relaxing?', 'Being so restless that it si hard to sit still?', 'Becoming easily annoyed or irritable?', 'Feeling afraid as if something awful might happen?']
		answers = ['Not at all', 'Some days', 'Most days', "Almost every day"]
		outcomes= ["Mild", "Moderate", "Severe"]
	elif questionaire = 'Socrates':
		questions	=	['I really want to make changes in my drinking.', 'Sometimes I wonder if I am an alcoholic.', "If I don't change my drinking soon, my problems are going to get worse/", 'I have already started making some changes in my drinking.', "I was drinking too much at one time, but I've managed to change my drinking.", 'Sometimes I wonder if my drinking is hurting other people.', 'I am a problem drinker.', "I'm not just thinking about changing my drinking, I'm already doing something about it.", 'I have already changed my drinking, and I am looking for ways to keep from slipping back to my old pattern.', 'I have serious problems with drinking.', 'Sometimes I wonder if I am in control of my drinking.', 'My drinking is cauasing a lot of harm.', 'I am actively doing things now to cut down or stop drinking.', 'I want help to keep from going back to the drinking problems that I had before.', 'I know that I have a drinking problem.', 'There are times when I wonder if I drink too much.', 'I am an alcoholic.', 'I am working hard to change my drinking.', 'I have made some changes in my drinking, and I want some help to keep from going back to the way I used to drink.']
		answers = ["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"]
		outcomes = []
	elif questionaire == 'PSS':
		questions = ['In the last month, how often have you been upset because of something that happened unexpectedly?', 'In the last month, how often have you felt that you were unable to control the important things in your life?', 'In the last month, how often have you felt nervous and “stressed”?', 'In the last month, how often have you felt confident about your ability to handle your personal problems?', 'In the last month, how often have you felt that things were going your way?', 'In the last month, how often have you found that you could not cope with all the things that you had to do?', 'In the last month, how often have you been able to control irritations in your life?', 'In the last month, how often have you felt that you were on top of things?', 'In the last month, how often have you been angered because of things that were outside of your control?', 'In the last month, how often have you felt difficulties were piling up so high that you could not overcome them?.']
		answers = ["Never", "Almost never", "Sometimes", "Fairly often", "Very often"]
		outcomes = ["Low stress", "Moderate stress", "High stress"]

	elif questionaire = 'SPIN':
		questions = ['I am afraid of people in authority', 'I am bothered by blushing in front of people', 'Parties and social events scare me', "I avoid talking to people i don't know", 'Being criticized scares me a lot.', 'I avoid doing things or speaking to people for fear of embarrassment', 'Sweating in front of people causes me distress', 'I avoid going to parties', 'I avoid activities in which i am the center of attention', 'Talking to strangers scares me', 'I avoid having to gve speeches', 'I would do anything to avoid being criticized', 'Heart palpitations bother me when i am aroudn people', 'I am afraid of doing things when people might be watching', 'Being embarrassed of looking stupid are among my worst fears', 'I avoid speaking to anyone in authority', 'Trembling or shaking in front of others is distressing to me']
		answers = ["Not at all", "A little bit", "Somewhat", "Very much", "Extremely"]
		outcomes = []

	return {'text':questions[0], 'buttons':answers, 'type':typeOf}

def getQuestions(typeOf):
	questionaire = typeOf
	if typeOf== 'PHQuestions':
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

	elif typeOf == 'RelationshipQuestions':
		questions = ["How well does your partner meet your needs?","In general, how satisfied are you with your relationship?",
		"How good s your relationship compared to most?","How often do you wish you hadn't gotten into this relationship?",
		"To what extent has your relationship met your original expectations?","How much do you love your partner?","How many problems are there in your relationship?"]
		answers = ["Low", "Average","High"]
		outcomes = ["Low Satisfaction", "High Satisfaction"]

	elif questionaire == 'PHQ-15':
		questions = ['Over the last week, how often have you been bothered by stomach pain?', 'Over the last week, how often have you been bothered by back pain?', 'Over the laast week, how often have you been bothered by pain in you arms, legs or joints (knees, hips, etc.)?', 'Over the last week, how often have you been bothered by menstural cramps or other problems with your periods?', 'Over the last week, how often have you been bothered by headaches?', 'Over the last week, how often have you been bothered by dizziness?', 'Over the last week, how often have you been bothered by feeling your heart pound or race?', 'Over the last week, how often have you been bothered by shortness or breath?', 'Over the last week, how often have you been bothered by pain or problems during sexual intercourse?', 'Over the alst week, how often have you been bthered by constipation, loos bowels or diarrhea?', 'Over the last week, how often have you been bothered by nausea, gas or indigestion?', 'Over the last week, how often have you been bothered by feeling tired or having low energy?', 'Over the last week, how often have you been bothered by trouble sleeping?', 'Over the last week, how often have you been bothered by chest pain?', 'Over the last week, how often have you been bothered by fainting spells?']
		answers = ["Not at all","Bothered a little","Bothered a lot"]
		outcomes = ["Low", "Medium", "High Somatic Symptom Severity"]

	elif questionaire == "Y-BOC":
		questions = ['how much of your time is occupied by obsessive thoughts?', "How much do your obsessive thoughts interfere with your work, school, social or other important role functioning? Is there anything that you don't do because of them?", 'How much distress do your obsessive thoughts cause you?', 'How much of an effort do you make to resist the obsessive thoughts? How often fo you try to disregard or turn your attention away from these thoughts as they enter your mind?', 'How much control do you have over your obsessive thoughts? How sucessful are you in stopping or diverting your obsessive thinking? Can you dismiss them?', 'How much time do you spend performing compulsive behaviors? How much long than most people does it take to complete routine activity because of your rituals? How frequently do you do rituals?', 'How much do your compulsive behaviors interfere with your work, school, social or other important role functioning? Is there anything your don;t do because of the compulsions?', 'How would you feel if prevented from prforming your compulsion (s)? how anxious would you become?', 'how much of an effort do you make to resist the compulsions?', 'How strong is the drive to perform the compulsive behavior? How much control do you have over the compulsions?']
		answers = answers = [
		"Not at all/minimal",
		"Observable time and interference",
		"Several times and causes high interference in day-to-day life",
		"Taking a high toll on life and compulsive"
		]
		outcomes = ["Mild", "Moderate", "Severe", "Extreme"]
	elif questionaire == 'GAD-7':
		questions = ['Over the last 2 weeks', ' how often have you been bothered by any of the following problems?', 'Feeling nervous', ' anxious or on edge?', 'Not being able to stop or control worrying?', 'Worrying too much about different things?', 'Trouble relaxing?', 'Being so restless that it si hard to sit still?', 'Becoming easily annoyed or irritable?', 'Feeling afraid as if something awful might happen?']
		answers = ['Not at all', 'Some days', 'Most days', "Almost every day"]
		outcomes= ["Mild", "Moderate", "Severe"]
	elif questionaire = 'Socrates':
		questions	=	['I really want to make changes in my drinking.', 'Sometimes I wonder if I am an alcoholic.', "If I don't change my drinking soon, my problems are going to get worse/", 'I have already started making some changes in my drinking.', "I was drinking too much at one time, but I've managed to change my drinking.", 'Sometimes I wonder if my drinking is hurting other people.', 'I am a problem drinker.', "I'm not just thinking about changing my drinking, I'm already doing something about it.", 'I have already changed my drinking, and I am looking for ways to keep from slipping back to my old pattern.', 'I have serious problems with drinking.', 'Sometimes I wonder if I am in control of my drinking.', 'My drinking is cauasing a lot of harm.', 'I am actively doing things now to cut down or stop drinking.', 'I want help to keep from going back to the drinking problems that I had before.', 'I know that I have a drinking problem.', 'There are times when I wonder if I drink too much.', 'I am an alcoholic.', 'I am working hard to change my drinking.', 'I have made some changes in my drinking, and I want some help to keep from going back to the way I used to drink.']
		answers = ["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"]
		outcomes = []
	elif questionaire == 'PSS':
		questions = ['In the last month, how often have you been upset because of something that happened unexpectedly?', 'In the last month, how often have you felt that you were unable to control the important things in your life?', 'In the last month, how often have you felt nervous and “stressed”?', 'In the last month, how often have you felt confident about your ability to handle your personal problems?', 'In the last month, how often have you felt that things were going your way?', 'In the last month, how often have you found that you could not cope with all the things that you had to do?', 'In the last month, how often have you been able to control irritations in your life?', 'In the last month, how often have you felt that you were on top of things?', 'In the last month, how often have you been angered because of things that were outside of your control?', 'In the last month, how often have you felt difficulties were piling up so high that you could not overcome them?.']
		answers = ["Never", "Almost never", "Sometimes", "Fairly often", "Very often"]
		outcomes = ["Low stress", "Moderate stress", "High stress"]

	elif questionaire = 'SPIN':
		questions = ['I am afraid of people in authority', 'I am bothered by blushing in front of people', 'Parties and social events scare me', "I avoid talking to people i don't know", 'Being criticized scares me a lot.', 'I avoid doing things or speaking to people for fear of embarrassment', 'Sweating in front of people causes me distress', 'I avoid going to parties', 'I avoid activities in which i am the center of attention', 'Talking to strangers scares me', 'I avoid having to gve speeches', 'I would do anything to avoid being criticized', 'Heart palpitations bother me when i am aroudn people', 'I am afraid of doing things when people might be watching', 'Being embarrassed of looking stupid are among my worst fears', 'I avoid speaking to anyone in authority', 'Trembling or shaking in front of others is distressing to me']
		answers = ["Not at all", "A little bit", "Somewhat", "Very much", "Extremely"]
		outcomes = []

	return questions
