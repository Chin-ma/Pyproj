import random
import time
import os
from win10toast import ToastNotifier
jokes = ["Alright! I took the quiz and it turns out I do put career over men.",
         "Yes, on a scale of one to 10, 10 being the dumbest a person can look, you are definitely 19",
         "I'm not great at advice. Can I interest you with a sarcastic comment?",
         "Ok, you have to stop the Q-tip when there's resistance!",
         "What do you know? You're a door. You only like knock knock jokes.",
         "Until I was 25, I thought that the only response to 'I love you' was 'Oh, crap!'"]

facts = ["Yawning Cools Your Brain",
         "It Takes 68 Days to Swim the Full Length of the Mississippi River",
         "Fleas Are Among the World's Best Jumpers",
         "An Apple Can Last up to 10 Months",
         "The Creator of the Pringles Can is Buried in One",
         "The Wizard of Oz's Full Name is Oscar Zoroaster Phadrig Isaac Norman Henkel Emmannuel Ambroise Diggs",
         "Penguins Used to Be Six Feet Tall",
         "A Brewery in Canada Makes Beer Using Water from 20,000-Year-Old Icebergs",
         "The Letter Z Was Removed from the Alphabet for 200 Years"]

rps = ["rock","paper","scissor"]

dice = ["1","2","3","4","5","6"]

def notify():
    notifTime = input("Input time in 24hr format(HH:MM:SS) to set reminder")
    notMessage = input("Enter your message: ")
    while True:
        current_time = time.strftime("%H:%M:%S")
        if current_time == notifTime:
            # print(current_time)
            break
    
    notify = ToastNotifier()
    notify.show_toast("Notification",notMessage)

while True:
    message = input('Human: ')

    if 'who' in message and 'you' in message:
        reply = "Hello, I'm Someone."
    # FACTS
    elif 'fact' in message:
        reply = random.choice(facts)
    # ROCK PAPER SCISSOR
    elif 'rock' in message or 'paper' in message or 'scissor' in message:
        reply = random.choice(rps)
        if message == 'rock' and reply == 'paper':
            print("***You win!!***")
        elif message == 'rock' and reply == 'scissor':
            print("***You Lose :(:(***")
        elif message == 'paper' and reply == 'scissor':
            print("***You Lose :(:(***")
        elif message == 'paper' and reply == 'rock':
            print("***You Win!!***")
        elif message == 'scissor' and reply == 'rock':
            print("***You Lose :(:(***")
        elif message == 'scissor' and reply == 'paper':
            print("***You Win!!***")
    # ROLL THE DICE
    elif 'roll dice' in message or 'dice' in message or 'dice roll' in message:
        reply = random.choice(dice)
    # OPEN ANY FILE
    elif 'open' in message or 'app' in message:
        reply = str(os.system(input()))
    # SET SOME NOTIFICATION
    elif 'notify' in message or 'notify me' in message:
        reply = str(notify())
    # EDIOTIC JOKES
    elif 'joke' in message:
        reply = random.choice(jokes)
    # STOP THE ASSISTANT
    elif 'exit' in message or 'stop' in message:
        reply = exit(0)
    # GUESS GAME
    elif 'number guess' in message or 'guess game' in message or 'number game' in message or 'guess the number' in message:
        print("Think of a number between 1 and 10!")
        time.sleep(5)
        print("Multiply it by two")
        time.sleep(5)
        print("Add 10 to obtained number")
        time.sleep(7)
        print("Divide the answer by 2")
        time.sleep(6)
        print("Subtract original number from obtained number")
        time.sleep(5)
        reply = "The answer is 5"
    else:
        reply = "Blah blah blah"
    print('Bot: ' + reply)
