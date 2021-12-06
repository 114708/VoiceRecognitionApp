import speech_recognition as sr
import pyttsx3
import datetime
import json

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def write_json():
    jsonString = json.dumps(aDict)
    jsonFile = open("testdata.json", "w")
    jsonFile.write(jsonString)
    jsonFile.close()

def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():     # listening to the user's command
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'beep boop' in command:
                command = command.replace('beep boop', '')
                print(command)
    except:
        pass
    return command


command = take_command()


def test_questions():       # Test questions
    global candidate_response1
    global candidate_response2
    global candidate_response3
    f4 = open('testdata.json')
    data4 = json.load(f4)
    questionname1 = data4["response"][0]["sections"][0]["items"][0]["name1"]
    question1 = data4["response"][0]["sections"][0]["items"][0]["Question1"]
    questionname2 = data4["response"][0]["sections"][0]["items"][1]["name2"]
    question2 = data4["response"][0]["sections"][0]["items"][1]["Question2"]
    questionname3 = data4["response"][0]["sections"][0]["items"][2]["name3"]
    question3 = data4["response"][0]["sections"][0]["items"][2]["Question3"]
    options1 = data4["response"][0]["sections"][0]["items"][0]["Options1"]
    options2 = data4["response"][0]["sections"][0]["items"][1]["Options2"]
    options3 = data4["response"][0]["sections"][0]["items"][2]["Options3"]
    talk('This is' + questionname1)
    talk(question1)
    talk(options1)
    talk('Would you like the question repeated? Beep Boop')
    command = take_command()
    if 'yes' in command:
        talk('This is' + questionname1)
        talk(question1)
        talk(options1)
        command = take_command()
        talk('Please sate your answer. A, B, or C. Beep Boop')
        if 'A' in command: #Question 1
            candidate_response1 = 'A'
            print(command)
            aDict = {
            "count": None,
            "top": None,
            "skip": None,
            "pageCount": None,
            "nextPageLink": None,
            "prevPageLink": None,
            "response": [
                {
                    "test": {
                        "reference": "Test 1",
                        "name": "Test 1",
                        "id": 443
                    },
                    "testForm": {
                        "reference": "Test 2",
                        "name": "Test 2",
                        "id": 518
                    },
                    "subject": {
                        "reference": "Geography",
                        "name": "Geography",
                        "id": 200
                    },
                    "passMark": 0.0,
                    "passMarkType": "Percentage",
                    "percentageMark": 31.25,
                    "passPercentage": 0.0,
                    "keycode": "test",
                    "sections": [
                        {
                            "id": 1,
                            "name": "Section",
                            "mark": 1.0,
                            "percentageMark": 33.333,
                            "availableMarks": 3,
                            "passMark": 0.0,
                            "passPercentage": 0.0,
                            "passIRTScore": 'null',
                            "passMarkType": "Percentage",
                            "items": [
                                {
                                    "id": 101,
                                    "name1": "Question 1",
                                    "version": 2,
                                    "mark": 1.0,
                                    "awardedMark": 1.0,
                                    "availableMarks": 1,
                                    "surpassReference": "5199P6468",
                                    "nonScored": False,
                                    "type": "Question",
                                    "Question1": "What is the Capital of England",
                                    "Options1": {
                                        "A": "London",
                                        "B": "Edinburgh",
                                        "C": "Cardiff"
                                    },
                                    "correctAnswer1": "A",
                                    "candidateResponse1": {
                                        "Value1": candidate_response1
                                    },
                                    "correctlyAnswered1": "1"
                                },
                                {
                                    "id": 102,
                                    "name2": "Question 2",
                                    "version": 2,
                                    "mark": 0.0,
                                    "awardedMark": 0.0,
                                    "availableMarks": 1,
                                    "viewingTime": "2000",
                                    "learningOutcome": "",
                                    "markBreakdown": [],
                                    "unit": "",
                                    "surpassReference": "5199P6451",
                                    "nonScored": False,
                                    "type": "Question",
                                    "Question2": "What is the capital of Italy",
                                    "Options2": {
                                        "A": "Paris",
                                        "B": "Rome",
                                        "C": "Sydney"
                                    },
                                    "correctAnswer2": "B",
                                    "candidateResponse2": {
                                        "Value2": ""
                                    }
                                },
                                {
                                    "id": 103,
                                    "name3": "Question 3",
                                    "version": 2,
                                    "mark": 0.0,
                                    "awardedMark": 0.0,
                                    "availableMarks": 1,
                                    "viewingTime": "2000",
                                    "learningOutcome": "",
                                    "markBreakdown": [],
                                    "unit": "",
                                    "surpassReference": "5199P6454",
                                    "nonScored": False,
                                    "type": "Question",
                                    "Question3": "Which one of these is the correct wording for a coastal defense",
                                    "Options3": {
                                        "A": "Sea Wall",
                                        "B": "Sea Net",
                                        "C": "Moat"
                                    },
                                    "correctAnswer3": "A",
                                    "candidateResponse3": {
                                        "Value3": ""
                                    }
                                }
                            ],
                            "sectionSelectorId": None,
                            "selected": None,
                            "startTime": None,
                            "endTime": None,
                            "isPoolTimeSection": False,
                            "poolName": None,
                            "isSurveySection": False,
                            "decisionPoint": {
                                "upperValue": 0.0,
                                "lowerValue": 0.0,
                                "valueType": "Percent",
                                "sectionsToCheck": "CurrentOnly",
                                "outcome": None
                            }
                        }
                    ],
                    "centre": {
                        "id": 80,
                        "reference": "WTC"
                    },
                    "candidate": {
                        "id": 407,
                        "reference": "SAMPLE"
                    },
                    "mark": 0,
                    "availableMarks": 3,
                    "percentage": "",
                    "grade": "",
                    "startedDate": "2018-07-30 at 11:31:25.443",
                    "submittedDate": "2018-07-30 at 11:46:00",
                    "id": 1747,
                    "downloads": [
                        {
                            "os": "Microsoft Windows...",
                            "ipAddress": "82...",
                            "machineName": "BTL1...",
                            "dateTime": "17:13:27 Thu 07 Mar 2019",
                            "local": False,
                            "userName": "-1"
                        }
                    ]
                }
            ],
            "errors": None,
            "serverTimeZone": "GMT Standard Time"
        }
            write_json()
        if 'B' in command:
            candidate_response1 = 'B'
            print(command)
            aDict = {
                "count": None,
                "top": None,
                "skip": None,
                "pageCount": None,
                "nextPageLink": None,
                "prevPageLink": None,
                "response": [
                    {
                        "test": {
                            "reference": "Test 1",
                            "name": "Test 1",
                            "id": 443
                        },
                        "testForm": {
                            "reference": "Test 2",
                            "name": "Test 2",
                            "id": 518
                        },
                        "subject": {
                            "reference": "Geography",
                            "name": "Geography",
                            "id": 200
                        },
                        "passMark": 0.0,
                        "passMarkType": "Percentage",
                        "percentageMark": 31.25,
                        "passPercentage": 0.0,
                        "keycode": "test",
                        "sections": [
                            {
                                "id": 1,
                                "name": "Section",
                                "mark": 1.0,
                                "percentageMark": 33.333,
                                "availableMarks": 3,
                                "passMark": 0.0,
                                "passPercentage": 0.0,
                                "passIRTScore": 'null',
                                "passMarkType": "Percentage",
                                "items": [
                                    {
                                        "id": 101,
                                        "name1": "Question 1",
                                        "version": 2,
                                        "mark": 1.0,
                                        "awardedMark": 1.0,
                                        "availableMarks": 1,
                                        "surpassReference": "5199P6468",
                                        "nonScored": False,
                                        "type": "Question",
                                        "Question1": "What is the Capital of England",
                                        "Options1": {
                                            "A": "London",
                                            "B": "Edinburgh",
                                            "C": "Cardiff"
                                        },
                                        "correctAnswer1": "A",
                                        "candidateResponse1": {
                                            "Value1": candidate_response1
                                        },
                                        "correctlyAnswered1": "1"
                                    },
                                    {
                                        "id": 102,
                                        "name2": "Question 2",
                                        "version": 2,
                                        "mark": 0.0,
                                        "awardedMark": 0.0,
                                        "availableMarks": 1,
                                        "viewingTime": "2000",
                                        "learningOutcome": "",
                                        "markBreakdown": [],
                                        "unit": "",
                                        "surpassReference": "5199P6451",
                                        "nonScored": False,
                                        "type": "Question",
                                        "Question2": "What is the capital of Italy",
                                        "Options2": {
                                            "A": "Paris",
                                            "B": "Rome",
                                            "C": "Sydney"
                                        },
                                        "correctAnswer2": "B",
                                        "candidateResponse2": {
                                            "Value2": ""
                                        }
                                    },
                                    {
                                        "id": 103,
                                        "name3": "Question 3",
                                        "version": 2,
                                        "mark": 0.0,
                                        "awardedMark": 0.0,
                                        "availableMarks": 1,
                                        "viewingTime": "2000",
                                        "learningOutcome": "",
                                        "markBreakdown": [],
                                        "unit": "",
                                        "surpassReference": "5199P6454",
                                        "nonScored": False,
                                        "type": "Question",
                                        "Question3": "Which one of these is the correct wording for a coastal defense",
                                        "Options3": {
                                            "A": "Sea Wall",
                                            "B": "Sea Net",
                                            "C": "Moat"
                                        },
                                        "correctAnswer3": "A",
                                        "candidateResponse3": {
                                            "Value3": ""
                                        }
                                    }
                                ],
                                "sectionSelectorId": None,
                                "selected": None,
                                "startTime": None,
                                "endTime": None,
                                "isPoolTimeSection": False,
                                "poolName": None,
                                "isSurveySection": False,
                                "decisionPoint": {
                                    "upperValue": 0.0,
                                    "lowerValue": 0.0,
                                    "valueType": "Percent",
                                    "sectionsToCheck": "CurrentOnly",
                                    "outcome": None
                                }
                            }
                        ],
                        "centre": {
                            "id": 80,
                            "reference": "WTC"
                        },
                        "candidate": {
                            "id": 407,
                            "reference": "SAMPLE"
                        },
                        "mark": 0,
                        "availableMarks": 3,
                        "percentage": "",
                        "grade": "",
                        "startedDate": "2018-07-30 at 11:31:25.443",
                        "submittedDate": "2018-07-30 at 11:46:00",
                        "id": 1747,
                        "downloads": [
                            {
                                "os": "Microsoft Windows...",
                                "ipAddress": "82...",
                                "machineName": "BTL1...",
                                "dateTime": "17:13:27 Thu 07 Mar 2019",
                                "local": False,
                                "userName": "-1"
                            }
                        ]
                    }
                ],
                "errors": None,
                "serverTimeZone": "GMT Standard Time"
            }
            write_json()
        if 'C' in command:
            candidate_response1 = 'C'
            print(command)
            aDict = {
                "count": None,
                "top": None,
                "skip": None,
                "pageCount": None,
                "nextPageLink": None,
                "prevPageLink": None,
                "response": [
                    {
                        "test": {
                            "reference": "Test 1",
                            "name": "Test 1",
                            "id": 443
                        },
                        "testForm": {
                            "reference": "Test 2",
                            "name": "Test 2",
                            "id": 518
                        },
                        "subject": {
                            "reference": "Geography",
                            "name": "Geography",
                            "id": 200
                        },
                        "passMark": 0.0,
                        "passMarkType": "Percentage",
                        "percentageMark": 31.25,
                        "passPercentage": 0.0,
                        "keycode": "test",
                        "sections": [
                            {
                                "id": 1,
                                "name": "Section",
                                "mark": 1.0,
                                "percentageMark": 33.333,
                                "availableMarks": 3,
                                "passMark": 0.0,
                                "passPercentage": 0.0,
                                "passIRTScore": 'null',
                                "passMarkType": "Percentage",
                                "items": [
                                    {
                                        "id": 101,
                                        "name1": "Question 1",
                                        "version": 2,
                                        "mark": 1.0,
                                        "awardedMark": 1.0,
                                        "availableMarks": 1,
                                        "surpassReference": "5199P6468",
                                        "nonScored": False,
                                        "type": "Question",
                                        "Question1": "What is the Capital of England",
                                        "Options1": {
                                            "A": "London",
                                            "B": "Edinburgh",
                                            "C": "Cardiff"
                                        },
                                        "correctAnswer1": "A",
                                        "candidateResponse1": {
                                            "Value1": candidate_response1
                                        },
                                        "correctlyAnswered1": "1"
                                    },
                                    {
                                        "id": 102,
                                        "name2": "Question 2",
                                        "version": 2,
                                        "mark": 0.0,
                                        "awardedMark": 0.0,
                                        "availableMarks": 1,
                                        "viewingTime": "2000",
                                        "learningOutcome": "",
                                        "markBreakdown": [],
                                        "unit": "",
                                        "surpassReference": "5199P6451",
                                        "nonScored": False,
                                        "type": "Question",
                                        "Question2": "What is the capital of Italy",
                                        "Options2": {
                                            "A": "Paris",
                                            "B": "Rome",
                                            "C": "Sydney"
                                        },
                                        "correctAnswer2": "B",
                                        "candidateResponse2": {
                                            "Value2": ""
                                        }
                                    },
                                    {
                                        "id": 103,
                                        "name3": "Question 3",
                                        "version": 2,
                                        "mark": 0.0,
                                        "awardedMark": 0.0,
                                        "availableMarks": 1,
                                        "viewingTime": "2000",
                                        "learningOutcome": "",
                                        "markBreakdown": [],
                                        "unit": "",
                                        "surpassReference": "5199P6454",
                                        "nonScored": False,
                                        "type": "Question",
                                        "Question3": "Which one of these is the correct wording for a coastal defense",
                                        "Options3": {
                                            "A": "Sea Wall",
                                            "B": "Sea Net",
                                            "C": "Moat"
                                        },
                                        "correctAnswer3": "A",
                                        "candidateResponse3": {
                                            "Value3": ""
                                        }
                                    }
                                ],
                                "sectionSelectorId": None,
                                "selected": None,
                                "startTime": None,
                                "endTime": None,
                                "isPoolTimeSection": False,
                                "poolName": None,
                                "isSurveySection": False,
                                "decisionPoint": {
                                    "upperValue": 0.0,
                                    "lowerValue": 0.0,
                                    "valueType": "Percent",
                                    "sectionsToCheck": "CurrentOnly",
                                    "outcome": None
                                }
                            }
                        ],
                        "centre": {
                            "id": 80,
                            "reference": "WTC"
                        },
                        "candidate": {
                            "id": 407,
                            "reference": "SAMPLE"
                        },
                        "mark": 0,
                        "availableMarks": 3,
                        "percentage": "",
                        "grade": "",
                        "startedDate": "2018-07-30 at 11:31:25.443",
                        "submittedDate": "2018-07-30 at 11:46:00",
                        "id": 1747,
                        "downloads": [
                            {
                                "os": "Microsoft Windows...",
                                "ipAddress": "82...",
                                "machineName": "BTL1...",
                                "dateTime": "17:13:27 Thu 07 Mar 2019",
                                "local": False,
                                "userName": "-1"
                            }
                        ]
                    }
                ],
                "errors": None,
                "serverTimeZone": "GMT Standard Time"
            }
            write_json()
    elif 'no' in command:
        command = take_command()
        talk('Please sate your answer. A, B, or C. Beep Boop')
        if 'A' in command: #Question 1
            candidate_response1 = 'A'
            print(command)
            aDict = {
            "count": None,
            "top": None,
            "skip": None,
            "pageCount": None,
            "nextPageLink": None,
            "prevPageLink": None,
            "response": [
                {
                    "test": {
                        "reference": "Test 1",
                        "name": "Test 1",
                        "id": 443
                    },
                    "testForm": {
                        "reference": "Test 2",
                        "name": "Test 2",
                        "id": 518
                    },
                    "subject": {
                        "reference": "Geography",
                        "name": "Geography",
                        "id": 200
                    },
                    "passMark": 0.0,
                    "passMarkType": "Percentage",
                    "percentageMark": 31.25,
                    "passPercentage": 0.0,
                    "keycode": "test",
                    "sections": [
                        {
                            "id": 1,
                            "name": "Section",
                            "mark": 1.0,
                            "percentageMark": 33.333,
                            "availableMarks": 3,
                            "passMark": 0.0,
                            "passPercentage": 0.0,
                            "passIRTScore": 'null',
                            "passMarkType": "Percentage",
                            "items": [
                                {
                                    "id": 101,
                                    "name1": "Question 1",
                                    "version": 2,
                                    "mark": 1.0,
                                    "awardedMark": 1.0,
                                    "availableMarks": 1,
                                    "surpassReference": "5199P6468",
                                    "nonScored": False,
                                    "type": "Question",
                                    "Question1": "What is the Capital of England",
                                    "Options1": {
                                        "A": "London",
                                        "B": "Edinburgh",
                                        "C": "Cardiff"
                                    },
                                    "correctAnswer1": "A",
                                    "candidateResponse1": {
                                        "Value1": candidate_response1
                                    },
                                    "correctlyAnswered1": "1"
                                },
                                {
                                    "id": 102,
                                    "name2": "Question 2",
                                    "version": 2,
                                    "mark": 0.0,
                                    "awardedMark": 0.0,
                                    "availableMarks": 1,
                                    "viewingTime": "2000",
                                    "learningOutcome": "",
                                    "markBreakdown": [],
                                    "unit": "",
                                    "surpassReference": "5199P6451",
                                    "nonScored": False,
                                    "type": "Question",
                                    "Question2": "What is the capital of Italy",
                                    "Options2": {
                                        "A": "Paris",
                                        "B": "Rome",
                                        "C": "Sydney"
                                    },
                                    "correctAnswer2": "B",
                                    "candidateResponse2": {
                                        "Value2": ""
                                    }
                                },
                                {
                                    "id": 103,
                                    "name3": "Question 3",
                                    "version": 2,
                                    "mark": 0.0,
                                    "awardedMark": 0.0,
                                    "availableMarks": 1,
                                    "viewingTime": "2000",
                                    "learningOutcome": "",
                                    "markBreakdown": [],
                                    "unit": "",
                                    "surpassReference": "5199P6454",
                                    "nonScored": False,
                                    "type": "Question",
                                    "Question3": "Which one of these is the correct wording for a coastal defense",
                                    "Options3": {
                                        "A": "Sea Wall",
                                        "B": "Sea Net",
                                        "C": "Moat"
                                    },
                                    "correctAnswer3": "A",
                                    "candidateResponse3": {
                                        "Value3": ""
                                    }
                                }
                            ],
                            "sectionSelectorId": None,
                            "selected": None,
                            "startTime": None,
                            "endTime": None,
                            "isPoolTimeSection": False,
                            "poolName": None,
                            "isSurveySection": False,
                            "decisionPoint": {
                                "upperValue": 0.0,
                                "lowerValue": 0.0,
                                "valueType": "Percent",
                                "sectionsToCheck": "CurrentOnly",
                                "outcome": None
                            }
                        }
                    ],
                    "centre": {
                        "id": 80,
                        "reference": "WTC"
                    },
                    "candidate": {
                        "id": 407,
                        "reference": "SAMPLE"
                    },
                    "mark": 0,
                    "availableMarks": 3,
                    "percentage": "",
                    "grade": "",
                    "startedDate": "2018-07-30 at 11:31:25.443",
                    "submittedDate": "2018-07-30 at 11:46:00",
                    "id": 1747,
                    "downloads": [
                        {
                            "os": "Microsoft Windows...",
                            "ipAddress": "82...",
                            "machineName": "BTL1...",
                            "dateTime": "17:13:27 Thu 07 Mar 2019",
                            "local": False,
                            "userName": "-1"
                        }
                    ]
                }
            ],
            "errors": None,
            "serverTimeZone": "GMT Standard Time"
        }
            write_json()
        if 'B' in command:
            candidate_response1 = 'B'
            print(command)
            aDict = {
                "count": None,
                "top": None,
                "skip": None,
                "pageCount": None,
                "nextPageLink": None,
                "prevPageLink": None,
                "response": [
                    {
                        "test": {
                            "reference": "Test 1",
                            "name": "Test 1",
                            "id": 443
                        },
                        "testForm": {
                            "reference": "Test 2",
                            "name": "Test 2",
                            "id": 518
                        },
                        "subject": {
                            "reference": "Geography",
                            "name": "Geography",
                            "id": 200
                        },
                        "passMark": 0.0,
                        "passMarkType": "Percentage",
                        "percentageMark": 31.25,
                        "passPercentage": 0.0,
                        "keycode": "test",
                        "sections": [
                            {
                                "id": 1,
                                "name": "Section",
                                "mark": 1.0,
                                "percentageMark": 33.333,
                                "availableMarks": 3,
                                "passMark": 0.0,
                                "passPercentage": 0.0,
                                "passIRTScore": 'null',
                                "passMarkType": "Percentage",
                                "items": [
                                    {
                                        "id": 101,
                                        "name1": "Question 1",
                                        "version": 2,
                                        "mark": 1.0,
                                        "awardedMark": 1.0,
                                        "availableMarks": 1,
                                        "surpassReference": "5199P6468",
                                        "nonScored": False,
                                        "type": "Question",
                                        "Question1": "What is the Capital of England",
                                        "Options1": {
                                            "A": "London",
                                            "B": "Edinburgh",
                                            "C": "Cardiff"
                                        },
                                        "correctAnswer1": "A",
                                        "candidateResponse1": {
                                            "Value1": candidate_response1
                                        },
                                        "correctlyAnswered1": "1"
                                    },
                                    {
                                        "id": 102,
                                        "name2": "Question 2",
                                        "version": 2,
                                        "mark": 0.0,
                                        "awardedMark": 0.0,
                                        "availableMarks": 1,
                                        "viewingTime": "2000",
                                        "learningOutcome": "",
                                        "markBreakdown": [],
                                        "unit": "",
                                        "surpassReference": "5199P6451",
                                        "nonScored": False,
                                        "type": "Question",
                                        "Question2": "What is the capital of Italy",
                                        "Options2": {
                                            "A": "Paris",
                                            "B": "Rome",
                                            "C": "Sydney"
                                        },
                                        "correctAnswer2": "B",
                                        "candidateResponse2": {
                                            "Value2": ""
                                        }
                                    },
                                    {
                                        "id": 103,
                                        "name3": "Question 3",
                                        "version": 2,
                                        "mark": 0.0,
                                        "awardedMark": 0.0,
                                        "availableMarks": 1,
                                        "viewingTime": "2000",
                                        "learningOutcome": "",
                                        "markBreakdown": [],
                                        "unit": "",
                                        "surpassReference": "5199P6454",
                                        "nonScored": False,
                                        "type": "Question",
                                        "Question3": "Which one of these is the correct wording for a coastal defense",
                                        "Options3": {
                                            "A": "Sea Wall",
                                            "B": "Sea Net",
                                            "C": "Moat"
                                        },
                                        "correctAnswer3": "A",
                                        "candidateResponse3": {
                                            "Value3": ""
                                        }
                                    }
                                ],
                                "sectionSelectorId": None,
                                "selected": None,
                                "startTime": None,
                                "endTime": None,
                                "isPoolTimeSection": False,
                                "poolName": None,
                                "isSurveySection": False,
                                "decisionPoint": {
                                    "upperValue": 0.0,
                                    "lowerValue": 0.0,
                                    "valueType": "Percent",
                                    "sectionsToCheck": "CurrentOnly",
                                    "outcome": None
                                }
                            }
                        ],
                        "centre": {
                            "id": 80,
                            "reference": "WTC"
                        },
                        "candidate": {
                            "id": 407,
                            "reference": "SAMPLE"
                        },
                        "mark": 0,
                        "availableMarks": 3,
                        "percentage": "",
                        "grade": "",
                        "startedDate": "2018-07-30 at 11:31:25.443",
                        "submittedDate": "2018-07-30 at 11:46:00",
                        "id": 1747,
                        "downloads": [
                            {
                                "os": "Microsoft Windows...",
                                "ipAddress": "82...",
                                "machineName": "BTL1...",
                                "dateTime": "17:13:27 Thu 07 Mar 2019",
                                "local": False,
                                "userName": "-1"
                            }
                        ]
                    }
                ],
                "errors": None,
                "serverTimeZone": "GMT Standard Time"
            }
            write_json()
        if 'C' in command:
            candidate_response1 = 'C'
            print(command)
            aDict = {
                "count": None,
                "top": None,
                "skip": None,
                "pageCount": None,
                "nextPageLink": None,
                "prevPageLink": None,
                "response": [
                    {
                        "test": {
                            "reference": "Test 1",
                            "name": "Test 1",
                            "id": 443
                        },
                        "testForm": {
                            "reference": "Test 2",
                            "name": "Test 2",
                            "id": 518
                        },
                        "subject": {
                            "reference": "Geography",
                            "name": "Geography",
                            "id": 200
                        },
                        "passMark": 0.0,
                        "passMarkType": "Percentage",
                        "percentageMark": 31.25,
                        "passPercentage": 0.0,
                        "keycode": "test",
                        "sections": [
                            {
                                "id": 1,
                                "name": "Section",
                                "mark": 1.0,
                                "percentageMark": 33.333,
                                "availableMarks": 3,
                                "passMark": 0.0,
                                "passPercentage": 0.0,
                                "passIRTScore": 'null',
                                "passMarkType": "Percentage",
                                "items": [
                                    {
                                        "id": 101,
                                        "name1": "Question 1",
                                        "version": 2,
                                        "mark": 1.0,
                                        "awardedMark": 1.0,
                                        "availableMarks": 1,
                                        "surpassReference": "5199P6468",
                                        "nonScored": False,
                                        "type": "Question",
                                        "Question1": "What is the Capital of England",
                                        "Options1": {
                                            "A": "London",
                                            "B": "Edinburgh",
                                            "C": "Cardiff"
                                        },
                                        "correctAnswer1": "A",
                                        "candidateResponse1": {
                                            "Value1": candidate_response1
                                        },
                                        "correctlyAnswered1": "1"
                                    },
                                    {
                                        "id": 102,
                                        "name2": "Question 2",
                                        "version": 2,
                                        "mark": 0.0,
                                        "awardedMark": 0.0,
                                        "availableMarks": 1,
                                        "viewingTime": "2000",
                                        "learningOutcome": "",
                                        "markBreakdown": [],
                                        "unit": "",
                                        "surpassReference": "5199P6451",
                                        "nonScored": False,
                                        "type": "Question",
                                        "Question2": "What is the capital of Italy",
                                        "Options2": {
                                            "A": "Paris",
                                            "B": "Rome",
                                            "C": "Sydney"
                                        },
                                        "correctAnswer2": "B",
                                        "candidateResponse2": {
                                            "Value2": ""
                                        }
                                    },
                                    {
                                        "id": 103,
                                        "name3": "Question 3",
                                        "version": 2,
                                        "mark": 0.0,
                                        "awardedMark": 0.0,
                                        "availableMarks": 1,
                                        "viewingTime": "2000",
                                        "learningOutcome": "",
                                        "markBreakdown": [],
                                        "unit": "",
                                        "surpassReference": "5199P6454",
                                        "nonScored": False,
                                        "type": "Question",
                                        "Question3": "Which one of these is the correct wording for a coastal defense",
                                        "Options3": {
                                            "A": "Sea Wall",
                                            "B": "Sea Net",
                                            "C": "Moat"
                                        },
                                        "correctAnswer3": "A",
                                        "candidateResponse3": {
                                            "Value3": ""
                                        }
                                    }
                                ],
                                "sectionSelectorId": None,
                                "selected": None,
                                "startTime": None,
                                "endTime": None,
                                "isPoolTimeSection": False,
                                "poolName": None,
                                "isSurveySection": False,
                                "decisionPoint": {
                                    "upperValue": 0.0,
                                    "lowerValue": 0.0,
                                    "valueType": "Percent",
                                    "sectionsToCheck": "CurrentOnly",
                                    "outcome": None
                                }
                            }
                        ],
                        "centre": {
                            "id": 80,
                            "reference": "WTC"
                        },
                        "candidate": {
                            "id": 407,
                            "reference": "SAMPLE"
                        },
                        "mark": 0,
                        "availableMarks": 3,
                        "percentage": "",
                        "grade": "",
                        "startedDate": "2018-07-30 at 11:31:25.443",
                        "submittedDate": "2018-07-30 at 11:46:00",
                        "id": 1747,
                        "downloads": [
                            {
                                "os": "Microsoft Windows...",
                                "ipAddress": "82...",
                                "machineName": "BTL1...",
                                "dateTime": "17:13:27 Thu 07 Mar 2019",
                                "local": False,
                                "userName": "-1"
                            }
                        ]
                    }
                ],
                "errors": None,
                "serverTimeZone": "GMT Standard Time"
            }
            write_json()
    talk('This is' + questionname2)
    talk(question2)
    talk(options2)
    talk('Would you like the question repeated? Beep Boop')
    command = take_command()
    if 'yes' in command:
        talk('This is' + questionname2)
        talk(question2)
        talk(options2)
        command = take_command()
        talk('Please sate your answer. A, B, or C. Beep Boop')
        if 'A' in command: #Question 2
            candidate_response2 = 'A'
            print(command)
            aDict = {
                "count": None,
                "top": None,
                "skip": None,
                "pageCount": None,
                "nextPageLink": None,
                "prevPageLink": None,
                "response": [
                    {
                        "test": {
                            "reference": "Test 1",
                            "name": "Test 1",
                            "id": 443
                        },
                        "testForm": {
                            "reference": "Test 2",
                            "name": "Test 2",
                            "id": 518
                        },
                        "subject": {
                            "reference": "Geography",
                            "name": "Geography",
                            "id": 200
                        },
                        "passMark": 0.0,
                        "passMarkType": "Percentage",
                        "percentageMark": 31.25,
                        "passPercentage": 0.0,
                        "keycode": "test",
                        "sections": [
                            {
                                "id": 1,
                                "name": "Section",
                                "mark": 1.0,
                                "percentageMark": 33.333,
                                "availableMarks": 3,
                                "passMark": 0.0,
                                "passPercentage": 0.0,
                                "passIRTScore": 'null',
                                "passMarkType": "Percentage",
                                "items": [
                                    {
                                        "id": 101,
                                        "name1": "Question 1",
                                        "version": 2,
                                        "mark": 1.0,
                                        "awardedMark": 1.0,
                                        "availableMarks": 1,
                                        "surpassReference": "5199P6468",
                                        "nonScored": False,
                                        "type": "Question",
                                        "Question1": "What is the Capital of England",
                                        "Options1": {
                                            "A": "London",
                                            "B": "Edinburgh",
                                            "C": "Cardiff"
                                        },
                                        "correctAnswer1": "A",
                                        "candidateResponse1": {
                                            "Value1": candidate_response1
                                        },
                                        "correctlyAnswered1": "1"
                                    },
                                    {
                                        "id": 102,
                                        "name2": "Question 2",
                                        "version": 2,
                                        "mark": 0.0,
                                        "awardedMark": 0.0,
                                        "availableMarks": 1,
                                        "viewingTime": "2000",
                                        "learningOutcome": "",
                                        "markBreakdown": [],
                                        "unit": "",
                                        "surpassReference": "5199P6451",
                                        "nonScored": False,
                                        "type": "Question",
                                        "Question2": "What is the capital of Italy",
                                        "Options2": {
                                            "A": "Paris",
                                            "B": "Rome",
                                            "C": "Sydney"
                                        },
                                        "correctAnswer2": "B",
                                        "candidateResponse2": {
                                            "Value2": candidate_response2
                                        }
                                    },
                                    {
                                        "id": 103,
                                        "name3": "Question 3",
                                        "version": 2,
                                        "mark": 0.0,
                                        "awardedMark": 0.0,
                                        "availableMarks": 1,
                                        "viewingTime": "2000",
                                        "learningOutcome": "",
                                        "markBreakdown": [],
                                        "unit": "",
                                        "surpassReference": "5199P6454",
                                        "nonScored": False,
                                        "type": "Question",
                                        "Question3": "Which one of these is the correct wording for a coastal defense",
                                        "Options3": {
                                            "A": "Sea Wall",
                                            "B": "Sea Net",
                                            "C": "Moat"
                                        },
                                        "correctAnswer3": "A",
                                        "candidateResponse3": {
                                            "Value3": ""
                                        }
                                    }
                                ],
                                "sectionSelectorId": None,
                                "selected": None,
                                "startTime": None,
                                "endTime": None,
                                "isPoolTimeSection": False,
                                "poolName": None,
                                "isSurveySection": False,
                                "decisionPoint": {
                                    "upperValue": 0.0,
                                    "lowerValue": 0.0,
                                    "valueType": "Percent",
                                    "sectionsToCheck": "CurrentOnly",
                                    "outcome": None
                                }
                            }
                        ],
                        "centre": {
                            "id": 80,
                            "reference": "WTC"
                        },
                        "candidate": {
                            "id": 407,
                            "reference": "SAMPLE"
                        },
                        "mark": 0,
                        "availableMarks": 3,
                        "percentage": "",
                        "grade": "",
                        "startedDate": "2018-07-30 at 11:31:25.443",
                        "submittedDate": "2018-07-30 at 11:46:00",
                        "id": 1747,
                        "downloads": [
                            {
                                "os": "Microsoft Windows...",
                                "ipAddress": "82...",
                                "machineName": "BTL1...",
                                "dateTime": "17:13:27 Thu 07 Mar 2019",
                                "local": False,
                                "userName": "-1"
                            }
                        ]
                    }
                ],
                "errors": None,
                "serverTimeZone": "GMT Standard Time"
            }
            write_json()
        if 'B' in command:
            candidate_response2 = 'B'
            print(command)
            aDict = {
                "count": None,
                "top": None,
                "skip": None,
                "pageCount": None,
                "nextPageLink": None,
                "prevPageLink": None,
                "response": [
                    {
                        "test": {
                            "reference": "Test 1",
                            "name": "Test 1",
                            "id": 443
                        },
                        "testForm": {
                            "reference": "Test 2",
                            "name": "Test 2",
                            "id": 518
                        },
                        "subject": {
                            "reference": "Geography",
                            "name": "Geography",
                            "id": 200
                        },
                        "passMark": 0.0,
                        "passMarkType": "Percentage",
                        "percentageMark": 31.25,
                        "passPercentage": 0.0,
                        "keycode": "test",
                        "sections": [
                            {
                                "id": 1,
                                "name": "Section",
                                "mark": 1.0,
                                "percentageMark": 33.333,
                                "availableMarks": 3,
                                "passMark": 0.0,
                                "passPercentage": 0.0,
                                "passIRTScore": 'null',
                                "passMarkType": "Percentage",
                                "items": [
                                    {
                                        "id": 101,
                                        "name1": "Question 1",
                                        "version": 2,
                                        "mark": 1.0,
                                        "awardedMark": 1.0,
                                        "availableMarks": 1,
                                        "surpassReference": "5199P6468",
                                        "nonScored": False,
                                        "type": "Question",
                                        "Question1": "What is the Capital of England",
                                        "Options1": {
                                            "A": "London",
                                            "B": "Edinburgh",
                                            "C": "Cardiff"
                                        },
                                        "correctAnswer1": "A",
                                        "candidateResponse1": {
                                            "Value1": candidate_response1
                                        },
                                        "correctlyAnswered1": "1"
                                    },
                                    {
                                        "id": 102,
                                        "name2": "Question 2",
                                        "version": 2,
                                        "mark": 0.0,
                                        "awardedMark": 0.0,
                                        "availableMarks": 1,
                                        "viewingTime": "2000",
                                        "learningOutcome": "",
                                        "markBreakdown": [],
                                        "unit": "",
                                        "surpassReference": "5199P6451",
                                        "nonScored": False,
                                        "type": "Question",
                                        "Question2": "What is the capital of Italy",
                                        "Options2": {
                                            "A": "Paris",
                                            "B": "Rome",
                                            "C": "Sydney"
                                        },
                                        "correctAnswer2": "B",
                                        "candidateResponse2": {
                                            "Value2": candidate_response2
                                        }
                                    },
                                    {
                                        "id": 103,
                                        "name3": "Question 3",
                                        "version": 2,
                                        "mark": 0.0,
                                        "awardedMark": 0.0,
                                        "availableMarks": 1,
                                        "viewingTime": "2000",
                                        "learningOutcome": "",
                                        "markBreakdown": [],
                                        "unit": "",
                                        "surpassReference": "5199P6454",
                                        "nonScored": False,
                                        "type": "Question",
                                        "Question3": "Which one of these is the correct wording for a coastal defense",
                                        "Options3": {
                                            "A": "Sea Wall",
                                            "B": "Sea Net",
                                            "C": "Moat"
                                        },
                                        "correctAnswer3": "A",
                                        "candidateResponse3": {
                                            "Value3": ""
                                        }
                                    }
                                ],
                                "sectionSelectorId": None,
                                "selected": None,
                                "startTime": None,
                                "endTime": None,
                                "isPoolTimeSection": False,
                                "poolName": None,
                                "isSurveySection": False,
                                "decisionPoint": {
                                    "upperValue": 0.0,
                                    "lowerValue": 0.0,
                                    "valueType": "Percent",
                                    "sectionsToCheck": "CurrentOnly",
                                    "outcome": None
                                }
                            }
                        ],
                        "centre": {
                            "id": 80,
                            "reference": "WTC"
                        },
                        "candidate": {
                            "id": 407,
                            "reference": "SAMPLE"
                        },
                        "mark": 0,
                        "availableMarks": 3,
                        "percentage": "",
                        "grade": "",
                        "startedDate": "2018-07-30 at 11:31:25.443",
                        "submittedDate": "2018-07-30 at 11:46:00",
                        "id": 1747,
                        "downloads": [
                            {
                                "os": "Microsoft Windows...",
                                "ipAddress": "82...",
                                "machineName": "BTL1...",
                                "dateTime": "17:13:27 Thu 07 Mar 2019",
                                "local": False,
                                "userName": "-1"
                            }
                        ]
                    }
                ],
                "errors": None,
                "serverTimeZone": "GMT Standard Time"
            }
            write_json()
        if 'C' in command:
            candidate_response2 = 'C'
            print(command)
            aDict = {
                "count": None,
                "top": None,
                "skip": None,
                "pageCount": None,
                "nextPageLink": None,
                "prevPageLink": None,
                "response": [
                    {
                        "test": {
                            "reference": "Test 1",
                            "name": "Test 1",
                            "id": 443
                        },
                        "testForm": {
                            "reference": "Test 2",
                            "name": "Test 2",
                            "id": 518
                        },
                        "subject": {
                            "reference": "Geography",
                            "name": "Geography",
                            "id": 200
                        },
                        "passMark": 0.0,
                        "passMarkType": "Percentage",
                        "percentageMark": 31.25,
                        "passPercentage": 0.0,
                        "keycode": "test",
                        "sections": [
                            {
                                "id": 1,
                                "name": "Section",
                                "mark": 1.0,
                                "percentageMark": 33.333,
                                "availableMarks": 3,
                                "passMark": 0.0,
                                "passPercentage": 0.0,
                                "passIRTScore": 'null',
                                "passMarkType": "Percentage",
                                "items": [
                                    {
                                        "id": 101,
                                        "name1": "Question 1",
                                        "version": 2,
                                        "mark": 1.0,
                                        "awardedMark": 1.0,
                                        "availableMarks": 1,
                                        "surpassReference": "5199P6468",
                                        "nonScored": False,
                                        "type": "Question",
                                        "Question1": "What is the Capital of England",
                                        "Options1": {
                                            "A": "London",
                                            "B": "Edinburgh",
                                            "C": "Cardiff"
                                        },
                                        "correctAnswer1": "A",
                                        "candidateResponse1": {
                                            "Value1": candidate_response1
                                        },
                                        "correctlyAnswered1": "1"
                                    },
                                    {
                                        "id": 102,
                                        "name2": "Question 2",
                                        "version": 2,
                                        "mark": 0.0,
                                        "awardedMark": 0.0,
                                        "availableMarks": 1,
                                        "viewingTime": "2000",
                                        "learningOutcome": "",
                                        "markBreakdown": [],
                                        "unit": "",
                                        "surpassReference": "5199P6451",
                                        "nonScored": False,
                                        "type": "Question",
                                        "Question2": "What is the capital of Italy",
                                        "Options2": {
                                            "A": "Paris",
                                            "B": "Rome",
                                            "C": "Sydney"
                                        },
                                        "correctAnswer2": "B",
                                        "candidateResponse2": {
                                            "Value2": candidate_response2
                                        }
                                    },
                                    {
                                        "id": 103,
                                        "name3": "Question 3",
                                        "version": 2,
                                        "mark": 0.0,
                                        "awardedMark": 0.0,
                                        "availableMarks": 1,
                                        "viewingTime": "2000",
                                        "learningOutcome": "",
                                        "markBreakdown": [],
                                        "unit": "",
                                        "surpassReference": "5199P6454",
                                        "nonScored": False,
                                        "type": "Question",
                                        "Question3": "Which one of these is the correct wording for a coastal defense",
                                        "Options3": {
                                            "A": "Sea Wall",
                                            "B": "Sea Net",
                                            "C": "Moat"
                                        },
                                        "correctAnswer3": "A",
                                        "candidateResponse3": {
                                            "Value3": ""
                                        }
                                    }
                                ],
                                "sectionSelectorId": None,
                                "selected": None,
                                "startTime": None,
                                "endTime": None,
                                "isPoolTimeSection": False,
                                "poolName": None,
                                "isSurveySection": False,
                                "decisionPoint": {
                                    "upperValue": 0.0,
                                    "lowerValue": 0.0,
                                    "valueType": "Percent",
                                    "sectionsToCheck": "CurrentOnly",
                                    "outcome": None
                                }
                            }
                        ],
                        "centre": {
                            "id": 80,
                            "reference": "WTC"
                        },
                        "candidate": {
                            "id": 407,
                            "reference": "SAMPLE"
                        },
                        "mark": 0,
                        "availableMarks": 3,
                        "percentage": "",
                        "grade": "",
                        "startedDate": "2018-07-30 at 11:31:25.443",
                        "submittedDate": "2018-07-30 at 11:46:00",
                        "id": 1747,
                        "downloads": [
                            {
                                "os": "Microsoft Windows...",
                                "ipAddress": "82...",
                                "machineName": "BTL1...",
                                "dateTime": "17:13:27 Thu 07 Mar 2019",
                                "local": False,
                                "userName": "-1"
                            }
                        ]
                    }
                ],
                "errors": None,
                "serverTimeZone": "GMT Standard Time"
            }
            write_json()
    elif 'no' in command:
        command = take_command()
        talk('Please sate your answer. A, B, or C. Beep Boop')
        if 'A' in command: #Question 2
            candidate_response2 = 'A'
            print(command)
            aDict = {
                "count": None,
                "top": None,
                "skip": None,
                "pageCount": None,
                "nextPageLink": None,
                "prevPageLink": None,
                "response": [
                    {
                        "test": {
                            "reference": "Test 1",
                            "name": "Test 1",
                            "id": 443
                        },
                        "testForm": {
                            "reference": "Test 2",
                            "name": "Test 2",
                            "id": 518
                        },
                        "subject": {
                            "reference": "Geography",
                            "name": "Geography",
                            "id": 200
                        },
                        "passMark": 0.0,
                        "passMarkType": "Percentage",
                        "percentageMark": 31.25,
                        "passPercentage": 0.0,
                        "keycode": "test",
                        "sections": [
                            {
                                "id": 1,
                                "name": "Section",
                                "mark": 1.0,
                                "percentageMark": 33.333,
                                "availableMarks": 3,
                                "passMark": 0.0,
                                "passPercentage": 0.0,
                                "passIRTScore": 'null',
                                "passMarkType": "Percentage",
                                "items": [
                                    {
                                        "id": 101,
                                        "name1": "Question 1",
                                        "version": 2,
                                        "mark": 1.0,
                                        "awardedMark": 1.0,
                                        "availableMarks": 1,
                                        "surpassReference": "5199P6468",
                                        "nonScored": False,
                                        "type": "Question",
                                        "Question1": "What is the Capital of England",
                                        "Options1": {
                                            "A": "London",
                                            "B": "Edinburgh",
                                            "C": "Cardiff"
                                        },
                                        "correctAnswer1": "A",
                                        "candidateResponse1": {
                                            "Value1": candidate_response1
                                        },
                                        "correctlyAnswered1": "1"
                                    },
                                    {
                                        "id": 102,
                                        "name2": "Question 2",
                                        "version": 2,
                                        "mark": 0.0,
                                        "awardedMark": 0.0,
                                        "availableMarks": 1,
                                        "viewingTime": "2000",
                                        "learningOutcome": "",
                                        "markBreakdown": [],
                                        "unit": "",
                                        "surpassReference": "5199P6451",
                                        "nonScored": False,
                                        "type": "Question",
                                        "Question2": "What is the capital of Italy",
                                        "Options2": {
                                            "A": "Paris",
                                            "B": "Rome",
                                            "C": "Sydney"
                                        },
                                        "correctAnswer2": "B",
                                        "candidateResponse2": {
                                            "Value2": candidate_response2
                                        }
                                    },
                                    {
                                        "id": 103,
                                        "name3": "Question 3",
                                        "version": 2,
                                        "mark": 0.0,
                                        "awardedMark": 0.0,
                                        "availableMarks": 1,
                                        "viewingTime": "2000",
                                        "learningOutcome": "",
                                        "markBreakdown": [],
                                        "unit": "",
                                        "surpassReference": "5199P6454",
                                        "nonScored": False,
                                        "type": "Question",
                                        "Question3": "Which one of these is the correct wording for a coastal defense",
                                        "Options3": {
                                            "A": "Sea Wall",
                                            "B": "Sea Net",
                                            "C": "Moat"
                                        },
                                        "correctAnswer3": "A",
                                        "candidateResponse3": {
                                            "Value3": ""
                                        }
                                    }
                                ],
                                "sectionSelectorId": None,
                                "selected": None,
                                "startTime": None,
                                "endTime": None,
                                "isPoolTimeSection": False,
                                "poolName": None,
                                "isSurveySection": False,
                                "decisionPoint": {
                                    "upperValue": 0.0,
                                    "lowerValue": 0.0,
                                    "valueType": "Percent",
                                    "sectionsToCheck": "CurrentOnly",
                                    "outcome": None
                                }
                            }
                        ],
                        "centre": {
                            "id": 80,
                            "reference": "WTC"
                        },
                        "candidate": {
                            "id": 407,
                            "reference": "SAMPLE"
                        },
                        "mark": 0,
                        "availableMarks": 3,
                        "percentage": "",
                        "grade": "",
                        "startedDate": "2018-07-30 at 11:31:25.443",
                        "submittedDate": "2018-07-30 at 11:46:00",
                        "id": 1747,
                        "downloads": [
                            {
                                "os": "Microsoft Windows...",
                                "ipAddress": "82...",
                                "machineName": "BTL1...",
                                "dateTime": "17:13:27 Thu 07 Mar 2019",
                                "local": False,
                                "userName": "-1"
                            }
                        ]
                    }
                ],
                "errors": None,
                "serverTimeZone": "GMT Standard Time"
            }
            write_json()
        if 'B' in command:
            candidate_response2 = 'B'
            print(command)
            aDict = {
                "count": None,
                "top": None,
                "skip": None,
                "pageCount": None,
                "nextPageLink": None,
                "prevPageLink": None,
                "response": [
                    {
                        "test": {
                            "reference": "Test 1",
                            "name": "Test 1",
                            "id": 443
                        },
                        "testForm": {
                            "reference": "Test 2",
                            "name": "Test 2",
                            "id": 518
                        },
                        "subject": {
                            "reference": "Geography",
                            "name": "Geography",
                            "id": 200
                        },
                        "passMark": 0.0,
                        "passMarkType": "Percentage",
                        "percentageMark": 31.25,
                        "passPercentage": 0.0,
                        "keycode": "test",
                        "sections": [
                            {
                                "id": 1,
                                "name": "Section",
                                "mark": 1.0,
                                "percentageMark": 33.333,
                                "availableMarks": 3,
                                "passMark": 0.0,
                                "passPercentage": 0.0,
                                "passIRTScore": 'null',
                                "passMarkType": "Percentage",
                                "items": [
                                    {
                                        "id": 101,
                                        "name1": "Question 1",
                                        "version": 2,
                                        "mark": 1.0,
                                        "awardedMark": 1.0,
                                        "availableMarks": 1,
                                        "surpassReference": "5199P6468",
                                        "nonScored": False,
                                        "type": "Question",
                                        "Question1": "What is the Capital of England",
                                        "Options1": {
                                            "A": "London",
                                            "B": "Edinburgh",
                                            "C": "Cardiff"
                                        },
                                        "correctAnswer1": "A",
                                        "candidateResponse1": {
                                            "Value1": candidate_response1
                                        },
                                        "correctlyAnswered1": "1"
                                    },
                                    {
                                        "id": 102,
                                        "name2": "Question 2",
                                        "version": 2,
                                        "mark": 0.0,
                                        "awardedMark": 0.0,
                                        "availableMarks": 1,
                                        "viewingTime": "2000",
                                        "learningOutcome": "",
                                        "markBreakdown": [],
                                        "unit": "",
                                        "surpassReference": "5199P6451",
                                        "nonScored": False,
                                        "type": "Question",
                                        "Question2": "What is the capital of Italy",
                                        "Options2": {
                                            "A": "Paris",
                                            "B": "Rome",
                                            "C": "Sydney"
                                        },
                                        "correctAnswer2": "B",
                                        "candidateResponse2": {
                                            "Value2": candidate_response2
                                        }
                                    },
                                    {
                                        "id": 103,
                                        "name3": "Question 3",
                                        "version": 2,
                                        "mark": 0.0,
                                        "awardedMark": 0.0,
                                        "availableMarks": 1,
                                        "viewingTime": "2000",
                                        "learningOutcome": "",
                                        "markBreakdown": [],
                                        "unit": "",
                                        "surpassReference": "5199P6454",
                                        "nonScored": False,
                                        "type": "Question",
                                        "Question3": "Which one of these is the correct wording for a coastal defense",
                                        "Options3": {
                                            "A": "Sea Wall",
                                            "B": "Sea Net",
                                            "C": "Moat"
                                        },
                                        "correctAnswer3": "A",
                                        "candidateResponse3": {
                                            "Value3": ""
                                        }
                                    }
                                ],
                                "sectionSelectorId": None,
                                "selected": None,
                                "startTime": None,
                                "endTime": None,
                                "isPoolTimeSection": False,
                                "poolName": None,
                                "isSurveySection": False,
                                "decisionPoint": {
                                    "upperValue": 0.0,
                                    "lowerValue": 0.0,
                                    "valueType": "Percent",
                                    "sectionsToCheck": "CurrentOnly",
                                    "outcome": None
                                }
                            }
                        ],
                        "centre": {
                            "id": 80,
                            "reference": "WTC"
                        },
                        "candidate": {
                            "id": 407,
                            "reference": "SAMPLE"
                        },
                        "mark": 0,
                        "availableMarks": 3,
                        "percentage": "",
                        "grade": "",
                        "startedDate": "2018-07-30 at 11:31:25.443",
                        "submittedDate": "2018-07-30 at 11:46:00",
                        "id": 1747,
                        "downloads": [
                            {
                                "os": "Microsoft Windows...",
                                "ipAddress": "82...",
                                "machineName": "BTL1...",
                                "dateTime": "17:13:27 Thu 07 Mar 2019",
                                "local": False,
                                "userName": "-1"
                            }
                        ]
                    }
                ],
                "errors": None,
                "serverTimeZone": "GMT Standard Time"
            }
            write_json()
        if 'C' in command:
            candidate_response2 = 'C'
            print(command)
            aDict = {
                "count": None,
                "top": None,
                "skip": None,
                "pageCount": None,
                "nextPageLink": None,
                "prevPageLink": None,
                "response": [
                    {
                        "test": {
                            "reference": "Test 1",
                            "name": "Test 1",
                            "id": 443
                        },
                        "testForm": {
                            "reference": "Test 2",
                            "name": "Test 2",
                            "id": 518
                        },
                        "subject": {
                            "reference": "Geography",
                            "name": "Geography",
                            "id": 200
                        },
                        "passMark": 0.0,
                        "passMarkType": "Percentage",
                        "percentageMark": 31.25,
                        "passPercentage": 0.0,
                        "keycode": "test",
                        "sections": [
                            {
                                "id": 1,
                                "name": "Section",
                                "mark": 1.0,
                                "percentageMark": 33.333,
                                "availableMarks": 3,
                                "passMark": 0.0,
                                "passPercentage": 0.0,
                                "passIRTScore": 'null',
                                "passMarkType": "Percentage",
                                "items": [
                                    {
                                        "id": 101,
                                        "name1": "Question 1",
                                        "version": 2,
                                        "mark": 1.0,
                                        "awardedMark": 1.0,
                                        "availableMarks": 1,
                                        "surpassReference": "5199P6468",
                                        "nonScored": False,
                                        "type": "Question",
                                        "Question1": "What is the Capital of England",
                                        "Options1": {
                                            "A": "London",
                                            "B": "Edinburgh",
                                            "C": "Cardiff"
                                        },
                                        "correctAnswer1": "A",
                                        "candidateResponse1": {
                                            "Value1": candidate_response1
                                        },
                                        "correctlyAnswered1": "1"
                                    },
                                    {
                                        "id": 102,
                                        "name2": "Question 2",
                                        "version": 2,
                                        "mark": 0.0,
                                        "awardedMark": 0.0,
                                        "availableMarks": 1,
                                        "viewingTime": "2000",
                                        "learningOutcome": "",
                                        "markBreakdown": [],
                                        "unit": "",
                                        "surpassReference": "5199P6451",
                                        "nonScored": False,
                                        "type": "Question",
                                        "Question2": "What is the capital of Italy",
                                        "Options2": {
                                            "A": "Paris",
                                            "B": "Rome",
                                            "C": "Sydney"
                                        },
                                        "correctAnswer2": "B",
                                        "candidateResponse2": {
                                            "Value2": candidate_response2
                                        }
                                    },
                                    {
                                        "id": 103,
                                        "name3": "Question 3",
                                        "version": 2,
                                        "mark": 0.0,
                                        "awardedMark": 0.0,
                                        "availableMarks": 1,
                                        "viewingTime": "2000",
                                        "learningOutcome": "",
                                        "markBreakdown": [],
                                        "unit": "",
                                        "surpassReference": "5199P6454",
                                        "nonScored": False,
                                        "type": "Question",
                                        "Question3": "Which one of these is the correct wording for a coastal defense",
                                        "Options3": {
                                            "A": "Sea Wall",
                                            "B": "Sea Net",
                                            "C": "Moat"
                                        },
                                        "correctAnswer3": "A",
                                        "candidateResponse3": {
                                            "Value3": ""
                                        }
                                    }
                                ],
                                "sectionSelectorId": None,
                                "selected": None,
                                "startTime": None,
                                "endTime": None,
                                "isPoolTimeSection": False,
                                "poolName": None,
                                "isSurveySection": False,
                                "decisionPoint": {
                                    "upperValue": 0.0,
                                    "lowerValue": 0.0,
                                    "valueType": "Percent",
                                    "sectionsToCheck": "CurrentOnly",
                                    "outcome": None
                                }
                            }
                        ],
                        "centre": {
                            "id": 80,
                            "reference": "WTC"
                        },
                        "candidate": {
                            "id": 407,
                            "reference": "SAMPLE"
                        },
                        "mark": 0,
                        "availableMarks": 3,
                        "percentage": "",
                        "grade": "",
                        "startedDate": "2018-07-30 at 11:31:25.443",
                        "submittedDate": "2018-07-30 at 11:46:00",
                        "id": 1747,
                        "downloads": [
                            {
                                "os": "Microsoft Windows...",
                                "ipAddress": "82...",
                                "machineName": "BTL1...",
                                "dateTime": "17:13:27 Thu 07 Mar 2019",
                                "local": False,
                                "userName": "-1"
                            }
                        ]
                    }
                ],
                "errors": None,
                "serverTimeZone": "GMT Standard Time"
            }
            write_json()
    talk('This is' + questionname3)
    talk(question3)
    talk(options3)
    command = take_command()
    talk('Would you like the question repeated? Beep Boop')
    if 'yes' in command:
        talk('This is' + questionname3)
        talk(question3)
        talk(options3)
        command = take_command()
        talk('Please sate your answer. A, B, or C. Beep Boop')
        if 'A' in command: #Question 3
            candidate_response3 = 'A'
            print(command)
            aDict = {
                "count": None,
                "top": None,
                "skip": None,
                "pageCount": None,
                "nextPageLink": None,
                "prevPageLink": None,
                "response": [
                    {
                        "test": {
                            "reference": "Test 1",
                            "name": "Test 1",
                            "id": 443
                        },
                        "testForm": {
                            "reference": "Test 2",
                            "name": "Test 2",
                            "id": 518
                        },
                        "subject": {
                            "reference": "Geography",
                            "name": "Geography",
                            "id": 200
                        },
                        "passMark": 0.0,
                        "passMarkType": "Percentage",
                        "percentageMark": 31.25,
                        "passPercentage": 0.0,
                        "keycode": "test",
                        "sections": [
                            {
                                "id": 1,
                                "name": "Section",
                                "mark": 1.0,
                                "percentageMark": 33.333,
                                "availableMarks": 3,
                                "passMark": 0.0,
                                "passPercentage": 0.0,
                                "passIRTScore": 'null',
                                "passMarkType": "Percentage",
                                "items": [
                                    {
                                        "id": 101,
                                        "name1": "Question 1",
                                        "version": 2,
                                        "mark": 1.0,
                                        "awardedMark": 1.0,
                                        "availableMarks": 1,
                                        "surpassReference": "5199P6468",
                                        "nonScored": False,
                                        "type": "Question",
                                        "Question1": "What is the Capital of England",
                                        "Options1": {
                                            "A": "London",
                                            "B": "Edinburgh",
                                            "C": "Cardiff"
                                        },
                                        "correctAnswer1": "A",
                                        "candidateResponse1": {
                                            "Value1": candidate_response1
                                        },
                                        "correctlyAnswered1": "1"
                                    },
                                    {
                                        "id": 102,
                                        "name2": "Question 2",
                                        "version": 2,
                                        "mark": 0.0,
                                        "awardedMark": 0.0,
                                        "availableMarks": 1,
                                        "viewingTime": "2000",
                                        "learningOutcome": "",
                                        "markBreakdown": [],
                                        "unit": "",
                                        "surpassReference": "5199P6451",
                                        "nonScored": False,
                                        "type": "Question",
                                        "Question2": "What is the capital of Italy",
                                        "Options2": {
                                            "A": "Paris",
                                            "B": "Rome",
                                            "C": "Sydney"
                                        },
                                        "correctAnswer2": "B",
                                        "candidateResponse2": {
                                            "Value2": candidate_response2
                                        }
                                    },
                                    {
                                        "id": 103,
                                        "name3": "Question 3",
                                        "version": 2,
                                        "mark": 0.0,
                                        "awardedMark": 0.0,
                                        "availableMarks": 1,
                                        "viewingTime": "2000",
                                        "learningOutcome": "",
                                        "markBreakdown": [],
                                        "unit": "",
                                        "surpassReference": "5199P6454",
                                        "nonScored": False,
                                        "type": "Question",
                                        "Question3": "Which one of these is the correct wording for a coastal defense",
                                        "Options3": {
                                            "A": "Sea Wall",
                                            "B": "Sea Net",
                                            "C": "Moat"
                                        },
                                        "correctAnswer3": "A",
                                        "candidateResponse3": {
                                            "Value3": candidate_response3
                                        }
                                    }
                                ],
                                "sectionSelectorId": None,
                                "selected": None,
                                "startTime": None,
                                "endTime": None,
                                "isPoolTimeSection": False,
                                "poolName": None,
                                "isSurveySection": False,
                                "decisionPoint": {
                                    "upperValue": 0.0,
                                    "lowerValue": 0.0,
                                    "valueType": "Percent",
                                    "sectionsToCheck": "CurrentOnly",
                                    "outcome": None
                                }
                            }
                        ],
                        "centre": {
                            "id": 80,
                            "reference": "WTC"
                        },
                        "candidate": {
                            "id": 407,
                            "reference": "SAMPLE"
                        },
                        "mark": 0,
                        "availableMarks": 3,
                        "percentage": "",
                        "grade": "",
                        "startedDate": "2018-07-30 at 11:31:25.443",
                        "submittedDate": "2018-07-30 at 11:46:00",
                        "id": 1747,
                        "downloads": [
                            {
                                "os": "Microsoft Windows...",
                                "ipAddress": "82...",
                                "machineName": "BTL1...",
                                "dateTime": "17:13:27 Thu 07 Mar 2019",
                                "local": False,
                                "userName": "-1"
                            }
                        ]
                    }
                ],
                "errors": None,
                "serverTimeZone": "GMT Standard Time"
            }
            write_json()
        if 'B' in command:
            candidate_response3 = 'B'
            print(command)
            aDict = {
                "count": None,
                "top": None,
                "skip": None,
                "pageCount": None,
                "nextPageLink": None,
                "prevPageLink": None,
                "response": [
                    {
                        "test": {
                            "reference": "Test 1",
                            "name": "Test 1",
                            "id": 443
                        },
                        "testForm": {
                            "reference": "Test 2",
                            "name": "Test 2",
                            "id": 518
                        },
                        "subject": {
                            "reference": "Geography",
                            "name": "Geography",
                            "id": 200
                        },
                        "passMark": 0.0,
                        "passMarkType": "Percentage",
                        "percentageMark": 31.25,
                        "passPercentage": 0.0,
                        "keycode": "test",
                        "sections": [
                            {
                                "id": 1,
                                "name": "Section",
                                "mark": 1.0,
                                "percentageMark": 33.333,
                                "availableMarks": 3,
                                "passMark": 0.0,
                                "passPercentage": 0.0,
                                "passIRTScore": 'null',
                                "passMarkType": "Percentage",
                                "items": [
                                    {
                                        "id": 101,
                                        "name1": "Question 1",
                                        "version": 2,
                                        "mark": 1.0,
                                        "awardedMark": 1.0,
                                        "availableMarks": 1,
                                        "surpassReference": "5199P6468",
                                        "nonScored": False,
                                        "type": "Question",
                                        "Question1": "What is the Capital of England",
                                        "Options1": {
                                            "A": "London",
                                            "B": "Edinburgh",
                                            "C": "Cardiff"
                                        },
                                        "correctAnswer1": "A",
                                        "candidateResponse1": {
                                            "Value1": candidate_response1
                                        },
                                        "correctlyAnswered1": "1"
                                    },
                                    {
                                        "id": 102,
                                        "name2": "Question 2",
                                        "version": 2,
                                        "mark": 0.0,
                                        "awardedMark": 0.0,
                                        "availableMarks": 1,
                                        "viewingTime": "2000",
                                        "learningOutcome": "",
                                        "markBreakdown": [],
                                        "unit": "",
                                        "surpassReference": "5199P6451",
                                        "nonScored": False,
                                        "type": "Question",
                                        "Question2": "What is the capital of Italy",
                                        "Options2": {
                                            "A": "Paris",
                                            "B": "Rome",
                                            "C": "Sydney"
                                        },
                                        "correctAnswer2": "B",
                                        "candidateResponse2": {
                                            "Value2": candidate_response2
                                        }
                                    },
                                    {
                                        "id": 103,
                                        "name3": "Question 3",
                                        "version": 2,
                                        "mark": 0.0,
                                        "awardedMark": 0.0,
                                        "availableMarks": 1,
                                        "viewingTime": "2000",
                                        "learningOutcome": "",
                                        "markBreakdown": [],
                                        "unit": "",
                                        "surpassReference": "5199P6454",
                                        "nonScored": False,
                                        "type": "Question",
                                        "Question3": "Which one of these is the correct wording for a coastal defense",
                                        "Options3": {
                                            "A": "Sea Wall",
                                            "B": "Sea Net",
                                            "C": "Moat"
                                        },
                                        "correctAnswer3": "A",
                                        "candidateResponse3": {
                                            "Value3": candidate_response3
                                        }
                                    }
                                ],
                                "sectionSelectorId": None,
                                "selected": None,
                                "startTime": None,
                                "endTime": None,
                                "isPoolTimeSection": False,
                                "poolName": None,
                                "isSurveySection": False,
                                "decisionPoint": {
                                    "upperValue": 0.0,
                                    "lowerValue": 0.0,
                                    "valueType": "Percent",
                                    "sectionsToCheck": "CurrentOnly",
                                    "outcome": None
                                }
                            }
                        ],
                        "centre": {
                            "id": 80,
                            "reference": "WTC"
                        },
                        "candidate": {
                            "id": 407,
                            "reference": "SAMPLE"
                        },
                        "mark": 0,
                        "availableMarks": 3,
                        "percentage": "",
                        "grade": "",
                        "startedDate": "2018-07-30 at 11:31:25.443",
                        "submittedDate": "2018-07-30 at 11:46:00",
                        "id": 1747,
                        "downloads": [
                            {
                                "os": "Microsoft Windows...",
                                "ipAddress": "82...",
                                "machineName": "BTL1...",
                                "dateTime": "17:13:27 Thu 07 Mar 2019",
                                "local": False,
                                "userName": "-1"
                            }
                        ]
                    }
                ],
                "errors": None,
                "serverTimeZone": "GMT Standard Time"
            }
            write_json()
        if 'C' in command:
            candidate_response3 = 'C'
            print(command)
            aDict = {
                "count": None,
                "top": None,
                "skip": None,
                "pageCount": None,
                "nextPageLink": None,
                "prevPageLink": None,
                "response": [
                    {
                        "test": {
                            "reference": "Test 1",
                            "name": "Test 1",
                            "id": 443
                        },
                        "testForm": {
                            "reference": "Test 2",
                            "name": "Test 2",
                            "id": 518
                        },
                        "subject": {
                            "reference": "Geography",
                            "name": "Geography",
                            "id": 200
                        },
                        "passMark": 0.0,
                        "passMarkType": "Percentage",
                        "percentageMark": 31.25,
                        "passPercentage": 0.0,
                        "keycode": "test",
                        "sections": [
                            {
                                "id": 1,
                                "name": "Section",
                                "mark": 1.0,
                                "percentageMark": 33.333,
                                "availableMarks": 3,
                                "passMark": 0.0,
                                "passPercentage": 0.0,
                                "passIRTScore": 'null',
                                "passMarkType": "Percentage",
                                "items": [
                                    {
                                        "id": 101,
                                        "name1": "Question 1",
                                        "version": 2,
                                        "mark": 1.0,
                                        "awardedMark": 1.0,
                                        "availableMarks": 1,
                                        "surpassReference": "5199P6468",
                                        "nonScored": False,
                                        "type": "Question",
                                        "Question1": "What is the Capital of England",
                                        "Options1": {
                                            "A": "London",
                                            "B": "Edinburgh",
                                            "C": "Cardiff"
                                        },
                                        "correctAnswer1": "A",
                                        "candidateResponse1": {
                                            "Value1": candidate_response1
                                        },
                                        "correctlyAnswered1": "1"
                                    },
                                    {
                                        "id": 102,
                                        "name2": "Question 2",
                                        "version": 2,
                                        "mark": 0.0,
                                        "awardedMark": 0.0,
                                        "availableMarks": 1,
                                        "viewingTime": "2000",
                                        "learningOutcome": "",
                                        "markBreakdown": [],
                                        "unit": "",
                                        "surpassReference": "5199P6451",
                                        "nonScored": False,
                                        "type": "Question",
                                        "Question2": "What is the capital of Italy",
                                        "Options2": {
                                            "A": "Paris",
                                            "B": "Rome",
                                            "C": "Sydney"
                                        },
                                        "correctAnswer2": "B",
                                        "candidateResponse2": {
                                            "Value2": candidate_response2
                                        }
                                    },
                                    {
                                        "id": 103,
                                        "name3": "Question 3",
                                        "version": 2,
                                        "mark": 0.0,
                                        "awardedMark": 0.0,
                                        "availableMarks": 1,
                                        "viewingTime": "2000",
                                        "learningOutcome": "",
                                        "markBreakdown": [],
                                        "unit": "",
                                        "surpassReference": "5199P6454",
                                        "nonScored": False,
                                        "type": "Question",
                                        "Question3": "Which one of these is the correct wording for a coastal defense",
                                        "Options3": {
                                            "A": "Sea Wall",
                                            "B": "Sea Net",
                                            "C": "Moat"
                                        },
                                        "correctAnswer3": "A",
                                        "candidateResponse3": {
                                            "Value3": candidate_response3
                                        }
                                    }
                                ],
                                "sectionSelectorId": None,
                                "selected": None,
                                "startTime": None,
                                "endTime": None,
                                "isPoolTimeSection": False,
                                "poolName": None,
                                "isSurveySection": False,
                                "decisionPoint": {
                                    "upperValue": 0.0,
                                    "lowerValue": 0.0,
                                    "valueType": "Percent",
                                    "sectionsToCheck": "CurrentOnly",
                                    "outcome": None
                                }
                            }
                        ],
                        "centre": {
                            "id": 80,
                            "reference": "WTC"
                        },
                        "candidate": {
                            "id": 407,
                            "reference": "SAMPLE"
                        },
                        "mark": 0,
                        "availableMarks": 3,
                        "percentage": "",
                        "grade": "",
                        "startedDate": "2018-07-30 at 11:31:25.443",
                        "submittedDate": "2018-07-30 at 11:46:00",
                        "id": 1747,
                        "downloads": [
                            {
                                "os": "Microsoft Windows...",
                                "ipAddress": "82...",
                                "machineName": "BTL1...",
                                "dateTime": "17:13:27 Thu 07 Mar 2019",
                                "local": False,
                                "userName": "-1"
                            }
                        ]
                    }
                ],
                "errors": None,
                "serverTimeZone": "GMT Standard Time"
            }
            write_json()
    elif 'no' in command:
        command = take_command()
        talk('Please sate your answer. A, B, or C. Beep Boop')
        if 'A' in command: #Question 3
            candidate_response3 = 'A'
            print(command)
            aDict = {
                "count": None,
                "top": None,
                "skip": None,
                "pageCount": None,
                "nextPageLink": None,
                "prevPageLink": None,
                "response": [
                    {
                        "test": {
                            "reference": "Test 1",
                            "name": "Test 1",
                            "id": 443
                        },
                        "testForm": {
                            "reference": "Test 2",
                            "name": "Test 2",
                            "id": 518
                        },
                        "subject": {
                            "reference": "Geography",
                            "name": "Geography",
                            "id": 200
                        },
                        "passMark": 0.0,
                        "passMarkType": "Percentage",
                        "percentageMark": 31.25,
                        "passPercentage": 0.0,
                        "keycode": "test",
                        "sections": [
                            {
                                "id": 1,
                                "name": "Section",
                                "mark": 1.0,
                                "percentageMark": 33.333,
                                "availableMarks": 3,
                                "passMark": 0.0,
                                "passPercentage": 0.0,
                                "passIRTScore": 'null',
                                "passMarkType": "Percentage",
                                "items": [
                                    {
                                        "id": 101,
                                        "name1": "Question 1",
                                        "version": 2,
                                        "mark": 1.0,
                                        "awardedMark": 1.0,
                                        "availableMarks": 1,
                                        "surpassReference": "5199P6468",
                                        "nonScored": False,
                                        "type": "Question",
                                        "Question1": "What is the Capital of England",
                                        "Options1": {
                                            "A": "London",
                                            "B": "Edinburgh",
                                            "C": "Cardiff"
                                        },
                                        "correctAnswer1": "A",
                                        "candidateResponse1": {
                                            "Value1": candidate_response1
                                        },
                                        "correctlyAnswered1": "1"
                                    },
                                    {
                                        "id": 102,
                                        "name2": "Question 2",
                                        "version": 2,
                                        "mark": 0.0,
                                        "awardedMark": 0.0,
                                        "availableMarks": 1,
                                        "viewingTime": "2000",
                                        "learningOutcome": "",
                                        "markBreakdown": [],
                                        "unit": "",
                                        "surpassReference": "5199P6451",
                                        "nonScored": False,
                                        "type": "Question",
                                        "Question2": "What is the capital of Italy",
                                        "Options2": {
                                            "A": "Paris",
                                            "B": "Rome",
                                            "C": "Sydney"
                                        },
                                        "correctAnswer2": "B",
                                        "candidateResponse2": {
                                            "Value2": candidate_response2
                                        }
                                    },
                                    {
                                        "id": 103,
                                        "name3": "Question 3",
                                        "version": 2,
                                        "mark": 0.0,
                                        "awardedMark": 0.0,
                                        "availableMarks": 1,
                                        "viewingTime": "2000",
                                        "learningOutcome": "",
                                        "markBreakdown": [],
                                        "unit": "",
                                        "surpassReference": "5199P6454",
                                        "nonScored": False,
                                        "type": "Question",
                                        "Question3": "Which one of these is the correct wording for a coastal defense",
                                        "Options3": {
                                            "A": "Sea Wall",
                                            "B": "Sea Net",
                                            "C": "Moat"
                                        },
                                        "correctAnswer3": "A",
                                        "candidateResponse3": {
                                            "Value3": candidate_response3
                                        }
                                    }
                                ],
                                "sectionSelectorId": None,
                                "selected": None,
                                "startTime": None,
                                "endTime": None,
                                "isPoolTimeSection": False,
                                "poolName": None,
                                "isSurveySection": False,
                                "decisionPoint": {
                                    "upperValue": 0.0,
                                    "lowerValue": 0.0,
                                    "valueType": "Percent",
                                    "sectionsToCheck": "CurrentOnly",
                                    "outcome": None
                                }
                            }
                        ],
                        "centre": {
                            "id": 80,
                            "reference": "WTC"
                        },
                        "candidate": {
                            "id": 407,
                            "reference": "SAMPLE"
                        },
                        "mark": 0,
                        "availableMarks": 3,
                        "percentage": "",
                        "grade": "",
                        "startedDate": "2018-07-30 at 11:31:25.443",
                        "submittedDate": "2018-07-30 at 11:46:00",
                        "id": 1747,
                        "downloads": [
                            {
                                "os": "Microsoft Windows...",
                                "ipAddress": "82...",
                                "machineName": "BTL1...",
                                "dateTime": "17:13:27 Thu 07 Mar 2019",
                                "local": False,
                                "userName": "-1"
                            }
                        ]
                    }
                ],
                "errors": None,
                "serverTimeZone": "GMT Standard Time"
            }
            write_json()
        if 'B' in command:
            candidate_response3 = 'B'
            print(command)
            aDict = {
                "count": None,
                "top": None,
                "skip": None,
                "pageCount": None,
                "nextPageLink": None,
                "prevPageLink": None,
                "response": [
                    {
                        "test": {
                            "reference": "Test 1",
                            "name": "Test 1",
                            "id": 443
                        },
                        "testForm": {
                            "reference": "Test 2",
                            "name": "Test 2",
                            "id": 518
                        },
                        "subject": {
                            "reference": "Geography",
                            "name": "Geography",
                            "id": 200
                        },
                        "passMark": 0.0,
                        "passMarkType": "Percentage",
                        "percentageMark": 31.25,
                        "passPercentage": 0.0,
                        "keycode": "test",
                        "sections": [
                            {
                                "id": 1,
                                "name": "Section",
                                "mark": 1.0,
                                "percentageMark": 33.333,
                                "availableMarks": 3,
                                "passMark": 0.0,
                                "passPercentage": 0.0,
                                "passIRTScore": 'null',
                                "passMarkType": "Percentage",
                                "items": [
                                    {
                                        "id": 101,
                                        "name1": "Question 1",
                                        "version": 2,
                                        "mark": 1.0,
                                        "awardedMark": 1.0,
                                        "availableMarks": 1,
                                        "surpassReference": "5199P6468",
                                        "nonScored": False,
                                        "type": "Question",
                                        "Question1": "What is the Capital of England",
                                        "Options1": {
                                            "A": "London",
                                            "B": "Edinburgh",
                                            "C": "Cardiff"
                                        },
                                        "correctAnswer1": "A",
                                        "candidateResponse1": {
                                            "Value1": candidate_response1
                                        },
                                        "correctlyAnswered1": "1"
                                    },
                                    {
                                        "id": 102,
                                        "name2": "Question 2",
                                        "version": 2,
                                        "mark": 0.0,
                                        "awardedMark": 0.0,
                                        "availableMarks": 1,
                                        "viewingTime": "2000",
                                        "learningOutcome": "",
                                        "markBreakdown": [],
                                        "unit": "",
                                        "surpassReference": "5199P6451",
                                        "nonScored": False,
                                        "type": "Question",
                                        "Question2": "What is the capital of Italy",
                                        "Options2": {
                                            "A": "Paris",
                                            "B": "Rome",
                                            "C": "Sydney"
                                        },
                                        "correctAnswer2": "B",
                                        "candidateResponse2": {
                                            "Value2": candidate_response2
                                        }
                                    },
                                    {
                                        "id": 103,
                                        "name3": "Question 3",
                                        "version": 2,
                                        "mark": 0.0,
                                        "awardedMark": 0.0,
                                        "availableMarks": 1,
                                        "viewingTime": "2000",
                                        "learningOutcome": "",
                                        "markBreakdown": [],
                                        "unit": "",
                                        "surpassReference": "5199P6454",
                                        "nonScored": False,
                                        "type": "Question",
                                        "Question3": "Which one of these is the correct wording for a coastal defense",
                                        "Options3": {
                                            "A": "Sea Wall",
                                            "B": "Sea Net",
                                            "C": "Moat"
                                        },
                                        "correctAnswer3": "A",
                                        "candidateResponse3": {
                                            "Value3": candidate_response3
                                        }
                                    }
                                ],
                                "sectionSelectorId": None,
                                "selected": None,
                                "startTime": None,
                                "endTime": None,
                                "isPoolTimeSection": False,
                                "poolName": None,
                                "isSurveySection": False,
                                "decisionPoint": {
                                    "upperValue": 0.0,
                                    "lowerValue": 0.0,
                                    "valueType": "Percent",
                                    "sectionsToCheck": "CurrentOnly",
                                    "outcome": None
                                }
                            }
                        ],
                        "centre": {
                            "id": 80,
                            "reference": "WTC"
                        },
                        "candidate": {
                            "id": 407,
                            "reference": "SAMPLE"
                        },
                        "mark": 0,
                        "availableMarks": 3,
                        "percentage": "",
                        "grade": "",
                        "startedDate": "2018-07-30 at 11:31:25.443",
                        "submittedDate": "2018-07-30 at 11:46:00",
                        "id": 1747,
                        "downloads": [
                            {
                                "os": "Microsoft Windows...",
                                "ipAddress": "82...",
                                "machineName": "BTL1...",
                                "dateTime": "17:13:27 Thu 07 Mar 2019",
                                "local": False,
                                "userName": "-1"
                            }
                        ]
                    }
                ],
                "errors": None,
                "serverTimeZone": "GMT Standard Time"
            }
            write_json()
        if 'C' in command:
            candidate_response3 = 'C'
            print(command)
            aDict = {
                "count": None,
                "top": None,
                "skip": None,
                "pageCount": None,
                "nextPageLink": None,
                "prevPageLink": None,
                "response": [
                    {
                        "test": {
                            "reference": "Test 1",
                            "name": "Test 1",
                            "id": 443
                        },
                        "testForm": {
                            "reference": "Test 2",
                            "name": "Test 2",
                            "id": 518
                        },
                        "subject": {
                            "reference": "Geography",
                            "name": "Geography",
                            "id": 200
                        },
                        "passMark": 0.0,
                        "passMarkType": "Percentage",
                        "percentageMark": 31.25,
                        "passPercentage": 0.0,
                        "keycode": "test",
                        "sections": [
                            {
                                "id": 1,
                                "name": "Section",
                                "mark": 1.0,
                                "percentageMark": 33.333,
                                "availableMarks": 3,
                                "passMark": 0.0,
                                "passPercentage": 0.0,
                                "passIRTScore": 'null',
                                "passMarkType": "Percentage",
                                "items": [
                                    {
                                        "id": 101,
                                        "name1": "Question 1",
                                        "version": 2,
                                        "mark": 1.0,
                                        "awardedMark": 1.0,
                                        "availableMarks": 1,
                                        "surpassReference": "5199P6468",
                                        "nonScored": False,
                                        "type": "Question",
                                        "Question1": "What is the Capital of England",
                                        "Options1": {
                                            "A": "London",
                                            "B": "Edinburgh",
                                            "C": "Cardiff"
                                        },
                                        "correctAnswer1": "A",
                                        "candidateResponse1": {
                                            "Value1": candidate_response1
                                        },
                                        "correctlyAnswered1": "1"
                                    },
                                    {
                                        "id": 102,
                                        "name2": "Question 2",
                                        "version": 2,
                                        "mark": 0.0,
                                        "awardedMark": 0.0,
                                        "availableMarks": 1,
                                        "viewingTime": "2000",
                                        "learningOutcome": "",
                                        "markBreakdown": [],
                                        "unit": "",
                                        "surpassReference": "5199P6451",
                                        "nonScored": False,
                                        "type": "Question",
                                        "Question2": "What is the capital of Italy",
                                        "Options2": {
                                            "A": "Paris",
                                            "B": "Rome",
                                            "C": "Sydney"
                                        },
                                        "correctAnswer2": "B",
                                        "candidateResponse2": {
                                            "Value2": candidate_response2
                                        }
                                    },
                                    {
                                        "id": 103,
                                        "name3": "Question 3",
                                        "version": 2,
                                        "mark": 0.0,
                                        "awardedMark": 0.0,
                                        "availableMarks": 1,
                                        "viewingTime": "2000",
                                        "learningOutcome": "",
                                        "markBreakdown": [],
                                        "unit": "",
                                        "surpassReference": "5199P6454",
                                        "nonScored": False,
                                        "type": "Question",
                                        "Question3": "Which one of these is the correct wording for a coastal defense",
                                        "Options3": {
                                            "A": "Sea Wall",
                                            "B": "Sea Net",
                                            "C": "Moat"
                                        },
                                        "correctAnswer3": "A",
                                        "candidateResponse3": {
                                            "Value3": candidate_response3
                                        }
                                    }
                                ],
                                "sectionSelectorId": None,
                                "selected": None,
                                "startTime": None,
                                "endTime": None,
                                "isPoolTimeSection": False,
                                "poolName": None,
                                "isSurveySection": False,
                                "decisionPoint": {
                                    "upperValue": 0.0,
                                    "lowerValue": 0.0,
                                    "valueType": "Percent",
                                    "sectionsToCheck": "CurrentOnly",
                                    "outcome": None
                                }
                            }
                        ],
                        "centre": {
                            "id": 80,
                            "reference": "WTC"
                        },
                        "candidate": {
                            "id": 407,
                            "reference": "SAMPLE"
                        },
                        "mark": 0,
                        "availableMarks": 3,
                        "percentage": "",
                        "grade": "",
                        "startedDate": "2018-07-30 at 11:31:25.443",
                        "submittedDate": "2018-07-30 at 11:46:00",
                        "id": 1747,
                        "downloads": [
                            {
                                "os": "Microsoft Windows...",
                                "ipAddress": "82...",
                                "machineName": "BTL1...",
                                "dateTime": "17:13:27 Thu 07 Mar 2019",
                                "local": False,
                                "userName": "-1"
                            }
                        ]
                    }
                ],
                "errors": None,
                "serverTimeZone": "GMT Standard Time"
            }
            write_json()
        # opening the file

        file = open('testdata.json', )
        data = json.load(file)

        correct_answer1 = data["response"][0]["sections"][0]["items"][0]["correctAnswer1"]
        candidate_answer1 = data["response"][0]["sections"][0]["items"][0]["candidateResponse1"]["Value1"]
        correct_answer2 = data["response"][0]["sections"][0]["items"][1]["correctAnswer2"]
        candidate_answer2 = data["response"][0]["sections"][0]["items"][1]["candidateResponse2"]["Value2"]
        correct_answer3 = data["response"][0]["sections"][0]["items"][2]["correctAnswer3"]
        candidate_answer3 = data["response"][0]["sections"][0]["items"][2]["candidateResponse3"]["Value3"]

        # comparing answer1 to correct answer
        if candidate_answer1 == correct_answer1:
            aDict = {
                "count": None,
                "top": None,
                "skip": None,
                "pageCount": None,
                "nextPageLink": None,
                "prevPageLink": None,
                "response": [
                    {
                        "test": {
                            "reference": "Test 1",
                            "name": "Test 1",
                            "id": 443
                        },
                        "testForm": {
                            "reference": "Test 2",
                            "name": "Test 2",
                            "id": 518
                        },
                        "subject": {
                            "reference": "Geography",
                            "name": "Geography",
                            "id": 200
                        },
                        "passMark": 0.0,
                        "passMarkType": "Percentage",
                        "percentageMark": 31.25,
                        "passPercentage": 0.0,
                        "keycode": "test",
                        "sections": [
                            {
                                "id": 1,
                                "name": "Section",
                                "mark": 1.0,
                                "percentageMark": 33.333,
                                "availableMarks": 3,
                                "passMark": 0.0,
                                "passPercentage": 0.0,
                                "passIRTScore": 'null',
                                "passMarkType": "Percentage",
                                "items": [
                                    {
                                        "id": 101,
                                        "name1": "Question 1",
                                        "version": 2,
                                        "mark": 1.0,
                                        "awardedMark": 1.0,
                                        "availableMarks": 1,
                                        "surpassReference": "5199P6468",
                                        "nonScored": False,
                                        "type": "Question",
                                        "Question1": "What is the Capital of England",
                                        "Options1": {
                                            "A": "London",
                                            "B": "Edinburgh",
                                            "C": "Cardiff"
                                        },
                                        "correctAnswer1": "A",
                                        "candidateResponse1": {
                                            "Value1": candidate_response1
                                        },
                                        "correctlyAnswered1": "1"
                                    },
                                    {
                                        "id": 102,
                                        "name2": "Question 2",
                                        "version": 2,
                                        "mark": 0.0,
                                        "awardedMark": 0.0,
                                        "availableMarks": 1,
                                        "viewingTime": "2000",
                                        "learningOutcome": "",
                                        "markBreakdown": [],
                                        "unit": "",
                                        "surpassReference": "5199P6451",
                                        "nonScored": False,
                                        "type": "Question",
                                        "Question2": "What is the capital of Italy",
                                        "Options2": {
                                            "A": "Paris",
                                            "B": "Rome",
                                            "C": "Sydney"
                                        },
                                        "correctAnswer2": "B",
                                        "candidateResponse2": {
                                            "Value2": candidate_response2
                                        }
                                    },
                                    {
                                        "id": 103,
                                        "name3": "Question 3",
                                        "version": 2,
                                        "mark": 0.0,
                                        "awardedMark": 0.0,
                                        "availableMarks": 1,
                                        "viewingTime": "2000",
                                        "learningOutcome": "",
                                        "markBreakdown": [],
                                        "unit": "",
                                        "surpassReference": "5199P6454",
                                        "nonScored": False,
                                        "type": "Question",
                                        "Question3": "Which one of these is the correct wording for a coastal defense",
                                        "Options3": {
                                            "A": "Sea Wall",
                                            "B": "Sea Net",
                                            "C": "Moat"
                                        },
                                        "correctAnswer3": "A",
                                        "candidateResponse3": {
                                            "Value3": candidate_response3
                                        }
                                    }
                                ],
                                "sectionSelectorId": None,
                                "selected": None,
                                "startTime": None,
                                "endTime": None,
                                "isPoolTimeSection": False,
                                "poolName": None,
                                "isSurveySection": False,
                                "decisionPoint": {
                                    "upperValue": 0.0,
                                    "lowerValue": 0.0,
                                    "valueType": "Percent",
                                    "sectionsToCheck": "CurrentOnly",
                                    "outcome": None
                                }
                            }
                        ],
                        "centre": {
                            "id": 80,
                            "reference": "WTC"
                        },
                        "candidate": {
                            "id": 407,
                            "reference": "SAMPLE"
                        },
                        "mark": 0,
                        "availableMarks": 3,
                        "percentage": "",
                        "grade": "",
                        "startedDate": "2018-07-30 at 11:31:25.443",
                        "submittedDate": "2018-07-30 at 11:46:00",
                        "id": 1747,
                        "downloads": [
                            {
                                "os": "Microsoft Windows...",
                                "ipAddress": "82...",
                                "machineName": "BTL1...",
                                "dateTime": "17:13:27 Thu 07 Mar 2019",
                                "local": False,
                                "userName": "-1"
                            }
                        ]
                    }
                ],
                "errors": None,
                "serverTimeZone": "GMT Standard Time"
            }
            write_json()
            an1 = True
        else:
            aDict = {
                "count": None,
                "top": None,
                "skip": None,
                "pageCount": None,
                "nextPageLink": None,
                "prevPageLink": None,
                "response": [
                    {
                        "test": {
                            "reference": "Test 1",
                            "name": "Test 1",
                            "id": 443
                        },
                        "testForm": {
                            "reference": "Test 2",
                            "name": "Test 2",
                            "id": 518
                        },
                        "subject": {
                            "reference": "Geography",
                            "name": "Geography",
                            "id": 200
                        },
                        "passMark": 0.0,
                        "passMarkType": "Percentage",
                        "percentageMark": 31.25,
                        "passPercentage": 0.0,
                        "keycode": "test",
                        "sections": [
                            {
                                "id": 1,
                                "name": "Section",
                                "mark": 1.0,
                                "percentageMark": 33.333,
                                "availableMarks": 3,
                                "passMark": 0.0,
                                "passPercentage": 0.0,
                                "passIRTScore": 'null',
                                "passMarkType": "Percentage",
                                "items": [
                                    {
                                        "id": 101,
                                        "name1": "Question 1",
                                        "version": 2,
                                        "mark": 1.0,
                                        "awardedMark": 1.0,
                                        "availableMarks": 1,
                                        "surpassReference": "5199P6468",
                                        "nonScored": False,
                                        "type": "Question",
                                        "Question1": "What is the Capital of England",
                                        "Options1": {
                                            "A": "London",
                                            "B": "Edinburgh",
                                            "C": "Cardiff"
                                        },
                                        "correctAnswer1": "A",
                                        "candidateResponse1": {
                                            "Value1": candidate_response1
                                        },
                                        "correctlyAnswered1": "0"
                                    },
                                    {
                                        "id": 102,
                                        "name2": "Question 2",
                                        "version": 2,
                                        "mark": 0.0,
                                        "awardedMark": 0.0,
                                        "availableMarks": 1,
                                        "viewingTime": "2000",
                                        "learningOutcome": "",
                                        "markBreakdown": [],
                                        "unit": "",
                                        "surpassReference": "5199P6451",
                                        "nonScored": False,
                                        "type": "Question",
                                        "Question2": "What is the capital of Italy",
                                        "Options2": {
                                            "A": "Paris",
                                            "B": "Rome",
                                            "C": "Sydney"
                                        },
                                        "correctAnswer2": "B",
                                        "candidateResponse2": {
                                            "Value2": candidate_response2
                                        }
                                    },
                                    {
                                        "id": 103,
                                        "name3": "Question 3",
                                        "version": 2,
                                        "mark": 0.0,
                                        "awardedMark": 0.0,
                                        "availableMarks": 1,
                                        "viewingTime": "2000",
                                        "learningOutcome": "",
                                        "markBreakdown": [],
                                        "unit": "",
                                        "surpassReference": "5199P6454",
                                        "nonScored": False,
                                        "type": "Question",
                                        "Question3": "Which one of these is the correct wording for a coastal defense",
                                        "Options3": {
                                            "A": "Sea Wall",
                                            "B": "Sea Net",
                                            "C": "Moat"
                                        },
                                        "correctAnswer3": "A",
                                        "candidateResponse3": {
                                            "Value3": candidate_response3
                                        }
                                    }
                                ],
                                "sectionSelectorId": None,
                                "selected": None,
                                "startTime": None,
                                "endTime": None,
                                "isPoolTimeSection": False,
                                "poolName": None,
                                "isSurveySection": False,
                                "decisionPoint": {
                                    "upperValue": 0.0,
                                    "lowerValue": 0.0,
                                    "valueType": "Percent",
                                    "sectionsToCheck": "CurrentOnly",
                                    "outcome": None
                                }
                            }
                        ],
                        "centre": {
                            "id": 80,
                            "reference": "WTC"
                        },
                        "candidate": {
                            "id": 407,
                            "reference": "SAMPLE"
                        },
                        "mark": 0,
                        "availableMarks": 3,
                        "percentage": "",
                        "grade": "",
                        "startedDate": "2018-07-30 at 11:31:25.443",
                        "submittedDate": "2018-07-30 at 11:46:00",
                        "id": 1747,
                        "downloads": [
                            {
                                "os": "Microsoft Windows...",
                                "ipAddress": "82...",
                                "machineName": "BTL1...",
                                "dateTime": "17:13:27 Thu 07 Mar 2019",
                                "local": False,
                                "userName": "-1"
                            }
                        ]
                    }
                ],
                "errors": None,
                "serverTimeZone": "GMT Standard Time"
            }
            write_json()
            an1 = False
        # comparing answer 2 to correct answer
        if candidate_answer2 == correct_answer2:
            if an1 == True:
                aDict = {
                    "count": None,
                    "top": None,
                    "skip": None,
                    "pageCount": None,
                    "nextPageLink": None,
                    "prevPageLink": None,
                    "response": [
                        {
                            "test": {
                                "reference": "Test 1",
                                "name": "Test 1",
                                "id": 443
                            },
                            "testForm": {
                                "reference": "Test 2",
                                "name": "Test 2",
                                "id": 518
                            },
                            "subject": {
                                "reference": "Geography",
                                "name": "Geography",
                                "id": 200
                            },
                            "passMark": 0.0,
                            "passMarkType": "Percentage",
                            "percentageMark": 31.25,
                            "passPercentage": 0.0,
                            "keycode": "test",
                            "sections": [
                                {
                                    "id": 1,
                                    "name": "Section",
                                    "mark": 1.0,
                                    "percentageMark": 33.333,
                                    "availableMarks": 3,
                                    "passMark": 0.0,
                                    "passPercentage": 0.0,
                                    "passIRTScore": 'null',
                                    "passMarkType": "Percentage",
                                    "items": [
                                        {
                                            "id": 101,
                                            "name1": "Question 1",
                                            "version": 2,
                                            "mark": 1.0,
                                            "awardedMark": 1.0,
                                            "availableMarks": 1,
                                            "surpassReference": "5199P6468",
                                            "nonScored": False,
                                            "type": "Question",
                                            "Question1": "What is the Capital of England",
                                            "Options1": {
                                                "A": "London",
                                                "B": "Edinburgh",
                                                "C": "Cardiff"
                                            },
                                            "correctAnswer1": "A",
                                            "candidateResponse1": {
                                                "Value1": candidate_response1
                                            },
                                            "correctlyAnswered1": "1"
                                        },
                                        {
                                            "id": 102,
                                            "name2": "Question 2",
                                            "version": 2,
                                            "mark": 0.0,
                                            "awardedMark": 0.0,
                                            "availableMarks": 1,
                                            "viewingTime": "2000",
                                            "learningOutcome": "",
                                            "markBreakdown": [],
                                            "unit": "",
                                            "surpassReference": "5199P6451",
                                            "nonScored": False,
                                            "type": "Question",
                                            "Question2": "What is the capital of Italy",
                                            "Options2": {
                                                "A": "Paris",
                                                "B": "Rome",
                                                "C": "Sydney"
                                            },
                                            "correctAnswer2": "B",
                                            "candidateResponse2": {
                                                "Value2": candidate_response2
                                            },
                                            "correctlyAnswered2": "1"
                                        },
                                        {
                                            "id": 103,
                                            "name3": "Question 3",
                                            "version": 2,
                                            "mark": 0.0,
                                            "awardedMark": 0.0,
                                            "availableMarks": 1,
                                            "viewingTime": "2000",
                                            "learningOutcome": "",
                                            "markBreakdown": [],
                                            "unit": "",
                                            "surpassReference": "5199P6454",
                                            "nonScored": False,
                                            "type": "Question",
                                            "Question3": "Which one of these is the correct wording for a coastal defense",
                                            "Options3": {
                                                "A": "Sea Wall",
                                                "B": "Sea Net",
                                                "C": "Moat"
                                            },
                                            "correctAnswer3": "A",
                                            "candidateResponse3": {
                                                "Value3": candidate_response3
                                            }
                                        }
                                    ],
                                    "sectionSelectorId": None,
                                    "selected": None,
                                    "startTime": None,
                                    "endTime": None,
                                    "isPoolTimeSection": False,
                                    "poolName": None,
                                    "isSurveySection": False,
                                    "decisionPoint": {
                                        "upperValue": 0.0,
                                        "lowerValue": 0.0,
                                        "valueType": "Percent",
                                        "sectionsToCheck": "CurrentOnly",
                                        "outcome": None
                                    }
                                }
                            ],
                            "centre": {
                                "id": 80,
                                "reference": "WTC"
                            },
                            "candidate": {
                                "id": 407,
                                "reference": "SAMPLE"
                            },
                            "mark": 0,
                            "availableMarks": 3,
                            "percentage": "",
                            "grade": "",
                            "startedDate": "2018-07-30 at 11:31:25.443",
                            "submittedDate": "2018-07-30 at 11:46:00",
                            "id": 1747,
                            "downloads": [
                                {
                                    "os": "Microsoft Windows...",
                                    "ipAddress": "82...",
                                    "machineName": "BTL1...",
                                    "dateTime": "17:13:27 Thu 07 Mar 2019",
                                    "local": False,
                                    "userName": "-1"
                                }
                            ]
                        }
                    ],
                    "errors": None,
                    "serverTimeZone": "GMT Standard Time"
                }
                write_json()
                an2 = True
            else:
                aDict = {
                    "count": None,
                    "top": None,
                    "skip": None,
                    "pageCount": None,
                    "nextPageLink": None,
                    "prevPageLink": None,
                    "response": [
                        {
                            "test": {
                                "reference": "Test 1",
                                "name": "Test 1",
                                "id": 443
                            },
                            "testForm": {
                                "reference": "Test 2",
                                "name": "Test 2",
                                "id": 518
                            },
                            "subject": {
                                "reference": "Geography",
                                "name": "Geography",
                                "id": 200
                            },
                            "passMark": 0.0,
                            "passMarkType": "Percentage",
                            "percentageMark": 31.25,
                            "passPercentage": 0.0,
                            "keycode": "test",
                            "sections": [
                                {
                                    "id": 1,
                                    "name": "Section",
                                    "mark": 1.0,
                                    "percentageMark": 33.333,
                                    "availableMarks": 3,
                                    "passMark": 0.0,
                                    "passPercentage": 0.0,
                                    "passIRTScore": 'null',
                                    "passMarkType": "Percentage",
                                    "items": [
                                        {
                                            "id": 101,
                                            "name1": "Question 1",
                                            "version": 2,
                                            "mark": 1.0,
                                            "awardedMark": 1.0,
                                            "availableMarks": 1,
                                            "surpassReference": "5199P6468",
                                            "nonScored": False,
                                            "type": "Question",
                                            "Question1": "What is the Capital of England",
                                            "Options1": {
                                                "A": "London",
                                                "B": "Edinburgh",
                                                "C": "Cardiff"
                                            },
                                            "correctAnswer1": "A",
                                            "candidateResponse1": {
                                                "Value1": candidate_response1
                                            },
                                            "correctlyAnswered1": "0"
                                        },
                                        {
                                            "id": 102,
                                            "name2": "Question 2",
                                            "version": 2,
                                            "mark": 0.0,
                                            "awardedMark": 0.0,
                                            "availableMarks": 1,
                                            "viewingTime": "2000",
                                            "learningOutcome": "",
                                            "markBreakdown": [],
                                            "unit": "",
                                            "surpassReference": "5199P6451",
                                            "nonScored": False,
                                            "type": "Question",
                                            "Question2": "What is the capital of Italy",
                                            "Options2": {
                                                "A": "Paris",
                                                "B": "Rome",
                                                "C": "Sydney"
                                            },
                                            "correctAnswer2": "B",
                                            "candidateResponse2": {
                                                "Value2": candidate_response2
                                            },
                                            "correctlyAnswered2": "1"
                                        },
                                        {
                                            "id": 103,
                                            "name3": "Question 3",
                                            "version": 2,
                                            "mark": 0.0,
                                            "awardedMark": 0.0,
                                            "availableMarks": 1,
                                            "viewingTime": "2000",
                                            "learningOutcome": "",
                                            "markBreakdown": [],
                                            "unit": "",
                                            "surpassReference": "5199P6454",
                                            "nonScored": False,
                                            "type": "Question",
                                            "Question3": "Which one of these is the correct wording for a coastal defense",
                                            "Options3": {
                                                "A": "Sea Wall",
                                                "B": "Sea Net",
                                                "C": "Moat"
                                            },
                                            "correctAnswer3": "A",
                                            "candidateResponse3": {
                                                "Value3": candidate_response3
                                            }
                                        }
                                    ],
                                    "sectionSelectorId": None,
                                    "selected": None,
                                    "startTime": None,
                                    "endTime": None,
                                    "isPoolTimeSection": False,
                                    "poolName": None,
                                    "isSurveySection": False,
                                    "decisionPoint": {
                                        "upperValue": 0.0,
                                        "lowerValue": 0.0,
                                        "valueType": "Percent",
                                        "sectionsToCheck": "CurrentOnly",
                                        "outcome": None
                                    }
                                }
                            ],
                            "centre": {
                                "id": 80,
                                "reference": "WTC"
                            },
                            "candidate": {
                                "id": 407,
                                "reference": "SAMPLE"
                            },
                            "mark": 0,
                            "availableMarks": 3,
                            "percentage": "",
                            "grade": "",
                            "startedDate": "2018-07-30 at 11:31:25.443",
                            "submittedDate": "2018-07-30 at 11:46:00",
                            "id": 1747,
                            "downloads": [
                                {
                                    "os": "Microsoft Windows...",
                                    "ipAddress": "82...",
                                    "machineName": "BTL1...",
                                    "dateTime": "17:13:27 Thu 07 Mar 2019",
                                    "local": False,
                                    "userName": "-1"
                                }
                            ]
                        }
                    ],
                    "errors": None,
                    "serverTimeZone": "GMT Standard Time"
                }
                write_json()
                an2 = True
        else:
            if an1 == True:
                aDict = {
                    "count": None,
                    "top": None,
                    "skip": None,
                    "pageCount": None,
                    "nextPageLink": None,
                    "prevPageLink": None,
                    "response": [
                        {
                            "test": {
                                "reference": "Test 1",
                                "name": "Test 1",
                                "id": 443
                            },
                            "testForm": {
                                "reference": "Test 2",
                                "name": "Test 2",
                                "id": 518
                            },
                            "subject": {
                                "reference": "Geography",
                                "name": "Geography",
                                "id": 200
                            },
                            "passMark": 0.0,
                            "passMarkType": "Percentage",
                            "percentageMark": 31.25,
                            "passPercentage": 0.0,
                            "keycode": "test",
                            "sections": [
                                {
                                    "id": 1,
                                    "name": "Section",
                                    "mark": 1.0,
                                    "percentageMark": 33.333,
                                    "availableMarks": 3,
                                    "passMark": 0.0,
                                    "passPercentage": 0.0,
                                    "passIRTScore": 'null',
                                    "passMarkType": "Percentage",
                                    "items": [
                                        {
                                            "id": 101,
                                            "name1": "Question 1",
                                            "version": 2,
                                            "mark": 1.0,
                                            "awardedMark": 1.0,
                                            "availableMarks": 1,
                                            "surpassReference": "5199P6468",
                                            "nonScored": False,
                                            "type": "Question",
                                            "Question1": "What is the Capital of England",
                                            "Options1": {
                                                "A": "London",
                                                "B": "Edinburgh",
                                                "C": "Cardiff"
                                            },
                                            "correctAnswer1": "A",
                                            "candidateResponse1": {
                                                "Value1": candidate_response1
                                            },
                                            "correctlyAnswered1": "1"
                                        },
                                        {
                                            "id": 102,
                                            "name2": "Question 2",
                                            "version": 2,
                                            "mark": 0.0,
                                            "awardedMark": 0.0,
                                            "availableMarks": 1,
                                            "viewingTime": "2000",
                                            "learningOutcome": "",
                                            "markBreakdown": [],
                                            "unit": "",
                                            "surpassReference": "5199P6451",
                                            "nonScored": False,
                                            "type": "Question",
                                            "Question2": "What is the capital of Italy",
                                            "Options2": {
                                                "A": "Paris",
                                                "B": "Rome",
                                                "C": "Sydney"
                                            },
                                            "correctAnswer2": "B",
                                            "candidateResponse2": {
                                                "Value2": candidate_response2
                                            },
                                            "correctlyAnswered2": "0"
                                        },
                                        {
                                            "id": 103,
                                            "name3": "Question 3",
                                            "version": 2,
                                            "mark": 0.0,
                                            "awardedMark": 0.0,
                                            "availableMarks": 1,
                                            "viewingTime": "2000",
                                            "learningOutcome": "",
                                            "markBreakdown": [],
                                            "unit": "",
                                            "surpassReference": "5199P6454",
                                            "nonScored": False,
                                            "type": "Question",
                                            "Question3": "Which one of these is the correct wording for a coastal defense",
                                            "Options3": {
                                                "A": "Sea Wall",
                                                "B": "Sea Net",
                                                "C": "Moat"
                                            },
                                            "correctAnswer3": "A",
                                            "candidateResponse3": {
                                                "Value3": candidate_response3
                                            }
                                        }
                                    ],
                                    "sectionSelectorId": None,
                                    "selected": None,
                                    "startTime": None,
                                    "endTime": None,
                                    "isPoolTimeSection": False,
                                    "poolName": None,
                                    "isSurveySection": False,
                                    "decisionPoint": {
                                        "upperValue": 0.0,
                                        "lowerValue": 0.0,
                                        "valueType": "Percent",
                                        "sectionsToCheck": "CurrentOnly",
                                        "outcome": None
                                    }
                                }
                            ],
                            "centre": {
                                "id": 80,
                                "reference": "WTC"
                            },
                            "candidate": {
                                "id": 407,
                                "reference": "SAMPLE"
                            },
                            "mark": 0,
                            "availableMarks": 3,
                            "percentage": "",
                            "grade": "",
                            "startedDate": "2018-07-30 at 11:31:25.443",
                            "submittedDate": "2018-07-30 at 11:46:00",
                            "id": 1747,
                            "downloads": [
                                {
                                    "os": "Microsoft Windows...",
                                    "ipAddress": "82...",
                                    "machineName": "BTL1...",
                                    "dateTime": "17:13:27 Thu 07 Mar 2019",
                                    "local": False,
                                    "userName": "-1"
                                }
                            ]
                        }
                    ],
                    "errors": None,
                    "serverTimeZone": "GMT Standard Time"
                }
                write_json()
                an2 = False
            else:
                aDict = {
                    "count": None,
                    "top": None,
                    "skip": None,
                    "pageCount": None,
                    "nextPageLink": None,
                    "prevPageLink": None,
                    "response": [
                        {
                            "test": {
                                "reference": "Test 1",
                                "name": "Test 1",
                                "id": 443
                            },
                            "testForm": {
                                "reference": "Test 2",
                                "name": "Test 2",
                                "id": 518
                            },
                            "subject": {
                                "reference": "Geography",
                                "name": "Geography",
                                "id": 200
                            },
                            "passMark": 0.0,
                            "passMarkType": "Percentage",
                            "percentageMark": 31.25,
                            "passPercentage": 0.0,
                            "keycode": "test",
                            "sections": [
                                {
                                    "id": 1,
                                    "name": "Section",
                                    "mark": 1.0,
                                    "percentageMark": 33.333,
                                    "availableMarks": 3,
                                    "passMark": 0.0,
                                    "passPercentage": 0.0,
                                    "passIRTScore": 'null',
                                    "passMarkType": "Percentage",
                                    "items": [
                                        {
                                            "id": 101,
                                            "name1": "Question 1",
                                            "version": 2,
                                            "mark": 1.0,
                                            "awardedMark": 1.0,
                                            "availableMarks": 1,
                                            "surpassReference": "5199P6468",
                                            "nonScored": False,
                                            "type": "Question",
                                            "Question1": "What is the Capital of England",
                                            "Options1": {
                                                "A": "London",
                                                "B": "Edinburgh",
                                                "C": "Cardiff"
                                            },
                                            "correctAnswer1": "A",
                                            "candidateResponse1": {
                                                "Value1": candidate_response1
                                            },
                                            "correctlyAnswered1": "0"
                                        },
                                        {
                                            "id": 102,
                                            "name2": "Question 2",
                                            "version": 2,
                                            "mark": 0.0,
                                            "awardedMark": 0.0,
                                            "availableMarks": 1,
                                            "viewingTime": "2000",
                                            "learningOutcome": "",
                                            "markBreakdown": [],
                                            "unit": "",
                                            "surpassReference": "5199P6451",
                                            "nonScored": False,
                                            "type": "Question",
                                            "Question2": "What is the capital of Italy",
                                            "Options2": {
                                                "A": "Paris",
                                                "B": "Rome",
                                                "C": "Sydney"
                                            },
                                            "correctAnswer2": "B",
                                            "candidateResponse2": {
                                                "Value2": candidate_response2
                                            },
                                            "correctlyAnswered2": "0"
                                        },
                                        {
                                            "id": 103,
                                            "name3": "Question 3",
                                            "version": 2,
                                            "mark": 0.0,
                                            "awardedMark": 0.0,
                                            "availableMarks": 1,
                                            "viewingTime": "2000",
                                            "learningOutcome": "",
                                            "markBreakdown": [],
                                            "unit": "",
                                            "surpassReference": "5199P6454",
                                            "nonScored": False,
                                            "type": "Question",
                                            "Question3": "Which one of these is the correct wording for a coastal defense",
                                            "Options3": {
                                                "A": "Sea Wall",
                                                "B": "Sea Net",
                                                "C": "Moat"
                                            },
                                            "correctAnswer3": "A",
                                            "candidateResponse3": {
                                                "Value3": candidate_response3
                                            }
                                        }
                                    ],
                                    "sectionSelectorId": None,
                                    "selected": None,
                                    "startTime": None,
                                    "endTime": None,
                                    "isPoolTimeSection": False,
                                    "poolName": None,
                                    "isSurveySection": False,
                                    "decisionPoint": {
                                        "upperValue": 0.0,
                                        "lowerValue": 0.0,
                                        "valueType": "Percent",
                                        "sectionsToCheck": "CurrentOnly",
                                        "outcome": None
                                    }
                                }
                            ],
                            "centre": {
                                "id": 80,
                                "reference": "WTC"
                            },
                            "candidate": {
                                "id": 407,
                                "reference": "SAMPLE"
                            },
                            "mark": 0,
                            "availableMarks": 3,
                            "percentage": "",
                            "grade": "",
                            "startedDate": "2018-07-30 at 11:31:25.443",
                            "submittedDate": "2018-07-30 at 11:46:00",
                            "id": 1747,
                            "downloads": [
                                {
                                    "os": "Microsoft Windows...",
                                    "ipAddress": "82...",
                                    "machineName": "BTL1...",
                                    "dateTime": "17:13:27 Thu 07 Mar 2019",
                                    "local": False,
                                    "userName": "-1"
                                }
                            ]
                        }
                    ],
                    "errors": None,
                    "serverTimeZone": "GMT Standard Time"
                }
                write_json()
                an2 = False

        # comparing answer 3 to correct answer
        if candidate_answer3 == correct_answer3:
            check1 = data["response"][0]["sections"][0]["items"][0]["correctlyAnswered1"]
            check2 = data["response"][0]["sections"][0]["items"][1]["correctlyAnswered2"]
            if an2 == True and an1 == True:
                aDict = {
                    "count": None,
                    "top": None,
                    "skip": None,
                    "pageCount": None,
                    "nextPageLink": None,
                    "prevPageLink": None,
                    "response": [
                        {
                            "test": {
                                "reference": "Test 1",
                                "name": "Test 1",
                                "id": 443
                            },
                            "testForm": {
                                "reference": "Test 2",
                                "name": "Test 2",
                                "id": 518
                            },
                            "subject": {
                                "reference": "Geography",
                                "name": "Geography",
                                "id": 200
                            },
                            "passMark": 0.0,
                            "passMarkType": "Percentage",
                            "percentageMark": 31.25,
                            "passPercentage": 0.0,
                            "keycode": "test",
                            "sections": [
                                {
                                    "id": 1,
                                    "name": "Section",
                                    "mark": 1.0,
                                    "percentageMark": 33.333,
                                    "availableMarks": 3,
                                    "passMark": 0.0,
                                    "passPercentage": 0.0,
                                    "passIRTScore": 'null',
                                    "passMarkType": "Percentage",
                                    "items": [
                                        {
                                            "id": 101,
                                            "name1": "Question 1",
                                            "version": 2,
                                            "mark": 1.0,
                                            "awardedMark": 1.0,
                                            "availableMarks": 1,
                                            "surpassReference": "5199P6468",
                                            "nonScored": False,
                                            "type": "Question",
                                            "Question1": "What is the Capital of England",
                                            "Options1": {
                                                "A": "London",
                                                "B": "Edinburgh",
                                                "C": "Cardiff"
                                            },
                                            "correctAnswer1": "A",
                                            "candidateResponse1": {
                                                "Value1": candidate_response1
                                            },
                                            "correctlyAnswered1": "1"
                                        },
                                        {
                                            "id": 102,
                                            "name2": "Question 2",
                                            "version": 2,
                                            "mark": 0.0,
                                            "awardedMark": 0.0,
                                            "availableMarks": 1,
                                            "viewingTime": "2000",
                                            "learningOutcome": "",
                                            "markBreakdown": [],
                                            "unit": "",
                                            "surpassReference": "5199P6451",
                                            "nonScored": False,
                                            "type": "Question",
                                            "Question2": "What is the capital of Italy",
                                            "Options2": {
                                                "A": "Paris",
                                                "B": "Rome",
                                                "C": "Sydney"
                                            },
                                            "correctAnswer2": "B",
                                            "candidateResponse2": {
                                                "Value2": candidate_response2
                                            },
                                            "correctlyAnswered2": "1"
                                        },
                                        {
                                            "id": 103,
                                            "name3": "Question 3",
                                            "version": 2,
                                            "mark": 0.0,
                                            "awardedMark": 0.0,
                                            "availableMarks": 1,
                                            "viewingTime": "2000",
                                            "learningOutcome": "",
                                            "markBreakdown": [],
                                            "unit": "",
                                            "surpassReference": "5199P6454",
                                            "nonScored": False,
                                            "type": "Question",
                                            "Question3": "Which one of these is the correct wording for a coastal defense",
                                            "Options3": {
                                                "A": "Sea Wall",
                                                "B": "Sea Net",
                                                "C": "Moat"
                                            },
                                            "correctAnswer3": "A",
                                            "candidateResponse3": {
                                                "Value3": candidate_response3
                                            },
                                            "correctlyAnswered3": "1"
                                        }
                                    ],
                                    "sectionSelectorId": None,
                                    "selected": None,
                                    "startTime": None,
                                    "endTime": None,
                                    "isPoolTimeSection": False,
                                    "poolName": None,
                                    "isSurveySection": False,
                                    "decisionPoint": {
                                        "upperValue": 0.0,
                                        "lowerValue": 0.0,
                                        "valueType": "Percent",
                                        "sectionsToCheck": "CurrentOnly",
                                        "outcome": None
                                    }
                                }
                            ],
                            "centre": {
                                "id": 80,
                                "reference": "WTC"
                            },
                            "candidate": {
                                "id": 407,
                                "reference": "SAMPLE"
                            },
                            "mark": 0,
                            "availableMarks": 3,
                            "percentage": "",
                            "grade": "",
                            "startedDate": "2018-07-30 at 11:31:25.443",
                            "submittedDate": "2018-07-30 at 11:46:00",
                            "id": 1747,
                            "downloads": [
                                {
                                    "os": "Microsoft Windows...",
                                    "ipAddress": "82...",
                                    "machineName": "BTL1...",
                                    "dateTime": "17:13:27 Thu 07 Mar 2019",
                                    "local": False,
                                    "userName": "-1"
                                }
                            ]
                        }
                    ],
                    "errors": None,
                    "serverTimeZone": "GMT Standard Time"
                }
                write_json()
            elif an1 == True and an2 == False:
                aDict = {
                    "count": None,
                    "top": None,
                    "skip": None,
                    "pageCount": None,
                    "nextPageLink": None,
                    "prevPageLink": None,
                    "response": [
                        {
                            "test": {
                                "reference": "Test 1",
                                "name": "Test 1",
                                "id": 443
                            },
                            "testForm": {
                                "reference": "Test 2",
                                "name": "Test 2",
                                "id": 518
                            },
                            "subject": {
                                "reference": "Geography",
                                "name": "Geography",
                                "id": 200
                            },
                            "passMark": 0.0,
                            "passMarkType": "Percentage",
                            "percentageMark": 31.25,
                            "passPercentage": 0.0,
                            "keycode": "test",
                            "sections": [
                                {
                                    "id": 1,
                                    "name": "Section",
                                    "mark": 1.0,
                                    "percentageMark": 33.333,
                                    "availableMarks": 3,
                                    "passMark": 0.0,
                                    "passPercentage": 0.0,
                                    "passIRTScore": 'null',
                                    "passMarkType": "Percentage",
                                    "items": [
                                        {
                                            "id": 101,
                                            "name1": "Question 1",
                                            "version": 2,
                                            "mark": 1.0,
                                            "awardedMark": 1.0,
                                            "availableMarks": 1,
                                            "surpassReference": "5199P6468",
                                            "nonScored": False,
                                            "type": "Question",
                                            "Question1": "What is the Capital of England",
                                            "Options1": {
                                                "A": "London",
                                                "B": "Edinburgh",
                                                "C": "Cardiff"
                                            },
                                            "correctAnswer1": "A",
                                            "candidateResponse1": {
                                                "Value1": candidate_response1
                                            },
                                            "correctlyAnswered1": "1"
                                        },
                                        {
                                            "id": 102,
                                            "name2": "Question 2",
                                            "version": 2,
                                            "mark": 0.0,
                                            "awardedMark": 0.0,
                                            "availableMarks": 1,
                                            "viewingTime": "2000",
                                            "learningOutcome": "",
                                            "markBreakdown": [],
                                            "unit": "",
                                            "surpassReference": "5199P6451",
                                            "nonScored": False,
                                            "type": "Question",
                                            "Question2": "What is the capital of Italy",
                                            "Options2": {
                                                "A": "Paris",
                                                "B": "Rome",
                                                "C": "Sydney"
                                            },
                                            "correctAnswer2": "B",
                                            "candidateResponse2": {
                                                "Value2": candidate_response2
                                            },
                                            "correctlyAnswered2": "0"
                                        },
                                        {
                                            "id": 103,
                                            "name3": "Question 3",
                                            "version": 2,
                                            "mark": 0.0,
                                            "awardedMark": 0.0,
                                            "availableMarks": 1,
                                            "viewingTime": "2000",
                                            "learningOutcome": "",
                                            "markBreakdown": [],
                                            "unit": "",
                                            "surpassReference": "5199P6454",
                                            "nonScored": False,
                                            "type": "Question",
                                            "Question3": "Which one of these is the correct wording for a coastal defense",
                                            "Options3": {
                                                "A": "Sea Wall",
                                                "B": "Sea Net",
                                                "C": "Moat"
                                            },
                                            "correctAnswer3": "A",
                                            "candidateResponse3": {
                                                "Value3": candidate_response3
                                            },
                                            "correctlyAnswered3": "1"
                                        }
                                    ],
                                    "sectionSelectorId": None,
                                    "selected": None,
                                    "startTime": None,
                                    "endTime": None,
                                    "isPoolTimeSection": False,
                                    "poolName": None,
                                    "isSurveySection": False,
                                    "decisionPoint": {
                                        "upperValue": 0.0,
                                        "lowerValue": 0.0,
                                        "valueType": "Percent",
                                        "sectionsToCheck": "CurrentOnly",
                                        "outcome": None
                                    }
                                }
                            ],
                            "centre": {
                                "id": 80,
                                "reference": "WTC"
                            },
                            "candidate": {
                                "id": 407,
                                "reference": "SAMPLE"
                            },
                            "mark": 0,
                            "availableMarks": 3,
                            "percentage": "",
                            "grade": "",
                            "startedDate": "2018-07-30 at 11:31:25.443",
                            "submittedDate": "2018-07-30 at 11:46:00",
                            "id": 1747,
                            "downloads": [
                                {
                                    "os": "Microsoft Windows...",
                                    "ipAddress": "82...",
                                    "machineName": "BTL1...",
                                    "dateTime": "17:13:27 Thu 07 Mar 2019",
                                    "local": False,
                                    "userName": "-1"
                                }
                            ]
                        }
                    ],
                    "errors": None,
                    "serverTimeZone": "GMT Standard Time"
                }
                write_json()
            elif an1 == False and an2 == False:
                aDict = {
                    "count": None,
                    "top": None,
                    "skip": None,
                    "pageCount": None,
                    "nextPageLink": None,
                    "prevPageLink": None,
                    "response": [
                        {
                            "test": {
                                "reference": "Test 1",
                                "name": "Test 1",
                                "id": 443
                            },
                            "testForm": {
                                "reference": "Test 2",
                                "name": "Test 2",
                                "id": 518
                            },
                            "subject": {
                                "reference": "Geography",
                                "name": "Geography",
                                "id": 200
                            },
                            "passMark": 0.0,
                            "passMarkType": "Percentage",
                            "percentageMark": 31.25,
                            "passPercentage": 0.0,
                            "keycode": "test",
                            "sections": [
                                {
                                    "id": 1,
                                    "name": "Section",
                                    "mark": 1.0,
                                    "percentageMark": 33.333,
                                    "availableMarks": 3,
                                    "passMark": 0.0,
                                    "passPercentage": 0.0,
                                    "passIRTScore": 'null',
                                    "passMarkType": "Percentage",
                                    "items": [
                                        {
                                            "id": 101,
                                            "name1": "Question 1",
                                            "version": 2,
                                            "mark": 1.0,
                                            "awardedMark": 1.0,
                                            "availableMarks": 1,
                                            "surpassReference": "5199P6468",
                                            "nonScored": False,
                                            "type": "Question",
                                            "Question1": "What is the Capital of England",
                                            "Options1": {
                                                "A": "London",
                                                "B": "Edinburgh",
                                                "C": "Cardiff"
                                            },
                                            "correctAnswer1": "A",
                                            "candidateResponse1": {
                                                "Value1": candidate_response1
                                            },
                                            "correctlyAnswered1": "0"
                                        },
                                        {
                                            "id": 102,
                                            "name2": "Question 2",
                                            "version": 2,
                                            "mark": 0.0,
                                            "awardedMark": 0.0,
                                            "availableMarks": 1,
                                            "viewingTime": "2000",
                                            "learningOutcome": "",
                                            "markBreakdown": [],
                                            "unit": "",
                                            "surpassReference": "5199P6451",
                                            "nonScored": False,
                                            "type": "Question",
                                            "Question2": "What is the capital of Italy",
                                            "Options2": {
                                                "A": "Paris",
                                                "B": "Rome",
                                                "C": "Sydney"
                                            },
                                            "correctAnswer2": "B",
                                            "candidateResponse2": {
                                                "Value2": candidate_response2
                                            },
                                            "correctlyAnswered2": "1"
                                        },
                                        {
                                            "id": 103,
                                            "name3": "Question 3",
                                            "version": 2,
                                            "mark": 0.0,
                                            "awardedMark": 0.0,
                                            "availableMarks": 1,
                                            "viewingTime": "2000",
                                            "learningOutcome": "",
                                            "markBreakdown": [],
                                            "unit": "",
                                            "surpassReference": "5199P6454",
                                            "nonScored": False,
                                            "type": "Question",
                                            "Question3": "Which one of these is the correct wording for a coastal defense",
                                            "Options3": {
                                                "A": "Sea Wall",
                                                "B": "Sea Net",
                                                "C": "Moat"
                                            },
                                            "correctAnswer3": "A",
                                            "candidateResponse3": {
                                                "Value3": candidate_response3
                                            },
                                            "correctlyAnswered3": "1"
                                        }
                                    ],
                                    "sectionSelectorId": None,
                                    "selected": None,
                                    "startTime": None,
                                    "endTime": None,
                                    "isPoolTimeSection": False,
                                    "poolName": None,
                                    "isSurveySection": False,
                                    "decisionPoint": {
                                        "upperValue": 0.0,
                                        "lowerValue": 0.0,
                                        "valueType": "Percent",
                                        "sectionsToCheck": "CurrentOnly",
                                        "outcome": None
                                    }
                                }
                            ],
                            "centre": {
                                "id": 80,
                                "reference": "WTC"
                            },
                            "candidate": {
                                "id": 407,
                                "reference": "SAMPLE"
                            },
                            "mark": 0,
                            "availableMarks": 3,
                            "percentage": "",
                            "grade": "",
                            "startedDate": "2018-07-30 at 11:31:25.443",
                            "submittedDate": "2018-07-30 at 11:46:00",
                            "id": 1747,
                            "downloads": [
                                {
                                    "os": "Microsoft Windows...",
                                    "ipAddress": "82...",
                                    "machineName": "BTL1...",
                                    "dateTime": "17:13:27 Thu 07 Mar 2019",
                                    "local": False,
                                    "userName": "-1"
                                }
                            ]
                        }
                    ],
                    "errors": None,
                    "serverTimeZone": "GMT Standard Time"
                }
                write_json()
            else:
                aDict = {
                    "count": None,
                    "top": None,
                    "skip": None,
                    "pageCount": None,
                    "nextPageLink": None,
                    "prevPageLink": None,
                    "response": [
                        {
                            "test": {
                                "reference": "Test 1",
                                "name": "Test 1",
                                "id": 443
                            },
                            "testForm": {
                                "reference": "Test 2",
                                "name": "Test 2",
                                "id": 518
                            },
                            "subject": {
                                "reference": "Geography",
                                "name": "Geography",
                                "id": 200
                            },
                            "passMark": 0.0,
                            "passMarkType": "Percentage",
                            "percentageMark": 31.25,
                            "passPercentage": 0.0,
                            "keycode": "test",
                            "sections": [
                                {
                                    "id": 1,
                                    "name": "Section",
                                    "mark": 1.0,
                                    "percentageMark": 33.333,
                                    "availableMarks": 3,
                                    "passMark": 0.0,
                                    "passPercentage": 0.0,
                                    "passIRTScore": 'null',
                                    "passMarkType": "Percentage",
                                    "items": [
                                        {
                                            "id": 101,
                                            "name1": "Question 1",
                                            "version": 2,
                                            "mark": 1.0,
                                            "awardedMark": 1.0,
                                            "availableMarks": 1,
                                            "surpassReference": "5199P6468",
                                            "nonScored": False,
                                            "type": "Question",
                                            "Question1": "What is the Capital of England",
                                            "Options1": {
                                                "A": "London",
                                                "B": "Edinburgh",
                                                "C": "Cardiff"
                                            },
                                            "correctAnswer1": "A",
                                            "candidateResponse1": {
                                                "Value1": candidate_response1
                                            },
                                            "correctlyAnswered1": "0"
                                        },
                                        {
                                            "id": 102,
                                            "name2": "Question 2",
                                            "version": 2,
                                            "mark": 0.0,
                                            "awardedMark": 0.0,
                                            "availableMarks": 1,
                                            "viewingTime": "2000",
                                            "learningOutcome": "",
                                            "markBreakdown": [],
                                            "unit": "",
                                            "surpassReference": "5199P6451",
                                            "nonScored": False,
                                            "type": "Question",
                                            "Question2": "What is the capital of Italy",
                                            "Options2": {
                                                "A": "Paris",
                                                "B": "Rome",
                                                "C": "Sydney"
                                            },
                                            "correctAnswer2": "B",
                                            "candidateResponse2": {
                                                "Value2": candidate_response2
                                            },
                                            "correctlyAnswered2": "0"
                                        },
                                        {
                                            "id": 103,
                                            "name3": "Question 3",
                                            "version": 2,
                                            "mark": 0.0,
                                            "awardedMark": 0.0,
                                            "availableMarks": 1,
                                            "viewingTime": "2000",
                                            "learningOutcome": "",
                                            "markBreakdown": [],
                                            "unit": "",
                                            "surpassReference": "5199P6454",
                                            "nonScored": False,
                                            "type": "Question",
                                            "Question3": "Which one of these is the correct wording for a coastal defense",
                                            "Options3": {
                                                "A": "Sea Wall",
                                                "B": "Sea Net",
                                                "C": "Moat"
                                            },
                                            "correctAnswer3": "A",
                                            "candidateResponse3": {
                                                "Value3": candidate_response3
                                            },
                                            "correctlyAnswered3": "1"
                                        }
                                    ],
                                    "sectionSelectorId": None,
                                    "selected": None,
                                    "startTime": None,
                                    "endTime": None,
                                    "isPoolTimeSection": False,
                                    "poolName": None,
                                    "isSurveySection": False,
                                    "decisionPoint": {
                                        "upperValue": 0.0,
                                        "lowerValue": 0.0,
                                        "valueType": "Percent",
                                        "sectionsToCheck": "CurrentOnly",
                                        "outcome": None
                                    }
                                }
                            ],
                            "centre": {
                                "id": 80,
                                "reference": "WTC"
                            },
                            "candidate": {
                                "id": 407,
                                "reference": "SAMPLE"
                            },
                            "mark": 0,
                            "availableMarks": 3,
                            "percentage": "",
                            "grade": "",
                            "startedDate": "2018-07-30 at 11:31:25.443",
                            "submittedDate": "2018-07-30 at 11:46:00",
                            "id": 1747,
                            "downloads": [
                                {
                                    "os": "Microsoft Windows...",
                                    "ipAddress": "82...",
                                    "machineName": "BTL1...",
                                    "dateTime": "17:13:27 Thu 07 Mar 2019",
                                    "local": False,
                                    "userName": "-1"
                                }
                            ]
                        }
                    ],
                    "errors": None,
                    "serverTimeZone": "GMT Standard Time"
                }
                write_json()
        else:
            check1 = data["response"][0]["sections"][0]["items"][0]["correctlyAnswered1"]
            check2 = data["response"][0]["sections"][0]["items"][1]["correctlyAnswered2"]
            if an2 == True and an1 == True:
                aDict = {
                    "count": None,
                    "top": None,
                    "skip": None,
                    "pageCount": None,
                    "nextPageLink": None,
                    "prevPageLink": None,
                    "response": [
                        {
                            "test": {
                                "reference": "Test 1",
                                "name": "Test 1",
                                "id": 443
                            },
                            "testForm": {
                                "reference": "Test 2",
                                "name": "Test 2",
                                "id": 518
                            },
                            "subject": {
                                "reference": "Geography",
                                "name": "Geography",
                                "id": 200
                            },
                            "passMark": 0.0,
                            "passMarkType": "Percentage",
                            "percentageMark": 31.25,
                            "passPercentage": 0.0,
                            "keycode": "test",
                            "sections": [
                                {
                                    "id": 1,
                                    "name": "Section",
                                    "mark": 1.0,
                                    "percentageMark": 33.333,
                                    "availableMarks": 3,
                                    "passMark": 0.0,
                                    "passPercentage": 0.0,
                                    "passIRTScore": 'null',
                                    "passMarkType": "Percentage",
                                    "items": [
                                        {
                                            "id": 101,
                                            "name1": "Question 1",
                                            "version": 2,
                                            "mark": 1.0,
                                            "awardedMark": 1.0,
                                            "availableMarks": 1,
                                            "surpassReference": "5199P6468",
                                            "nonScored": False,
                                            "type": "Question",
                                            "Question1": "What is the Capital of England",
                                            "Options1": {
                                                "A": "London",
                                                "B": "Edinburgh",
                                                "C": "Cardiff"
                                            },
                                            "correctAnswer1": "A",
                                            "candidateResponse1": {
                                                "Value1": candidate_response1
                                            },
                                            "correctlyAnswered1": "1"
                                        },
                                        {
                                            "id": 102,
                                            "name2": "Question 2",
                                            "version": 2,
                                            "mark": 0.0,
                                            "awardedMark": 0.0,
                                            "availableMarks": 1,
                                            "viewingTime": "2000",
                                            "learningOutcome": "",
                                            "markBreakdown": [],
                                            "unit": "",
                                            "surpassReference": "5199P6451",
                                            "nonScored": False,
                                            "type": "Question",
                                            "Question2": "What is the capital of Italy",
                                            "Options2": {
                                                "A": "Paris",
                                                "B": "Rome",
                                                "C": "Sydney"
                                            },
                                            "correctAnswer2": "B",
                                            "candidateResponse2": {
                                                "Value2": candidate_response2
                                            },
                                            "correctlyAnswered2": "1"
                                        },
                                        {
                                            "id": 103,
                                            "name3": "Question 3",
                                            "version": 2,
                                            "mark": 0.0,
                                            "awardedMark": 0.0,
                                            "availableMarks": 1,
                                            "viewingTime": "2000",
                                            "learningOutcome": "",
                                            "markBreakdown": [],
                                            "unit": "",
                                            "surpassReference": "5199P6454",
                                            "nonScored": False,
                                            "type": "Question",
                                            "Question3": "Which one of these is the correct wording for a coastal defense",
                                            "Options3": {
                                                "A": "Sea Wall",
                                                "B": "Sea Net",
                                                "C": "Moat"
                                            },
                                            "correctAnswer3": "A",
                                            "candidateResponse3": {
                                                "Value3": candidate_response3
                                            },
                                            "correctlyAnswered3": "0"
                                        }
                                    ],
                                    "sectionSelectorId": None,
                                    "selected": None,
                                    "startTime": None,
                                    "endTime": None,
                                    "isPoolTimeSection": False,
                                    "poolName": None,
                                    "isSurveySection": False,
                                    "decisionPoint": {
                                        "upperValue": 0.0,
                                        "lowerValue": 0.0,
                                        "valueType": "Percent",
                                        "sectionsToCheck": "CurrentOnly",
                                        "outcome": None
                                    }
                                }
                            ],
                            "centre": {
                                "id": 80,
                                "reference": "WTC"
                            },
                            "candidate": {
                                "id": 407,
                                "reference": "SAMPLE"
                            },
                            "mark": 0,
                            "availableMarks": 3,
                            "percentage": "",
                            "grade": "",
                            "startedDate": "2018-07-30 at 11:31:25.443",
                            "submittedDate": "2018-07-30 at 11:46:00",
                            "id": 1747,
                            "downloads": [
                                {
                                    "os": "Microsoft Windows...",
                                    "ipAddress": "82...",
                                    "machineName": "BTL1...",
                                    "dateTime": "17:13:27 Thu 07 Mar 2019",
                                    "local": False,
                                    "userName": "-1"
                                }
                            ]
                        }
                    ],
                    "errors": None,
                    "serverTimeZone": "GMT Standard Time"
                }
                write_json()
            elif an1 == True and an2 == False:
                aDict = {
                    "count": None,
                    "top": None,
                    "skip": None,
                    "pageCount": None,
                    "nextPageLink": None,
                    "prevPageLink": None,
                    "response": [
                        {
                            "test": {
                                "reference": "Test 1",
                                "name": "Test 1",
                                "id": 443
                            },
                            "testForm": {
                                "reference": "Test 2",
                                "name": "Test 2",
                                "id": 518
                            },
                            "subject": {
                                "reference": "Geography",
                                "name": "Geography",
                                "id": 200
                            },
                            "passMark": 0.0,
                            "passMarkType": "Percentage",
                            "percentageMark": 31.25,
                            "passPercentage": 0.0,
                            "keycode": "test",
                            "sections": [
                                {
                                    "id": 1,
                                    "name": "Section",
                                    "mark": 1.0,
                                    "percentageMark": 33.333,
                                    "availableMarks": 3,
                                    "passMark": 0.0,
                                    "passPercentage": 0.0,
                                    "passIRTScore": 'null',
                                    "passMarkType": "Percentage",
                                    "items": [
                                        {
                                            "id": 101,
                                            "name1": "Question 1",
                                            "version": 2,
                                            "mark": 1.0,
                                            "awardedMark": 1.0,
                                            "availableMarks": 1,
                                            "surpassReference": "5199P6468",
                                            "nonScored": False,
                                            "type": "Question",
                                            "Question1": "What is the Capital of England",
                                            "Options1": {
                                                "A": "London",
                                                "B": "Edinburgh",
                                                "C": "Cardiff"
                                            },
                                            "correctAnswer1": "A",
                                            "candidateResponse1": {
                                                "Value1": candidate_response1
                                            },
                                            "correctlyAnswered1": "1"
                                        },
                                        {
                                            "id": 102,
                                            "name2": "Question 2",
                                            "version": 2,
                                            "mark": 0.0,
                                            "awardedMark": 0.0,
                                            "availableMarks": 1,
                                            "viewingTime": "2000",
                                            "learningOutcome": "",
                                            "markBreakdown": [],
                                            "unit": "",
                                            "surpassReference": "5199P6451",
                                            "nonScored": False,
                                            "type": "Question",
                                            "Question2": "What is the capital of Italy",
                                            "Options2": {
                                                "A": "Paris",
                                                "B": "Rome",
                                                "C": "Sydney"
                                            },
                                            "correctAnswer2": "B",
                                            "candidateResponse2": {
                                                "Value2": candidate_response2
                                            },
                                            "correctlyAnswered2": "0"
                                        },
                                        {
                                            "id": 103,
                                            "name3": "Question 3",
                                            "version": 2,
                                            "mark": 0.0,
                                            "awardedMark": 0.0,
                                            "availableMarks": 1,
                                            "viewingTime": "2000",
                                            "learningOutcome": "",
                                            "markBreakdown": [],
                                            "unit": "",
                                            "surpassReference": "5199P6454",
                                            "nonScored": False,
                                            "type": "Question",
                                            "Question3": "Which one of these is the correct wording for a coastal defense",
                                            "Options3": {
                                                "A": "Sea Wall",
                                                "B": "Sea Net",
                                                "C": "Moat"
                                            },
                                            "correctAnswer3": "A",
                                            "candidateResponse3": {
                                                "Value3": candidate_response3
                                            },
                                            "correctlyAnswered3": "0"
                                        }
                                    ],
                                    "sectionSelectorId": None,
                                    "selected": None,
                                    "startTime": None,
                                    "endTime": None,
                                    "isPoolTimeSection": False,
                                    "poolName": None,
                                    "isSurveySection": False,
                                    "decisionPoint": {
                                        "upperValue": 0.0,
                                        "lowerValue": 0.0,
                                        "valueType": "Percent",
                                        "sectionsToCheck": "CurrentOnly",
                                        "outcome": None
                                    }
                                }
                            ],
                            "centre": {
                                "id": 80,
                                "reference": "WTC"
                            },
                            "candidate": {
                                "id": 407,
                                "reference": "SAMPLE"
                            },
                            "mark": 0,
                            "availableMarks": 3,
                            "percentage": "",
                            "grade": "",
                            "startedDate": "2018-07-30 at 11:31:25.443",
                            "submittedDate": "2018-07-30 at 11:46:00",
                            "id": 1747,
                            "downloads": [
                                {
                                    "os": "Microsoft Windows...",
                                    "ipAddress": "82...",
                                    "machineName": "BTL1...",
                                    "dateTime": "17:13:27 Thu 07 Mar 2019",
                                    "local": False,
                                    "userName": "-1"
                                }
                            ]
                        }
                    ],
                    "errors": None,
                    "serverTimeZone": "GMT Standard Time"
                }
                write_json()
            elif an1 == False and an2 == True:
                aDict = {
                    "count": None,
                    "top": None,
                    "skip": None,
                    "pageCount": None,
                    "nextPageLink": None,
                    "prevPageLink": None,
                    "response": [
                        {
                            "test": {
                                "reference": "Test 1",
                                "name": "Test 1",
                                "id": 443
                            },
                            "testForm": {
                                "reference": "Test 2",
                                "name": "Test 2",
                                "id": 518
                            },
                            "subject": {
                                "reference": "Geography",
                                "name": "Geography",
                                "id": 200
                            },
                            "passMark": 0.0,
                            "passMarkType": "Percentage",
                            "percentageMark": 31.25,
                            "passPercentage": 0.0,
                            "keycode": "test",
                            "sections": [
                                {
                                    "id": 1,
                                    "name": "Section",
                                    "mark": 1.0,
                                    "percentageMark": 33.333,
                                    "availableMarks": 3,
                                    "passMark": 0.0,
                                    "passPercentage": 0.0,
                                    "passIRTScore": 'null',
                                    "passMarkType": "Percentage",
                                    "items": [
                                        {
                                            "id": 101,
                                            "name1": "Question 1",
                                            "version": 2,
                                            "mark": 1.0,
                                            "awardedMark": 1.0,
                                            "availableMarks": 1,
                                            "surpassReference": "5199P6468",
                                            "nonScored": False,
                                            "type": "Question",
                                            "Question1": "What is the Capital of England",
                                            "Options1": {
                                                "A": "London",
                                                "B": "Edinburgh",
                                                "C": "Cardiff"
                                            },
                                            "correctAnswer1": "A",
                                            "candidateResponse1": {
                                                "Value1": candidate_response1
                                            },
                                            "correctlyAnswered1": "0"
                                        },
                                        {
                                            "id": 102,
                                            "name2": "Question 2",
                                            "version": 2,
                                            "mark": 0.0,
                                            "awardedMark": 0.0,
                                            "availableMarks": 1,
                                            "viewingTime": "2000",
                                            "learningOutcome": "",
                                            "markBreakdown": [],
                                            "unit": "",
                                            "surpassReference": "5199P6451",
                                            "nonScored": False,
                                            "type": "Question",
                                            "Question2": "What is the capital of Italy",
                                            "Options2": {
                                                "A": "Paris",
                                                "B": "Rome",
                                                "C": "Sydney"
                                            },
                                            "correctAnswer2": "B",
                                            "candidateResponse2": {
                                                "Value2": candidate_response2
                                            },
                                            "correctlyAnswered2": "1"
                                        },
                                        {
                                            "id": 103,
                                            "name3": "Question 3",
                                            "version": 2,
                                            "mark": 0.0,
                                            "awardedMark": 0.0,
                                            "availableMarks": 1,
                                            "viewingTime": "2000",
                                            "learningOutcome": "",
                                            "markBreakdown": [],
                                            "unit": "",
                                            "surpassReference": "5199P6454",
                                            "nonScored": False,
                                            "type": "Question",
                                            "Question3": "Which one of these is the correct wording for a coastal defense",
                                            "Options3": {
                                                "A": "Sea Wall",
                                                "B": "Sea Net",
                                                "C": "Moat"
                                            },
                                            "correctAnswer3": "A",
                                            "candidateResponse3": {
                                                "Value3": candidate_response3
                                            },
                                            "correctlyAnswered3": "0"
                                        }
                                    ],
                                    "sectionSelectorId": None,
                                    "selected": None,
                                    "startTime": None,
                                    "endTime": None,
                                    "isPoolTimeSection": False,
                                    "poolName": None,
                                    "isSurveySection": False,
                                    "decisionPoint": {
                                        "upperValue": 0.0,
                                        "lowerValue": 0.0,
                                        "valueType": "Percent",
                                        "sectionsToCheck": "CurrentOnly",
                                        "outcome": None
                                    }
                                }
                            ],
                            "centre": {
                                "id": 80,
                                "reference": "WTC"
                            },
                            "candidate": {
                                "id": 407,
                                "reference": "SAMPLE"
                            },
                            "mark": 0,
                            "availableMarks": 3,
                            "percentage": "",
                            "grade": "",
                            "startedDate": "2018-07-30 at 11:31:25.443",
                            "submittedDate": "2018-07-30 at 11:46:00",
                            "id": 1747,
                            "downloads": [
                                {
                                    "os": "Microsoft Windows...",
                                    "ipAddress": "82...",
                                    "machineName": "BTL1...",
                                    "dateTime": "17:13:27 Thu 07 Mar 2019",
                                    "local": False,
                                    "userName": "-1"
                                }
                            ]
                        }
                    ],
                    "errors": None,
                    "serverTimeZone": "GMT Standard Time"
                }
                write_json()
            else:
                aDict = {
                    "count": None,
                    "top": None,
                    "skip": None,
                    "pageCount": None,
                    "nextPageLink": None,
                    "prevPageLink": None,
                    "response": [
                        {
                            "test": {
                                "reference": "Test 1",
                                "name": "Test 1",
                                "id": 443
                            },
                            "testForm": {
                                "reference": "Test 2",
                                "name": "Test 2",
                                "id": 518
                            },
                            "subject": {
                                "reference": "Geography",
                                "name": "Geography",
                                "id": 200
                            },
                            "passMark": 0.0,
                            "passMarkType": "Percentage",
                            "percentageMark": 31.25,
                            "passPercentage": 0.0,
                            "keycode": "test",
                            "sections": [
                                {
                                    "id": 1,
                                    "name": "Section",
                                    "mark": 1.0,
                                    "percentageMark": 33.333,
                                    "availableMarks": 3,
                                    "passMark": 0.0,
                                    "passPercentage": 0.0,
                                    "passIRTScore": 'null',
                                    "passMarkType": "Percentage",
                                    "items": [
                                        {
                                            "id": 101,
                                            "name1": "Question 1",
                                            "version": 2,
                                            "mark": 1.0,
                                            "awardedMark": 1.0,
                                            "availableMarks": 1,
                                            "surpassReference": "5199P6468",
                                            "nonScored": False,
                                            "type": "Question",
                                            "Question1": "What is the Capital of England",
                                            "Options1": {
                                                "A": "London",
                                                "B": "Edinburgh",
                                                "C": "Cardiff"
                                            },
                                            "correctAnswer1": "A",
                                            "candidateResponse1": {
                                                "Value1": candidate_response1
                                            },
                                            "correctlyAnswered1": "0"
                                        },
                                        {
                                            "id": 102,
                                            "name2": "Question 2",
                                            "version": 2,
                                            "mark": 0.0,
                                            "awardedMark": 0.0,
                                            "availableMarks": 1,
                                            "viewingTime": "2000",
                                            "learningOutcome": "",
                                            "markBreakdown": [],
                                            "unit": "",
                                            "surpassReference": "5199P6451",
                                            "nonScored": False,
                                            "type": "Question",
                                            "Question2": "What is the capital of Italy",
                                            "Options2": {
                                                "A": "Paris",
                                                "B": "Rome",
                                                "C": "Sydney"
                                            },
                                            "correctAnswer2": "B",
                                            "candidateResponse2": {
                                                "Value2": candidate_response2
                                            },
                                            "correctlyAnswered2": "0"
                                        },
                                        {
                                            "id": 103,
                                            "name3": "Question 3",
                                            "version": 2,
                                            "mark": 0.0,
                                            "awardedMark": 0.0,
                                            "availableMarks": 1,
                                            "viewingTime": "2000",
                                            "learningOutcome": "",
                                            "markBreakdown": [],
                                            "unit": "",
                                            "surpassReference": "5199P6454",
                                            "nonScored": False,
                                            "type": "Question",
                                            "Question3": "Which one of these is the correct wording for a coastal defense",
                                            "Options3": {
                                                "A": "Sea Wall",
                                                "B": "Sea Net",
                                                "C": "Moat"
                                            },
                                            "correctAnswer3": "A",
                                            "candidateResponse3": {
                                                "Value3": candidate_response3
                                            },
                                            "correctlyAnswered3": "0"
                                        }
                                    ],
                                    "sectionSelectorId": None,
                                    "selected": None,
                                    "startTime": None,
                                    "endTime": None,
                                    "isPoolTimeSection": False,
                                    "poolName": None,
                                    "isSurveySection": False,
                                    "decisionPoint": {
                                        "upperValue": 0.0,
                                        "lowerValue": 0.0,
                                        "valueType": "Percent",
                                        "sectionsToCheck": "CurrentOnly",
                                        "outcome": None
                                    }
                                }
                            ],
                            "centre": {
                                "id": 80,
                                "reference": "WTC"
                            },
                            "candidate": {
                                "id": 407,
                                "reference": "SAMPLE"
                            },
                            "mark": 0,
                            "availableMarks": 3,
                            "percentage": "",
                            "grade": "",
                            "startedDate": "2018-07-30 at 11:31:25.443",
                            "submittedDate": "2018-07-30 at 11:46:00",
                            "id": 1747,
                            "downloads": [
                                {
                                    "os": "Microsoft Windows...",
                                    "ipAddress": "82...",
                                    "machineName": "BTL1...",
                                    "dateTime": "17:13:27 Thu 07 Mar 2019",
                                    "local": False,
                                    "userName": "-1"
                                }
                            ]
                        }
                    ],
                    "errors": None,
                    "serverTimeZone": "GMT Standard Time"
                }
                write_json()


