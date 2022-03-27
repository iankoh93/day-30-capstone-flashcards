BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *
from tkinter import messagebox
import random
import json


# --------------- UI -------------------- #
window = Tk()
window.title("Flashcard Trainer")
window.config(padx=50, pady=50, bg="#9bdeac")

canvas = Canvas(height=526, width=800)
front = PhotoImage(file="images/card_front.png")
title_text = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="Title", font=("Ariel", 60, "bold"))
canvas.create_image(800/2, 526/2, image=front)
canvas.grid(row=0, column=0, columnspan=3)

correct_img = PhotoImage(file="images/right.png")
button_correct = Button(image=correct_img)
button_correct.grid(row=2, column=0)
wrong_img = PhotoImage(file="images/wrong.png")
button_wrong = Button(image=wrong_img)
button_wrong.grid(row=2, column=2)

window.mainloop()
