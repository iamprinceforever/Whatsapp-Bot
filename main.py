import pyautogui as pt
from time import sleep
import pyperclip
import random

sleep(5)
position1= pt.locateOnScreen("emojis.png", confidence=.6)
x = position1[0]
y = position1[1]

#Gets Message
def get_message():
    global x, y
    position = pt.locateOnScreen("emojis.png", confidence=.6)
    x = position[0]
    y = position[1]
    pt.moveTo(x,y)
    pt.moveTo(x+100,y-36)
    pt.tripleClick()
    pt.rightClick()
    pt.moveRel(12,-93)
    sleep(.5)
    pt.click()
    whatsapp_message = pyperclip.paste()
    pt.click()
    print("Message Received: "+ whatsapp_message)

    return whatsapp_message
#Posts
def post_response(message):
    global x,y
    position = pt.locateOnScreen("emojis.png", confidence=.6)
    x = position[0]
    y = position[1]
    pt.moveTo(x+200,y+20)
    pt.click()
    pt.typewrite(message, interval=.01)
    pt.typewrite("\n", interval=.01)

#Processes Response
def process_response(message):
    if "?" in str(message).lower():   
        return "We will inform Prince about that" 
    elif message.startswith('Ok'):                  #startswith  returns True if a string starts with the specified prefix(string)
        return "Yeah"
    elif message.startswith('Oh'):                  #startswith  returns True if a string starts with the specified prefix(string)
        return "Yeah"
    elif message.startswith('K'):                  #startswith  returns True if a string starts with the specified prefix(string)
        return "Yeah"
    elif message.startswith('Ss'):                  #startswith  returns True if a string starts with the specified prefix(string)
        return "Yeah"
    elif message.startswith('Ha'):                  #startswith  returns True if a string starts with the specified prefix(string)
        return "Yeah"
    elif message.startswith('Ha ok'):                  #startswith  returns True if a string starts with the specified prefix(string)
        return "Yeah"
    elif message.startswith('Ray'):                  #startswith  returns True if a string starts with the specified prefix(string)
        return "Please use English For Communication. I am yet to Learn Telugu."
    elif message.startswith('Can you'):                  #startswith  returns True if a string starts with the specified prefix(string)
        return "Please use (?) for question"
    elif message.startswith('Hi'):
        return "You're Talking to J.A.R.V.I.S (Prince Nikhilesh's Personal Assistant). He is Currently Busy. Please leave a message here :).Please use (?) if you have any question"
    elif message.startswith('Hello'):
        return "You're Talking to J.A.R.V.I.S (Prince Nikhilesh's Personal Assistant). He is Currently Busy. Please leave a message here :).Please use (?) if you have any question"
    elif message.startswith('Heyy'):
        return "You're Talking to J.A.R.V.I.S (Prince Nikhilesh's Personal Assistant). He is Currently Busy. Please leave a message here :).Please use (?) if you have any question"
    elif message.startswith('Hey'):
        return "You're Talking to J.A.R.V.I.S (Prince Nikhilesh's Personal Assistant). He is Currently Busy. Please leave a message here :).Please use (?) if you have any question"

#Checks for New Messages
def check_for_new_messages():
    pt.moveTo(x+100,y-25)
    while True:
        #Continuously Checks for Green Dots and New Messages
        try:
            position= pt.locateOnScreen("unread.png", confidence=.8)
            if position is not None:
                pt.moveTo(position)
                pt.moveRel(-11,0)
                pt.click()
                sleep(.5)
        except(Exception):
            print("No New Messages Detected")
        if pt.pixelMatchesColor(int(x+100), int(y-25),(255,255,255),tolerance=10):
            print("is_white")
            processed_message= process_response(get_message())
            post_response(processed_message)
        else:
            print("No New Messages yet...")
        sleep(6)
check_for_new_messages()
#processed_message = process_response(get_message())
#post_response(processed_message)
