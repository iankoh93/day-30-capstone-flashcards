BACKGROUND_COLOR = "#B1DDC6"

# Import modules
from tkinter import *
from tkinter import messagebox
import random
import json
from pandas import *


# --------------- New Random Word Function --------------- #
def new_word():
    word_data = read_csv("data/french_words.csv")
    word_dict = word_data.to_dict()
    rand_num = random.randint(0, len(word_dict["French"])-1)
    french_word = word_dict["French"][rand_num]
    english_word = word_dict["English"][rand_num]
    canvas.itemconfig(word_text, text=f"{french_word}")


# --------------- UI --------------- #
window = Tk()
window.title("Flashcard Trainer")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
front = PhotoImage(file="images/card_front.png")
canvas.create_image(800 / 2, 526 / 2, image=front)
canvas.grid(row=0, column=0, columnspan=3)
title_text = canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="Start", font=("Ariel", 60, "bold"))

correct_img = PhotoImage(file="images/right.png")
button_correct = Button(image=correct_img, bg=BACKGROUND_COLOR, highlightthickness=0, command=new_word)
button_correct.grid(row=1, column=0)

wrong_img = PhotoImage(file="images/wrong.png")
button_wrong = Button(image=wrong_img, bg=BACKGROUND_COLOR, highlightthickness=0, command=new_word)
button_wrong.grid(row=1, column=2)

window.mainloop()
