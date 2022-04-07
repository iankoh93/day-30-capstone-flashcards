import time

BACKGROUND_COLOR = "#B1DDC6"

# Import modules
from tkinter import *
from tkinter import messagebox
import random
import json
from pandas import *

current_card = {}
known_words = {}

try:
    word_data = read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    word_data = read_csv("data/french_words.csv")
finally:
    word_list = word_data.to_dict(orient="records")

# --------------- New Random Word Function --------------- #
def new_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    canvas.itemconfig(card, image=front)
    current_card = random.choice(word_list)
    french_word = current_card["French"]
    canvas.itemconfig(title_text, text="French")
    canvas.itemconfig(word_text, text=f"{french_word}", fill="black")
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    global current_card
    canvas.itemconfig(title_text, text="English")
    english_word = current_card["English"]
    canvas.itemconfig(card, image=back)
    canvas.itemconfig(word_text, text=f"{english_word}", fill="white")


def correct():
    word_list.remove(current_card)
    words_to_learn = DataFrame(word_list)
    words_to_learn.to_csv("data/words_to_learn.csv", index=False)
    new_word()


def wrong():
    new_word()


# --------------- UI --------------- #
window = Tk()
window.title("Flashcard Trainer")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
front = PhotoImage(file="images/card_front.png")
back = PhotoImage(file="images/card_back.png")
card = canvas.create_image(800 / 2, 526 / 2, image=front)
canvas.grid(row=0, column=0, columnspan=3)
title_text = canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="Start", font=("Ariel", 60, "bold"))

correct_img = PhotoImage(file="images/right.png")
button_correct = Button(image=correct_img, bg=BACKGROUND_COLOR, highlightthickness=0, command=correct)
button_correct.grid(row=1, column=0)

wrong_img = PhotoImage(file="images/wrong.png")
button_wrong = Button(image=wrong_img, bg=BACKGROUND_COLOR, highlightthickness=0, command=wrong)
button_wrong.grid(row=1, column=2)

new_word()

window.mainloop()
