from tkinter import Tk, messagebox
import time
from datetime import date, datetime
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

sarcastic_messages = [
    "Another day of outward smiles and inward screams is starting.",
    "Sometimes the best part of the job is that the chair swivels.",
    "When work feels overwhelming, remember you're going to die.",
    "It's never too early to start dreading Monday.",
    "Mentally check out of work for the week.",
    "On this beautiful day, take a break from crying at your desk to cry outside.",
    "Get another coffee."
]

# function to print out messages
def motivate_me():
    # choose a random message from the list
    random_message = messages[randint(0, len(messages) - 1)]

    Tk().wm_withdraw()
    messagebox.showinfo(
        title = "work motivation",
        message = random_message + "\nKeep on working!"
    )

    return "Motivation boost!"


if __name__ == "__main__":
    while True:
        time.sleep(timer)
        motivate_me()