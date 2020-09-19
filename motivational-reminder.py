from tkinter import Tk
from tkinter import messagebox
import time
from random import randint

# set timeout to 60 minutes
timer = 3600

# add messages to be printed out 
messages = [
    "You can do anything.",
    "Believe you can and you're halfway there.",
    "Now is your time to shine.",
    "It's kind of fun to do the impossible.",
    "Good things come to those who hustle.",
    "A winner is a dreamer who never gives up.",
    "Inspiration is everywhere",
    "Think it. Want it. Get it."
]

def motivate_me():
    random_msg = messages[randint(0, len(messages) - 1)]

    Tk().wm_withdraw()
    messagebox.showinfo(
        title = "work motivation",
        message = random_msg + "\nKeep on working!")

    return "Motivation boost!"


if __name__ == "__main__":
    while True:
        time.sleep(timer)
        motivate_me()
