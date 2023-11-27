'''mod'''
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

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    '''func'''
    window.after_cancel(timer)
    canvas.itemconfig(time_text, text="00:00")
    title_label.config(text="Timer")
    check.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    '''func'''
    global reps
    reps+=1

    work_sec=WORK_MIN*60
    short_break_sec=SHORT_BREAK_MIN*60
    long_break_sec=LONG_BREAK_MIN*60

    #-------------------#
    if reps%8==0:
        count_down(long_break_sec)
        title_label.config(text="Break", fg=RED)
    #-------------------#
    elif reps%2==0:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)
    #-------------------#
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    '''func'''
    count_min = math.floor(count/60)
    if count_min < 10:
        count_min=f"0{count_min}"
    count_sec = count%60
    if count_sec < 10:
        count_sec=f"0{count_sec}"

    canvas.itemconfig(time_text, text=f"{count_min}:{count_sec}")
    if count>0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark+="✔"
        check.config(text=mark, font=(FONT_NAME,15,"bold"))

# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)




title_label=Label(text="TIMER", fg=GREEN, bg=YELLOW,font=(FONT_NAME,50,"bold") )
title_label.grid(column=1,row=0)

canvas = Canvas(width=206,height=228, bg=YELLOW, highlightthickness=0)
tomatoimg = PhotoImage(file="tomato.png")
canvas.create_image(103,114, image=tomatoimg)
time_text = canvas.create_text(103,130,text="00:00", fill="white", font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)


start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

check = Label(fg=GREEN, bg = YELLOW)
check.grid(column=1,row=3)

window.mainloop()