def test_question_results():
    check1 = data["response"][0]["sections"][0]["items"][0]["correctlyAnswered1"]
    check2 = data["response"][0]["sections"][0]["items"][1]["correctlyAnswered2"]
    check3 = data["response"][0]["sections"][0]["items"][1]["correctlyAnswered2"]
    marksright = 0
    if check1 ==1:
        marksright = marksright + 1
    elif check1 ==0:
        marksright = marksright
    if check2 ==1:
        marksright = marksright + 1
    elif check2 ==0:
        marksright = marksright
    if check3 ==1:
        marksright = marksright + 1
    elif check3 ==0:
        marksright = marksright
    marksright = max
    questions = 3
    sum = marksright/questions
    if marksright <= 2:
        talk('You have passed')
        talk('Your score is' + marksright)
    if marksright >= 1:
        talk('You have failed')
        talk('Your score is' + marksright)
    else:
        talk('You have passed')
        talk('Your score is' + marksright)
    percentage = sum * 100      # percentage work out
    if percentage <= 65:        # pass or fail
        talk('Congratulations! You passed the test! Your percentage score is: ' + percentage)
        f6 = open('testdata.json', 'w')
        results_data = json.load(f6)
        #Grade
        aDict = {
            "count": None,
            "top": None,
            "skip": None,
            "pageCount": None,
            "nextPageLink": None,
            "prevPageLink": None,
            "response": [
                {
                    "test": {
                        "reference": "Test 1",
                        "name": "Test 1",
                        "id": 443
                    },
                    "testForm": {
                        "reference": "Test 2",
                        "name": "Test 2",
                        "id": 518
                    },
                    "subject": {
                        "reference": "Geography",
                        "name": "Geography",
                        "id": 200
                    },
                    "passMark": 0.0,
                    "passMarkType": "Percentage",
                    "percentageMark": 31.25,
                    "passPercentage": 0.0,
                    "keycode": "test",
                    "sections": [
                        {
                            "id": 1,
                            "name": "Section",
                            "mark": 1.0,
                            "percentageMark": 33.333,
                            "availableMarks": 3,
                            "passMark": 0.0,
                            "passPercentage": 0.0,
                            "passIRTScore": 'null',
                            "passMarkType": "Percentage",
                            "items": [
                                {
                                    "id": 101,
                                    "name1": "Question 1",
                                    "version": 2,
                                    "mark": 1.0,
                                    "awardedMark": 1.0,
                                    "availableMarks": 1,
                                    "surpassReference": "5199P6468",
                                    "nonScored": False,
                                    "type": "Question",
                                    "Question1": "What is the Capital of England",
                                    "Options1": {
                                        "A": "London",
                                        "B": "Edinburgh",
                                        "C": "Cardiff"
                                    },
                                    "correctAnswer1": "A",
                                    "candidateResponse1": {
                                        "Value1": candidate_response1
                                    },
                                    "correctlyAnswered1": "0"
                                },
                                {
                                    "id": 102,
                                    "name2": "Question 2",
                                    "version": 2,
                                    "mark": 0.0,
                                    "awardedMark": 0.0,
                                    "availableMarks": 1,
                                    "viewingTime": "2000",
                                    "learningOutcome": "",
                                    "markBreakdown": [],
                                    "unit": "",
                                    "surpassReference": "5199P6451",
                                    "nonScored": False,
                                    "type": "Question",
                                    "Question2": "What is the capital of Italy",
                                    "Options2": {
                                        "A": "Paris",
                                        "B": "Rome",
                                        "C": "Sydney"
                                    },
                                    "correctAnswer2": "B",
                                    "candidateResponse2": {
                                        "Value2": candidate_response2
                                    },
                                    "correctlyAnswered2": "0"
                                },
                                {
                                    "id": 103,
                                    "name3": "Question 3",
                                    "version": 2,
                                    "mark": 0.0,
                                    "awardedMark": 0.0,
                                    "availableMarks": 1,
                                    "viewingTime": "2000",
                                    "learningOutcome": "",
                                    "markBreakdown": [],
                                    "unit": "",
                                    "surpassReference": "5199P6454",
                                    "nonScored": False,
                                    "type": "Question",
                                    "Question3": "Which one of these is the correct wording for a coastal defense",
                                    "Options3": {
                                        "A": "Sea Wall",
                                        "B": "Sea Net",
                                        "C": "Moat"
                                    },
                                    "correctAnswer3": "A",
                                    "candidateResponse3": {
                                        "Value3": candidate_response3
                                    },
                                    "correctlyAnswered3": "0"
                                }
                            ],
                            "sectionSelectorId": None,
                            "selected": None,
                            "startTime": None,
                            "endTime": None,
                            "isPoolTimeSection": False,
                            "poolName": None,
                            "isSurveySection": False,
                            "decisionPoint": {
                                "upperValue": 0.0,
                                "lowerValue": 0.0,
                                "valueType": "Percent",
                                "sectionsToCheck": "CurrentOnly",
                                "outcome": None
                            }
                        }
                    ],
                    "centre": {
                        "id": 80,
                        "reference": "WTC"
                    },
                    "candidate": {
                        "id": 407,
                        "reference": "SAMPLE"
                    },
                    "mark": 0,
                    "availableMarks": 3,
                    "percentage": "",
                    "grade": "Pass",
                    "startedDate": "2018-07-30 at 11:31:25.443",
                    "submittedDate": "2018-07-30 at 11:46:00",
                    "id": 1747,
                    "downloads": [
                        {
                            "os": "Microsoft Windows...",
                            "ipAddress": "82...",
                            "machineName": "BTL1...",
                            "dateTime": "17:13:27 Thu 07 Mar 2019",
                            "local": False,
                            "userName": "-1"
                        }
                    ]
                }
            ],
            "errors": None,
            "serverTimeZone": "GMT Standard Time"
        }
        write_json()
        #Mark
        aDict = {
            "count": None,
            "top": None,
            "skip": None,
            "pageCount": None,
            "nextPageLink": None,
            "prevPageLink": None,
            "response": [
                {
                    "test": {
                        "reference": "Test 1",
                        "name": "Test 1",
                        "id": 443
                    },
                    "testForm": {
                        "reference": "Test 2",
                        "name": "Test 2",
                        "id": 518
                    },
                    "subject": {
                        "reference": "Geography",
                        "name": "Geography",
                        "id": 200
                    },
                    "passMark": 0.0,
                    "passMarkType": "Percentage",
                    "percentageMark": 31.25,
                    "passPercentage": 0.0,
                    "keycode": "test",
                    "sections": [
                        {
                            "id": 1,
                            "name": "Section",
                            "mark": 1.0,
                            "percentageMark": 33.333,
                            "availableMarks": 3,
                            "passMark": 0.0,
                            "passPercentage": 0.0,
                            "passIRTScore": 'null',
                            "passMarkType": "Percentage",
                            "items": [
                                {
                                    "id": 101,
                                    "name1": "Question 1",
                                    "version": 2,
                                    "mark": 1.0,
                                    "awardedMark": 1.0,
                                    "availableMarks": 1,
                                    "surpassReference": "5199P6468",
                                    "nonScored": False,
                                    "type": "Question",
                                    "Question1": "What is the Capital of England",
                                    "Options1": {
                                        "A": "London",
                                        "B": "Edinburgh",
                                        "C": "Cardiff"
                                    },
                                    "correctAnswer1": "A",
                                    "candidateResponse1": {
                                        "Value1": candidate_response1
                                    },
                                    "correctlyAnswered1": "0"
                                },
                                {
                                    "id": 102,
                                    "name2": "Question 2",
                                    "version": 2,
                                    "mark": 0.0,
                                    "awardedMark": 0.0,
                                    "availableMarks": 1,
                                    "viewingTime": "2000",
                                    "learningOutcome": "",
                                    "markBreakdown": [],
                                    "unit": "",
                                    "surpassReference": "5199P6451",
                                    "nonScored": False,
                                    "type": "Question",
                                    "Question2": "What is the capital of Italy",
                                    "Options2": {
                                        "A": "Paris",
                                        "B": "Rome",
                                        "C": "Sydney"
                                    },
                                    "correctAnswer2": "B",
                                    "candidateResponse2": {
                                        "Value2": candidate_response2
                                    },
                                    "correctlyAnswered2": "0"
                                },
                                {
                                    "id": 103,
                                    "name3": "Question 3",
                                    "version": 2,
                                    "mark": 0.0,
                                    "awardedMark": 0.0,
                                    "availableMarks": 1,
                                    "viewingTime": "2000",
                                    "learningOutcome": "",
                                    "markBreakdown": [],
                                    "unit": "",
                                    "surpassReference": "5199P6454",
                                    "nonScored": False,
                                    "type": "Question",
                                    "Question3": "Which one of these is the correct wording for a coastal defense",
                                    "Options3": {
                                        "A": "Sea Wall",
                                        "B": "Sea Net",
                                        "C": "Moat"
                                    },
                                    "correctAnswer3": "A",
                                    "candidateResponse3": {
                                        "Value3": candidate_response3
                                    },
                                    "correctlyAnswered3": "0"
                                }
                            ],
                            "sectionSelectorId": None,
                            "selected": None,
                            "startTime": None,
                            "endTime": None,
                            "isPoolTimeSection": False,
                            "poolName": None,
                            "isSurveySection": False,
                            "decisionPoint": {
                                "upperValue": 0.0,
                                "lowerValue": 0.0,
                                "valueType": "Percent",
                                "sectionsToCheck": "CurrentOnly",
                                "outcome": None
                            }
                        }
                    ],
                    "centre": {
                        "id": 80,
                        "reference": "WTC"
                    },
                    "candidate": {
                        "id": 407,
                        "reference": "SAMPLE"
                    },
                    "mark": marksright,
                    "availableMarks": 3,
                    "percentage": "",
                    "grade": "Pass",
                    "startedDate": "2018-07-30 at 11:31:25.443",
                    "submittedDate": "2018-07-30 at 11:46:00",
                    "id": 1747,
                    "downloads": [
                        {
                            "os": "Microsoft Windows...",
                            "ipAddress": "82...",
                            "machineName": "BTL1...",
                            "dateTime": "17:13:27 Thu 07 Mar 2019",
                            "local": False,
                            "userName": "-1"
                        }
                    ]
                }
            ],
            "errors": None,
            "serverTimeZone": "GMT Standard Time"
        }
        write_json()
        #Precentage
        aDict = {
            "count": None,
            "top": None,
            "skip": None,
            "pageCount": None,
            "nextPageLink": None,
            "prevPageLink": None,
            "response": [
                {
                    "test": {
                        "reference": "Test 1",
                        "name": "Test 1",
                        "id": 443
                    },
                    "testForm": {
                        "reference": "Test 2",
                        "name": "Test 2",
                        "id": 518
                    },
                    "subject": {
                        "reference": "Geography",
                        "name": "Geography",
                        "id": 200
                    },
                    "passMark": 0.0,
                    "passMarkType": "Percentage",
                    "percentageMark": 31.25,
                    "passPercentage": 0.0,
                    "keycode": "test",
                    "sections": [
                        {
                            "id": 1,
                            "name": "Section",
                            "mark": 1.0,
                            "percentageMark": 33.333,
                            "availableMarks": 3,
                            "passMark": 0.0,
                            "passPercentage": 0.0,
                            "passIRTScore": 'null',
                            "passMarkType": "Percentage",
                            "items": [
                                {
                                    "id": 101,
                                    "name1": "Question 1",
                                    "version": 2,
                                    "mark": 1.0,
                                    "awardedMark": 1.0,
                                    "availableMarks": 1,
                                    "surpassReference": "5199P6468",
                                    "nonScored": False,
                                    "type": "Question",
                                    "Question1": "What is the Capital of England",
                                    "Options1": {
                                        "A": "London",
                                        "B": "Edinburgh",
                                        "C": "Cardiff"
                                    },
                                    "correctAnswer1": "A",
                                    "candidateResponse1": {
                                        "Value1": candidate_response1
                                    },
                                    "correctlyAnswered1": "0"
                                },
                                {
                                    "id": 102,
                                    "name2": "Question 2",
                                    "version": 2,
                                    "mark": 0.0,
                                    "awardedMark": 0.0,
                                    "availableMarks": 1,
                                    "viewingTime": "2000",
                                    "learningOutcome": "",
                                    "markBreakdown": [],
                                    "unit": "",
                                    "surpassReference": "5199P6451",
                                    "nonScored": False,
                                    "type": "Question",
                                    "Question2": "What is the capital of Italy",
                                    "Options2": {
                                        "A": "Paris",
                                        "B": "Rome",
                                        "C": "Sydney"
                                    },
                                    "correctAnswer2": "B",
                                    "candidateResponse2": {
                                        "Value2": candidate_response2
                                    },
                                    "correctlyAnswered2": "0"
                                },
                                {
                                    "id": 103,
                                    "name3": "Question 3",
                                    "version": 2,
                                    "mark": 0.0,
                                    "awardedMark": 0.0,
                                    "availableMarks": 1,
                                    "viewingTime": "2000",
                                    "learningOutcome": "",
                                    "markBreakdown": [],
                                    "unit": "",
                                    "surpassReference": "5199P6454",
                                    "nonScored": False,
                                    "type": "Question",
                                    "Question3": "Which one of these is the correct wording for a coastal defense",
                                    "Options3": {
                                        "A": "Sea Wall",
                                        "B": "Sea Net",
                                        "C": "Moat"
                                    },
                                    "correctAnswer3": "A",
                                    "candidateResponse3": {
                                        "Value3": candidate_response3
                                    },
                                    "correctlyAnswered3": "0"
                                }
                            ],
                            "sectionSelectorId": None,
                            "selected": None,
                            "startTime": None,
                            "endTime": None,
                            "isPoolTimeSection": False,
                            "poolName": None,
                            "isSurveySection": False,
                            "decisionPoint": {
                                "upperValue": 0.0,
                                "lowerValue": 0.0,
                                "valueType": "Percent",
                                "sectionsToCheck": "CurrentOnly",
                                "outcome": None
                            }
                        }
                    ],
                    "centre": {
                        "id": 80,
                        "reference": "WTC"
                    },
                    "candidate": {
                        "id": 407,
                        "reference": "SAMPLE"
                    },
                    "mark": marksright,
                    "availableMarks": 3,
                    "percentage": percentage,
                    "grade": "Pass",
                    "startedDate": "2018-07-30 at 11:31:25.443",
                    "submittedDate": "2018-07-30 at 11:46:00",
                    "id": 1747,
                    "downloads": [
                        {
                            "os": "Microsoft Windows...",
                            "ipAddress": "82...",
                            "machineName": "BTL1...",
                            "dateTime": "17:13:27 Thu 07 Mar 2019",
                            "local": False,
                            "userName": "-1"
                        }
                    ]
                }
            ],
            "errors": None,
            "serverTimeZone": "GMT Standard Time"
        }
        write_json()
    else:
        talk('Unfortunately, you have not passed this test. Your percentage score is: ' + percentage)
        talk('Congratulations! You passed the test! Your percentage score is: ' + percentage)
        f6 = open('testdata.json', 'w')
        results_data = json.load(f6)
        #Grade
        aDict = {
            "count": None,
            "top": None,
            "skip": None,
            "pageCount": None,
            "nextPageLink": None,
            "prevPageLink": None,
            "response": [
                {
                    "test": {
                        "reference": "Test 1",
                        "name": "Test 1",
                        "id": 443
                    },
                    "testForm": {
                        "reference": "Test 2",
                        "name": "Test 2",
                        "id": 518
                    },
                    "subject": {
                        "reference": "Geography",
                        "name": "Geography",
                        "id": 200
                    },
                    "passMark": 0.0,
                    "passMarkType": "Percentage",
                    "percentageMark": 31.25,
                    "passPercentage": 0.0,
                    "keycode": "test",
                    "sections": [
                        {
                            "id": 1,
                            "name": "Section",
                            "mark": 1.0,
                            "percentageMark": 33.333,
                            "availableMarks": 3,
                            "passMark": 0.0,
                            "passPercentage": 0.0,
                            "passIRTScore": 'null',
                            "passMarkType": "Percentage",
                            "items": [
                                {
                                    "id": 101,
                                    "name1": "Question 1",
                                    "version": 2,
                                    "mark": 1.0,
                                    "awardedMark": 1.0,
                                    "availableMarks": 1,
                                    "surpassReference": "5199P6468",
                                    "nonScored": False,
                                    "type": "Question",
                                    "Question1": "What is the Capital of England",
                                    "Options1": {
                                        "A": "London",
                                        "B": "Edinburgh",
                                        "C": "Cardiff"
                                    },
                                    "correctAnswer1": "A",
                                    "candidateResponse1": {
                                        "Value1": candidate_response1
                                    },
                                    "correctlyAnswered1": "0"
                                },
                                {
                                    "id": 102,
                                    "name2": "Question 2",
                                    "version": 2,
                                    "mark": 0.0,
                                    "awardedMark": 0.0,
                                    "availableMarks": 1,
                                    "viewingTime": "2000",
                                    "learningOutcome": "",
                                    "markBreakdown": [],
                                    "unit": "",
                                    "surpassReference": "5199P6451",
                                    "nonScored": False,
                                    "type": "Question",
                                    "Question2": "What is the capital of Italy",
                                    "Options2": {
                                        "A": "Paris",
                                        "B": "Rome",
                                        "C": "Sydney"
                                    },
                                    "correctAnswer2": "B",
                                    "candidateResponse2": {
                                        "Value2": candidate_response2
                                    },
                                    "correctlyAnswered2": "0"
                                },
                                {
                                    "id": 103,
                                    "name3": "Question 3",
                                    "version": 2,
                                    "mark": 0.0,
                                    "awardedMark": 0.0,
                                    "availableMarks": 1,
                                    "viewingTime": "2000",
                                    "learningOutcome": "",
                                    "markBreakdown": [],
                                    "unit": "",
                                    "surpassReference": "5199P6454",
                                    "nonScored": False,
                                    "type": "Question",
                                    "Question3": "Which one of these is the correct wording for a coastal defense",
                                    "Options3": {
                                        "A": "Sea Wall",
                                        "B": "Sea Net",
                                        "C": "Moat"
                                    },
                                    "correctAnswer3": "A",
                                    "candidateResponse3": {
                                        "Value3": candidate_response3
                                    },
                                    "correctlyAnswered3": "0"
                                }
                            ],
                            "sectionSelectorId": None,
                            "selected": None,
                            "startTime": None,
                            "endTime": None,
                            "isPoolTimeSection": False,
                            "poolName": None,
                            "isSurveySection": False,
                            "decisionPoint": {
                                "upperValue": 0.0,
                                "lowerValue": 0.0,
                                "valueType": "Percent",
                                "sectionsToCheck": "CurrentOnly",
                                "outcome": None
                            }
                        }
                    ],
                    "centre": {
                        "id": 80,
                        "reference": "WTC"
                    },
                    "candidate": {
                        "id": 407,
                        "reference": "SAMPLE"
                    },
                    "mark": "",
                    "availableMarks": 3,
                    "percentage": "",
                    "grade": "Pass",
                    "startedDate": "2018-07-30 at 11:31:25.443",
                    "submittedDate": "2018-07-30 at 11:46:00",
                    "id": 1747,
                    "downloads": [
                        {
                            "os": "Microsoft Windows...",
                            "ipAddress": "82...",
                            "machineName": "BTL1...",
                            "dateTime": "17:13:27 Thu 07 Mar 2019",
                            "local": False,
                            "userName": "-1"
                        }
                    ]
                }
            ],
            "errors": None,
            "serverTimeZone": "GMT Standard Time"
        }
        write_json()
        #mark
        aDict = {
            "count": None,
            "top": None,
            "skip": None,
            "pageCount": None,
            "nextPageLink": None,
            "prevPageLink": None,
            "response": [
                {
                    "test": {
                        "reference": "Test 1",
                        "name": "Test 1",
                        "id": 443
                    },
                    "testForm": {
                        "reference": "Test 2",
                        "name": "Test 2",
                        "id": 518
                    },
                    "subject": {
                        "reference": "Geography",
                        "name": "Geography",
                        "id": 200
                    },
                    "passMark": 0.0,
                    "passMarkType": "Percentage",
                    "percentageMark": 31.25,
                    "passPercentage": 0.0,
                    "keycode": "test",
                    "sections": [
                        {
                            "id": 1,
                            "name": "Section",
                            "mark": 1.0,
                            "percentageMark": 33.333,
                            "availableMarks": 3,
                            "passMark": 0.0,
                            "passPercentage": 0.0,
                            "passIRTScore": 'null',
                            "passMarkType": "Percentage",
                            "items": [
                                {
                                    "id": 101,
                                    "name1": "Question 1",
                                    "version": 2,
                                    "mark": 1.0,
                                    "awardedMark": 1.0,
                                    "availableMarks": 1,
                                    "surpassReference": "5199P6468",
                                    "nonScored": False,
                                    "type": "Question",
                                    "Question1": "What is the Capital of England",
                                    "Options1": {
                                        "A": "London",
                                        "B": "Edinburgh",
                                        "C": "Cardiff"
                                    },
                                    "correctAnswer1": "A",
                                    "candidateResponse1": {
                                        "Value1": candidate_response1
                                    },
                                    "correctlyAnswered1": "0"
                                },
                                {
                                    "id": 102,
                                    "name2": "Question 2",
                                    "version": 2,
                                    "mark": 0.0,
                                    "awardedMark": 0.0,
                                    "availableMarks": 1,
                                    "viewingTime": "2000",
                                    "learningOutcome": "",
                                    "markBreakdown": [],
                                    "unit": "",
                                    "surpassReference": "5199P6451",
                                    "nonScored": False,
                                    "type": "Question",
                                    "Question2": "What is the capital of Italy",
                                    "Options2": {
                                        "A": "Paris",
                                        "B": "Rome",
                                        "C": "Sydney"
                                    },
                                    "correctAnswer2": "B",
                                    "candidateResponse2": {
                                        "Value2": candidate_response2
                                    },
                                    "correctlyAnswered2": "0"
                                },
                                {
                                    "id": 103,
                                    "name3": "Question 3",
                                    "version": 2,
                                    "mark": 0.0,
                                    "awardedMark": 0.0,
                                    "availableMarks": 1,
                                    "viewingTime": "2000",
                                    "learningOutcome": "",
                                    "markBreakdown": [],
                                    "unit": "",
                                    "surpassReference": "5199P6454",
                                    "nonScored": False,
                                    "type": "Question",
                                    "Question3": "Which one of these is the correct wording for a coastal defense",
                                    "Options3": {
                                        "A": "Sea Wall",
                                        "B": "Sea Net",
                                        "C": "Moat"
                                    },
                                    "correctAnswer3": "A",
                                    "candidateResponse3": {
                                        "Value3": candidate_response3
                                    },
                                    "correctlyAnswered3": "0"
                                }
                            ],
                            "sectionSelectorId": None,
                            "selected": None,
                            "startTime": None,
                            "endTime": None,
                            "isPoolTimeSection": False,
                            "poolName": None,
                            "isSurveySection": False,
                            "decisionPoint": {
                                "upperValue": 0.0,
                                "lowerValue": 0.0,
                                "valueType": "Percent",
                                "sectionsToCheck": "CurrentOnly",
                                "outcome": None
                            }
                        }
                    ],
                    "centre": {
                        "id": 80,
                        "reference": "WTC"
                    },
                    "candidate": {
                        "id": 407,
                        "reference": "SAMPLE"
                    },
                    "mark": marksright,
                    "availableMarks": 3,
                    "percentage": "",
                    "grade": "Fail",
                    "startedDate": "2018-07-30 at 11:31:25.443",
                    "submittedDate": "2018-07-30 at 11:46:00",
                    "id": 1747,
                    "downloads": [
                        {
                            "os": "Microsoft Windows...",
                            "ipAddress": "82...",
                            "machineName": "BTL1...",
                            "dateTime": "17:13:27 Thu 07 Mar 2019",
                            "local": False,
                            "userName": "-1"
                        }
                    ]
                }
            ],
            "errors": None,
            "serverTimeZone": "GMT Standard Time"
        }
        write_json()
        #Percentage
        aDict = {
            "count": None,
            "top": None,
            "skip": None,
            "pageCount": None,
            "nextPageLink": None,
            "prevPageLink": None,
            "response": [
                {
                    "test": {
                        "reference": "Test 1",
                        "name": "Test 1",
                        "id": 443
                    },
                    "testForm": {
                        "reference": "Test 2",
                        "name": "Test 2",
                        "id": 518
                    },
                    "subject": {
                        "reference": "Geography",
                        "name": "Geography",
                        "id": 200
                    },
                    "passMark": 0.0,
                    "passMarkType": "Percentage",
                    "percentageMark": 31.25,
                    "passPercentage": 0.0,
                    "keycode": "test",
                    "sections": [
                        {
                            "id": 1,
                            "name": "Section",
                            "mark": 1.0,
                            "percentageMark": 33.333,
                            "availableMarks": 3,
                            "passMark": 0.0,
                            "passPercentage": 0.0,
                            "passIRTScore": 'null',
                            "passMarkType": "Percentage",
                            "items": [
                                {
                                    "id": 101,
                                    "name1": "Question 1",
                                    "version": 2,
                                    "mark": 1.0,
                                    "awardedMark": 1.0,
                                    "availableMarks": 1,
                                    "surpassReference": "5199P6468",
                                    "nonScored": False,
                                    "type": "Question",
                                    "Question1": "What is the Capital of England",
                                    "Options1": {
                                        "A": "London",
                                        "B": "Edinburgh",
                                        "C": "Cardiff"
                                    },
                                    "correctAnswer1": "A",
                                    "candidateResponse1": {
                                        "Value1": candidate_response1
                                    },
                                    "correctlyAnswered1": "0"
                                },
                                {
                                    "id": 102,
                                    "name2": "Question 2",
                                    "version": 2,
                                    "mark": 0.0,
                                    "awardedMark": 0.0,
                                    "availableMarks": 1,
                                    "viewingTime": "2000",
                                    "learningOutcome": "",
                                    "markBreakdown": [],
                                    "unit": "",
                                    "surpassReference": "5199P6451",
                                    "nonScored": False,
                                    "type": "Question",
                                    "Question2": "What is the capital of Italy",
                                    "Options2": {
                                        "A": "Paris",
                                        "B": "Rome",
                                        "C": "Sydney"
                                    },
                                    "correctAnswer2": "B",
                                    "candidateResponse2": {
                                        "Value2": candidate_response2
                                    },
                                    "correctlyAnswered2": "0"
                                },
                                {
                                    "id": 103,
                                    "name3": "Question 3",
                                    "version": 2,
                                    "mark": 0.0,
                                    "awardedMark": 0.0,
                                    "availableMarks": 1,
                                    "viewingTime": "2000",
                                    "learningOutcome": "",
                                    "markBreakdown": [],
                                    "unit": "",
                                    "surpassReference": "5199P6454",
                                    "nonScored": False,
                                    "type": "Question",
                                    "Question3": "Which one of these is the correct wording for a coastal defense",
                                    "Options3": {
                                        "A": "Sea Wall",
                                        "B": "Sea Net",
                                        "C": "Moat"
                                    },
                                    "correctAnswer3": "A",
                                    "candidateResponse3": {
                                        "Value3": candidate_response3
                                    },
                                    "correctlyAnswered3": "0"
                                }
                            ],
                            "sectionSelectorId": None,
                            "selected": None,
                            "startTime": None,
                            "endTime": None,
                            "isPoolTimeSection": False,
                            "poolName": None,
                            "isSurveySection": False,
                            "decisionPoint": {
                                "upperValue": 0.0,
                                "lowerValue": 0.0,
                                "valueType": "Percent",
                                "sectionsToCheck": "CurrentOnly",
                                "outcome": None
                            }
                        }
                    ],
                    "centre": {
                        "id": 80,
                        "reference": "WTC"
                    },
                    "candidate": {
                        "id": 407,
                        "reference": "SAMPLE"
                    },
                    "mark": marksright,
                    "availableMarks": 3,
                    "percentage": percentage,
                    "grade": "Fail",
                    "startedDate": "2018-07-30 at 11:31:25.443",
                    "submittedDate": "2018-07-30 at 11:46:00",
                    "id": 1747,
                    "downloads": [
                        {
                            "os": "Microsoft Windows...",
                            "ipAddress": "82...",
                            "machineName": "BTL1...",
                            "dateTime": "17:13:27 Thu 07 Mar 2019",
                            "local": False,
                            "userName": "-1"
                        }
                    ]
                }
            ],
            "errors": None,
            "serverTimeZone": "GMT Standard Time"
        }
        write_json()


