from flask import Flask
from flask_ask import Ask, statement, question, session
import os
import random
import csv, sqlite3
#from rMinus3 import *
import time

app = Flask(__name__)
ask = Ask(app, "/darwin")

encode = {"walk":'1', "balance":2, "stand":'2'}


@app.route('/')
def homepage():
    return "hi there, how ya doin?"

@ask.launch
def start_skill():
    welcome_message = 'Hello there! would you like me to do something for you?'
    return question(welcome_message)

def execute(motion):
    print motion
    flag = True
    with open('file.txt', 'r') as file:
        value = file.read()
        if value != '-1' and len(value) != 0:
            flag = False
    if flag:
        with open('file.txt','w') as file:
            file.write(encode[motion])
    

@ask.intent("AMAZON.YesIntent")
def yes_intent():
    message = "What is it that you would like me to do ?"
    return question(message)


@ask.intent("DoMotion", mapping={'motion':'Action'})
def do_motion(motion):
    message = ["Sure Thing!", "Okay, watch me "+ motion, "Will do that", "Whatever you ask.."]
    execute(motion)
    message = random.choice(message)+ '.... Anything else ?'
    return question(message)

@ask.intent("AMAZON.NoIntent")
@ask.intent("AMAZON.StopIntent")
def stop():
    message = ['See you soon!', 'Bye, see you later', 'Have a good Day!']
    message = random.choice(message)
    return statement(message)
    
if __name__ == '__main__':
    #time.sleep(1)
    app.run(debug=True)
