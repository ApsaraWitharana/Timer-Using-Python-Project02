
import math
from tkinter import *
import itertools

# ---------------------------- CONSTANTS ------------------------------- #
BLACK = "#000000"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.1
SHORT_BREAK_MIN = 0.1
LONG_BREAK_MIN = 10
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def restart_timer():
    global timer
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label_timer.config(text="Timer")
    label_mark.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    if reps == 8:
        reps = 1
    else:
        reps += 1
    print(reps)

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        label_timer.config(text="Break", fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        label_timer.config(text="Break", fg=BLACK)
        count_down(short_break_sec)
    else:
        label_timer.config(text="Work", fg=GREEN)
        count_down(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global reps
    global timer
    global anim_cycle
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    if count > 0:
        canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
        # Animate by changing the image periodically
        canvas.itemconfig(timer_image, image=next(anim_cycle))
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps % 2 != 0:
            label_mark.config(text="✔" * ((reps - 1) // 2))

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title(" Timer")
window.config(padx=100, pady=100, bg=YELLOW)

label_timer = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 40), bg=YELLOW)
label_timer.grid(row=1, column=2)

# Load animation images
animation_images = ["img_1.png", "img2.png", "img3.png"]  # Replace with your actual image filenames
loaded_images = [PhotoImage(file=image) for image in animation_images]
anim_cycle = itertools.cycle(loaded_images)

canvas = Canvas(width=210, height=230, bg=YELLOW, highlightthickness=0)
timer_image = canvas.create_image(103, 100, image=next(anim_cycle))
timer_text = canvas.create_text(103, 125, text="00:00", font=(FONT_NAME, 30, "bold"), fill="black")
canvas.grid(row=2, column=2)

button_start = Button(text="Start", bg="red", font=(FONT_NAME, 15, "bold"), highlightthickness=0,
                      command=start_timer)
button_start.grid(row=3, column=1)

button_reset = Button(text="Reset", bg="green", font=(FONT_NAME, 15, "bold"), highlightthickness=0,
                      command=restart_timer)
button_reset.grid(row=3, column=3)

label_mark = Label(font=(FONT_NAME, 25, "bold"), bg=YELLOW, fg=GREEN)
label_mark.grid(row=4, column=2)

window.mainloop()