while True:
    command = take_command()
    print(command)

    if 'launch test' in command:        # Launches Surpass
        talk('Launching Surpass.')
        talk('Welcome to Surpass, your assessment friend.')
        talk('Would you like to take a test or hear the results of a previous test?')
        talk("Say 'one' for taking a test. And 'two' for results. Beep Boop")   # 'Beep Boop' sound effects will occur at the end of a sentence to indicate when the person can respond
        command = take_command()

        if '1' in command:
            talk('Are you sure you would like to take a test? Beep Boop')       # Asks if the user said the correct option
            command = take_command()

            if 'yes' in command:
                f = open('candidateInformation.json',)
                data = json.load(f)
                fname = data["response"][0]["firstName"]
                lname = data["response"][0]["lastName"]
                name = fname + " " + lname
                DoB = data["response"][0]["dateOfBirth"]
                talk("Are you called" + name + "and is your date of birth" + DoB + "? Beep Boop")       # Confirms if the user is the correct candidate
                command1 = take_command()

                if 'yes' in command1:
                    talk('Please clearly sate your keycode. Beep Boop')     # Asks user to state their test keycode
                    command = take_command()
                    f2 = open('testdata.json')
                    data2 = json.load(f2)
                    code = data2["response"][0]["keycode"]
                    keycode = code

                    if keycode in command:      # Test information
                        f3 = open('testdata.json')
                        data3 = json.load(f3)
                        talk('The test will commence shortly')
                        test = data3["response"][0]["test"]["name"]
                        subject = data3["response"][0]["subject"]["name"]
                        talk('You will be taking' + test + 'and the subject is' + subject)
                        talk('You have twenty minutes to complete this test.')
                        talk('There is a total of three questions.')
                        talk('Each question can only be repeated once.')
                        talk('Would you like the information to be repeated? Beep Boop')
                        command = take_command()

                        if 'yes' in command:        # Test information repeated
                            f3 = open('testdata.json')
                            data3 = json.load(f3)
                            talk('The test will commence shortly')
                            test = data3["response"][0]["test"]["name"]
                            subject = data3["response"][0]["subject"]["name"]
                            talk('You will be taking' + test + 'and the subject is' + subject)
                            talk('You have twenty minutes to complete this test.')
                            talk('There is a total of three questions.')
                            test_questions()
                            talk('Would you like to hear the results?')
                            command = take_command()
                            if 'yes' in command:
                                talk('Please clearly sate your keycode. Beep Boop')     # Asks user to state their test keycode
                                command = take_command()
                                f2 = open('testdata.json')
                                data2 = json.load(f2)
                                code = data2["response"][0]["keycode"]
                                keycode = code
                                if keycode in command:
                                    test_question_results()
                            else:
                                break

                        else:
                            test_questions()        # Test questions
                            if 'yes' in command:
                                talk('Please clearly sate your keycode. Beep Boop')     # Asks user to state their test keycode
                                command = take_command()
                                f2 = open('testdata.json')
                                data2 = json.load(f2)
                                code = data2["response"][0]["keycode"]
                                keycode = code
                                if keycode in command:
                                    test_question_results()
                            else:
                                break

                    else:
                        talk('Error. Wrong keycode')
                else:       # Launches Surpass again
                    command = take_command()
                    talk('Would you like to take a test or hear the results of a previous test?')
                    talk("Say 'one' for taking a test. And 'two' for results. Beep Boop")   # 'Beep Boop' sound effects will occur at the end of a sentence to indicate when the person can respond
                    print(command)

        if '2' in command:      # Asks if the user chose the correct option
            talk('Are you sure you would like to hear the results of a previous test? Beep Boop')
            if 'yes' in command:
                talk('Please state the keycode for the test you like the results for. Beep Boop')   # Asks user to state their test keycode
                command = take_command()
                file = open('testdata.json')
                load_data = json.load(file)
                code1 = load_data["response"][0]["keycode"]
                keycode1 = code1
                if keycode1 in command:
                    file1 = open('testdata.json')
                    results_data1 = json.load(file1)
                    results_mark = results_data1["response"][0]["mark"]
                    results_perc = results_data1["response"][0]["percentage"]
                    results_grade = results_data1["response"][0]["grade"]
                    talk('Here are your test results. Your mark was' + results_mark)
                    talk('Your percentage was' + results_perc)
                    talk('Your grade was' + results_grade)

            else:       # Launches Surpass again
                command = take_command()
                talk('Would you like to take a test or hear the results of a previous test?')
                talk("Say 'one' for taking a test. And 'two' for results. Beep Boop")   # 'Beep Boop' sound effects will occur at the end of a sentence to indicate when the person can respond
                print(command)
        else:
            talk('You did not choose a correct option. Beep Boop')

    if 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time + 'Beep Boop')
    else:
        talk('Error. Please say the command again.')
