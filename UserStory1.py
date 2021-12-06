import speech_recognition as sr
import pyttsx3
import datetime
import json

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


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


#def test_questions():       # Test questions
'''
    f4 = open('testdata.json')
    data4 = json.load(f4)
    questionname1 = data4["response"][0]["sections"]["items"]["name1"]
    question1 = data4["response"][0]["sections"]["items"]["Question1"]
    questionname2 = data4["response"][0]["sections"]["items"]["name2"]
    question2 = data4["response"][0]["sections"]["items"]["Question2"]
    questionname3 = data4["response"][0]["sections"]["items"]["name3"]
    question3 = data4["response"][0]["sections"]["items"]["Question3"]
    options1 = data4["response"][0]["sections"]["items"]["Options1"]
    options2 = data4["response"][0]["sections"]["items"]["Options2"]
    options3 = data4["response"][0]["sections"]["items"]["Options3"]
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
        if 'A' in command:
            print(command)
            f5 = open('testdata.json', 'w')
            data4 = json.load(f5)
            response1 = data4["response"][0]["sections"]["items"]["CandidateResponse1"]["value1"]
            response1.write('A')
        if 'B' in command:
            print(command)
            f5 = open('testdata.json', 'w')
            data4 = json.load(f5)
            response1 = data4["response"][0]["sections"]["items"]["CandidateResponse1"]["value1"]
            response1.write('B')
        if 'C' in command:
            print(command)
            f5 = open('testdata.json', 'w')
            data4 = json.load(f5)
            response1 = data4["response"][0]["sections"]["items"]["CandidateResponse1"]["value1"]
            response1.write('C')
    elif 'no' in command:
        command = take_command()
        talk('Please sate your answer. A, B, or C. Beep Boop')
        if 'A' in command:
            print(command)
            f5 = open('testdata.json', 'w')
            data4 = json.load(f5)
            response1 = data4["response"][0]["sections"]["items"]["CandidateResponse1"]["value1"]
            response1.write('A')
        if 'B' in command:
            print(command)
            f5 = open('testdata.json', 'w')
            data4 = json.load(f5)
            response1 = data4["response"][0]["sections"]["items"]["CandidateResponse1"]["value1"]
            response1.write('B')
        if 'C' in command:
            print(command)
            f5 = open('testdata.json', 'w')
            data4 = json.load(f5)
            response1 = data4["response"][0]["sections"]["items"]["CandidateResponse1"]["value1"]
            response1.write('C')
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
        if 'A' in command:
            print(command)
            f5 = open('testdata.json', 'w')
            data4 = json.load(f5)
            response1 = data4["response"][0]["sections"]["items"]["CandidateResponse2"]["value2"]
            response1.write('A')
        if 'B' in command:
            print(command)
            f5 = open('testdata.json', 'w')
            data4 = json.load(f5)
            response1 = data4["response"][0]["sections"]["items"]["CandidateResponse2"]["value2"]
            response1.write('B')
        if 'C' in command:
            print(command)
            f5 = open('testdata.json', 'w')
            data4 = json.load(f5)
            response1 = data4["response"][0]["sections"]["items"]["CandidateResponse2"]["value2"]
            response1.write('C')
    elif 'no' in command:
        command = take_command()
        talk('Please sate your answer. A, B, or C. Beep Boop')
        if 'A' in command:
            print(command)
            f5 = open('testdata.json', 'w')
            data4 = json.load(f5)
            response1 = data4["response"][0]["sections"]["items"]["CandidateResponse2"]["value2"]
            response1.write('A')
        if 'B' in command:
            print(command)
            f5 = open('testdata.json', 'w')
            data4 = json.load(f5)
            response1 = data4["response"][0]["sections"]["items"]["CandidateResponse2"]["value2"]
            response1.write('B')
        if 'C' in command:
            print(command)
            f5 = open('testdata.json', 'w')
            data4 = json.load(f5)
            response1 = data4["response"][0]["sections"]["items"]["CandidateResponse2"]["value2"]
            response1.write('C')
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
        if 'A' in command:
            print(command)
            f5 = open('testdata.json', 'w')
            data4 = json.load(f5)
            response1 = data4["response"][0]["sections"]["items"]["CandidateResponse3"]["value3"]
            response1.write('A')
        if 'B' in command:
            print(command)
            f5 = open('testdata.json', 'w')
            data4 = json.load(f5)
            response1 = data4["response"][0]["sections"]["items"]["CandidateResponse3"]["value3"]
            response1.write('B')
        if 'C' in command:
            print(command)
            f5 = open('testdata.json', 'w')
            data4 = json.load(f5)
            response1 = data4["response"][0]["sections"]["items"]["CandidateResponse3"]["value3"]
            response1.write('C')
    elif 'no' in command:
        command = take_command()
        talk('Please sate your answer. A, B, or C. Beep Boop')
        if 'A' in command:
            print(command)
            f5 = open('testdata.json', 'w')
            data4 = json.load(f5)
            response1 = data4["response"][0]["sections"]["items"]["CandidateResponse3"]["value3"]
            response1.write('A')
        if 'B' in command:
            print(command)
            f5 = open('testdata.json', 'w')
            data4 = json.load(f5)
            response1 = data4["response"][0]["sections"]["items"]["CandidateResponse3"]["value3"]
            response1.write('B')
        if 'C' in command:
            print(command)
            f5 = open('testdata.json', 'w')
            data4 = json.load(f5)
            response1 = data4["response"][0]["sections"]["items"]["CandidateResponse3"]["value3"]
            response1.write('C')
'''

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
                command = take_command()

                if 'yes' in command:
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
                            #test_questions()
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
                                talk('Please sate your answer. A, B, or C. Beep Boop')
                                command = take_command()

                                if 'A' in command:
                                    print('A')
                                    #f5 = open('testdata.json', 'w')
                                    #data4 = json.load(f5)
                                    #response1 = data4["response"][0]["sections"]["items"]["CandidateResponse1"]["value1"]
                                    #response1.write('A')
                                if 'B' in command:
                                    print('B')
                                    #f5 = open('testdata.json', 'w')
                                    #data4 = json.load(f5)
                                    #response1 = data4["response"][0]["sections"]["items"]["CandidateResponse1"]["value1"]
                                    #response1.write('B')
                                if 'C' in command:
                                    print('C')
                                    #f5 = open('testdata.json', 'w')
                                    #data4 = json.load(f5)
                                    #response1 = data4["response"][0]["sections"]["items"]["CandidateResponse1"]["value1"]
                                    #response1.write('C')

                            elif 'no' in command:
                                command = take_command()
                                talk('Please sate your answer. A, B, or C. Beep Boop')
                                if 'A' in command:
                                    print('A')
                                    #f5 = open('testdata.json', 'w')
                                    #data4 = json.load(f5)
                                    #response1 = data4["response"][0]["sections"]["items"]["CandidateResponse1"]["value1"]
                                    #response1.write('A')
                                if 'B' in command:
                                    print('B')
                                    #f5 = open('testdata.json', 'w')
                                    #data4 = json.load(f5)
                                    #response1 = data4["response"][0]["sections"]["items"]["CandidateResponse1"]["value1"]
                                    #response1.write('B')
                                if 'C' in command:
                                    print('C')
                                    #f5 = open('testdata.json', 'w')
                                    #data4 = json.load(f5)
                                    #response1 = data4["response"][0]["sections"]["items"]["CandidateResponse1"]["value1"]
                                    #response1.write('C')

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

                                if 'A' in command:
                                    print('A')
                                    #f5 = open('testdata.json', 'w')
                                    #data4 = json.load(f5)
                                    #response2 = data4["response"][0]["sections"]["items"]["CandidateResponse1"]["value2"]
                                    #response2.write('A')
                                if 'B' in command:
                                    print('B')
                                    #f5 = open('testdata.json', 'w')
                                    #data4 = json.load(f5)
                                    #response2 = data4["response"][0]["sections"]["items"]["CandidateResponse1"]["value2"]
                                    #response2.write('B')
                                if 'C' in command:
                                    print('C')
                                    #f5 = open('testdata.json', 'w')
                                    #data4 = json.load(f5)
                                    #response2 = data4["response"][0]["sections"]["items"]["CandidateResponse1"]["value2"]
                                    #response2.write('C')

                            elif 'no' in command:
                                command = take_command()
                                talk('Please sate your answer. A, B, or C. Beep Boop')
                                if 'A' in command:
                                    print('A')
                                    #f5 = open('testdata.json', 'w')
                                    #data4 = json.load(f5)
                                    #response2 = data4["response"][0]["sections"]["items"]["CandidateResponse1"]["value2"]
                                    #response2.write('A')
                                if 'B' in command:
                                    print('B')
                                    #f5 = open('testdata.json', 'w')
                                    #data4 = json.load(f5)
                                    #response2 = data4["response"][0]["sections"]["items"]["CandidateResponse1"]["value2"]
                                    #response2.write('B')
                                if 'C' in command:
                                    print('C')
                                    #f5 = open('testdata.json', 'w')
                                    #data4 = json.load(f5)
                                    #response2 = data4["response"][0]["sections"]["items"]["CandidateResponse1"]["value2"]
                                    #response2.write('C')

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
                                if 'A' in command:
                                    print('A')
                                    #f5 = open('testdata.json', 'w')
                                    #data4 = json.load(f5)
                                    #response3 = data4["response"][0]["sections"]["items"]["CandidateResponse1"]["value3"]
                                    #response3.write('A')
                                if 'B' in command:
                                    print('B')
                                    #f5 = open('testdata.json', 'w')
                                    #data4 = json.load(f5)
                                    #response3 = data4["response"][0]["sections"]["items"]["CandidateResponse1"]["value3"]
                                    #response3.write('B')
                                if 'C' in command:
                                    print('C')
                                    #f5 = open('testdata.json', 'w')
                                    #data4 = json.load(f5)
                                    #response3 = data4["response"][0]["sections"]["items"]["CandidateResponse1"]["value3"]
                                    #response3.write('C')

                            elif 'no' in command:
                                command = take_command()
                                talk('Please sate your answer. A, B, or C. Beep Boop')
                                if 'A' in command:
                                    print('A')
                                    #f5 = open('testdata.json', 'w')
                                    #data4 = json.load(f5)
                                    #response3 = data4["response"][0]["sections"]["items"]["CandidateResponse1"]["value3"]
                                    #response3.write('A')
                                if 'B' in command:
                                    print('B')
                                    #f5 = open('testdata.json', 'w')
                                    #data4 = json.load(f5)
                                    #response3 = data4["response"][0]["sections"]["items"]["CandidateResponse1"]["value3"]
                                    #response3.write('B')
                                if 'C' in command:
                                    print('C')
                                    #f5 = open('testdata.json', 'w')
                                    #data4 = json.load(f5)
                                    #response3 = data4["response"][0]["sections"]["items"]["CandidateResponse1"]["value3"]
                                    #response3.write('C')

                        else:
                            # test_questions()   Test questions
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
                                if 'A' in command:
                                    print('A')
                                    #f5 = open('testdata.json', 'w')
                                    #data4 = json.load(f5)
                                    #response1 = data4["response"][0]["sections"]["items"]["CandidateResponse1"]["value1"]
                                    #response1.write('A')
                                if 'B' in command:
                                    print('B')
                                    #f5 = open('testdata.json', 'w')
                                    #data4 = json.load(f5)
                                    #response1 = data4["response"][0]["sections"]["items"]["CandidateResponse1"]["value1"]
                                    #response1.write('B')
                                if 'C' in command:
                                    print('C')
                                    #f5 = open('testdata.json', 'w')
                                    #data4 = json.load(f5)
                                    #response1 = data4["response"][0]["sections"]["items"]["CandidateResponse1"]["value1"]
                                    #response1.write('C')
                            elif 'no' in command:
                                command = take_command()
                                talk('Please sate your answer. A, B, or C. Beep Boop')
                                if 'A' in command:
                                    print('A')
                                    #f5 = open('testdata.json', 'w')
                                    #data4 = json.load(f5)
                                    #response1 = data4["response"][0]["sections"]["items"]["CandidateResponse1"]["value1"]
                                    #response1.write('A')
                                if 'B' in command:
                                    print('B')
                                    #f5 = open('testdata.json', 'w')
                                    #data4 = json.load(f5)
                                    #response1 = data4["response"][0]["sections"]["items"]["CandidateResponse1"]["value1"]
                                    #response1.write('B')
                                if 'C' in command:
                                    print('C')
                                    #f5 = open('testdata.json', 'w')
                                    #data4 = json.load(f5)
                                    #response1 = data4["response"][0]["sections"]["items"]["CandidateResponse1"]["value1"]
                                    #response1.write('C')
                            talk('This is' + questionname2)
                            talk(question2)
                            talk(options2)
                            talk('Would you like the question repeated? Beep Boop')
                            command = take_command()
                            if 'yes' in command:
                                talk('This is' + questionname2)
                                talk(question2)
                                talk(options2)
                                talk('Please sate your answer. A, B, or C. Beep Boop')
                                command = take_command()
                                if 'A' in command:
                                    print('A')
                                    #f5 = open('testdata.json', 'w')
                                    #data4 = json.load(f5)
                                    #response2 = data4["response"][0]["sections"]["items"]["CandidateResponse1"]["value2"]
                                    #response2.write('A')
                                if 'B' in command:
                                    print('B')
                                    #f5 = open('testdata.json', 'w')
                                    #data4 = json.load(f5)
                                    #response2 = data4["response"][0]["sections"]["items"]["CandidateResponse1"]["value2"]
                                    #response2.write('B')
                                if 'C' in command:
                                    print('C')
                                    #f5 = open('testdata.json', 'w')
                                    #data4 = json.load(f5)
                                    #response2 = data4["response"][0]["sections"]["items"]["CandidateResponse1"]["value2"]
                                    #response2.write('C')
                            elif 'no' in command:
                                command = take_command()
                                talk('Please sate your answer. A, B, or C. Beep Boop')
                                if 'A' in command:
                                    print('A')
                                    #f5 = open('testdata.json', 'w')
                                    #data4 = json.load(f5)
                                    #response2 = data4["response"][0]["sections"]["items"]["CandidateResponse1"]["value2"]
                                    #response2.write('A')
                                if 'B' in command:
                                    print('B')
                                    #f5 = open('testdata.json', 'w')
                                    #data4 = json.load(f5)
                                    #response2 = data4["response"][0]["sections"]["items"]["CandidateResponse1"]["value2"]
                                    #response2.write('B')
                                if 'C' in command:
                                    print('C')
                                    #f5 = open('testdata.json', 'w')
                                    #data4 = json.load(f5)
                                    #response2 = data4["response"][0]["sections"]["items"]["CandidateResponse1"]["value2"]
                                    #response2.write('C')
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
                                if 'A' in command:
                                    print('A')
                                    #f5 = open('testdata.json', 'w')
                                    #data4 = json.load(f5)
                                    #response3 = data4["response"][0]["sections"]["items"]["CandidateResponse1"]["value3"]
                                    #response3.write('A')
                                if 'B' in command:
                                    print('B')
                                    #f5 = open('testdata.json', 'w')
                                    #data4 = json.load(f5)
                                    #response3 = data4["response"][0]["sections"]["items"]["CandidateResponse1"]["value3"]
                                    #response3.write('B')
                                if 'C' in command:
                                    print('C')
                                    #f5 = open('testdata.json', 'w')
                                    #data4 = json.load(f5)
                                    #response3 = data4["response"][0]["sections"]["items"]["CandidateResponse1"]["value3"]
                                    #response3.write('C')
                                elif 'no' in command:
                                    command = take_command()
                                talk('Please sate your answer. A, B, or C. Beep Boop')
                                if 'A' in command:
                                    print('A')
                                    #f5 = open('testdata.json', 'w')
                                    #data4 = json.load(f5)
                                    #response3 = data4["response"][0]["sections"]["items"]["CandidateResponse1"]["value3"]
                                    #response3.write('A')
                                if 'B' in command:
                                    print('B')
                                    #f5 = open('testdata.json', 'w')
                                    #data4 = json.load(f5)
                                    #response3 = data4["response"][0]["sections"]["items"]["CandidateResponse1"]["value3"]
                                    #response3.write('B')
                                if 'C' in command:
                                    print('C')
                                    #f5 = open('testdata.json', 'w')
                                    #data4 = json.load(f5)
                                    #response3 = data4["response"][0]["sections"]["items"]["CandidateResponse1"]["value3"]
                                    #response3.write('C')

                    else:
                        talk('Error. Wrong keycode')
                else:       # Launches Surpass again
                    command = take_command()
                    talk('Would you like to take a test or hear the results of a previous test?')
                    talk("Say 'one' for taking a test. And 'two' for results. Beep Boop")   # 'Beep Boop' sound effects will occur at the end of a sentence to indicate when the person can respond
                    print(command)

        if '2' in command:      # Asks if the user chose the correct option
            talk('Are you sure you would like to hear the results of a previous test? Beep Boop')
            #if 'yes' in command:
            #    talk('Please state the keycode for the test you like the results for. Beep Boop')   # Asks user to state their test keycode
            #    command = take_command()
            #    file = open('testdata.json')
            #    load_data = json.load(file)
            #    code1 = load_data["response"][0]["keycode"]
            #    keycode1 = code1
            #    if keycode1 in command:
            #        file1 = open('testdata.json')
            #        results_data1 = json.load(file1)
            #        results_mark = results_data1["response"][0]["mark"]
            #        results_perc = results_data1["response"][0]["percentage"]
            #        results_grade = results_data1["response"][0]["grade"]
            #        talk('Here are your test results. Your mark was' + results_mark)
            #        talk('Your percentage was' + results_perc)
            #        talk('Your grade was' + results_grade)

            #else:       # Launches Surpass again
            #    command = take_command()
            #    talk('Would you like to take a test or hear the results of a previous test?')
            #    talk("Say 'one' for taking a test. And 'two' for results. Beep Boop")   # 'Beep Boop' sound effects will occur at the end of a sentence to indicate when the person can respond
            #    print(command)
        else:
            talk('You did not choose a correct option. Beep Boop')

    if 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time + 'Beep Boop')
    else:
        talk('Error. Please say the command again.')
