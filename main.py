import tkinter.messagebox
from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- FOCUS WINDOW ------------------------------ #

def focus_window(option):
    if option == "on":
        window.deiconify()
        window.focus_force()
        window.attributes('-topmost', 1)
    elif option == "off":
        window.attributes('-topmost', 0)

# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    start_button.config(state='normal')
    reset_button.config(state='disabled')
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text='00:00')
    title_label.config(text='Timer', fg=GREEN)
    checkmark.config(text='')
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    start_button.config(state='disabled')
    reset_button.config(state='normal')
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    shot_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 2 == 1:
        #tkinter.messagebox.showinfo(title='Work', message='Start working!')
        countdown(work_sec)
        title_label.config(text='Work', fg=GREEN)
        focus_window('off')
    elif reps % 8 == 0:
        focus_window('on')
        #tkinter.messagebox.showinfo(title='Break', message='Long break!')
        countdown(long_break_sec)
        title_label.config(text='Break', fg=RED)
    else:
        focus_window('on')
        #tkinter.messagebox.showinfo(title='Work', message='Short break!')
        countdown(shot_break_sec)
        title_label.config(text='Break', fg=YELLOW)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def countdown(count):
    global timer
    count_minute = math.floor(count / 60)
    count_second = count % 60
    if count_second < 10:
        count_second = f'0{count_second}'

    canvas.itemconfig(timer_text, text=f'{count_minute}:{count_second}')
    if count > 0:
        timer = window.after(1000, countdown, count-1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps / 2)
        for i in range(work_sessions):
            mark += "✔"
        checkmark.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=PINK)


canvas = Canvas(width=200, height=224, bg=PINK, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 30, 'bold'))
canvas.grid(column=1, row=1)

title_label = Label(text='Timer', fg=GREEN, bg=PINK, font=(FONT_NAME, 50, 'bold'))
title_label.grid(column=1, row=0)

checkmark = Label(fg=GREEN, bg=PINK, font=(FONT_NAME, 25))
checkmark.grid(column=1, row=3)

start_button = Button(text='Start', font=(FONT_NAME, 10, 'bold'), highlightthickness=0, command=start_timer, state='normal')
start_button.grid(column=0, row=2)

reset_button = Button(text='Reset', font=(FONT_NAME, 10, 'bold'), highlightthickness=0, command=reset_timer, state='disabled')
reset_button.grid(column=2, row=2)





window.mainloop()
