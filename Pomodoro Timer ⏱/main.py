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
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    tittle_label.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
       count_down(long_break_sec)
       tittle_label.config(text="Break", bg=RED)
    elif reps % 2 == 0:
       count_down(short_break_sec)
       tittle_label.config(text="Break", bg=PINK)
    else:
        count_down(work_sec)
        tittle_label.config(text="Work", bg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):

    count_minutes = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_minutes}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔"
        check_marks.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=200, pady=100, bg="#A31D1D")

tittle_label = Label(text="Timer", fg=GREEN, bg="#A31D1D", font=(FONT_NAME, 50))
tittle_label.grid(column=1, row=0)

canvas = Canvas(width=600, height=600, bg="#A31D1D", highlightthickness=0)
strawberry_img = PhotoImage(file="Strawberry.png")
canvas.create_image(300,300, image=strawberry_img)
font_size = int(canvas.winfo_width() * 1)
timer_text = canvas.create_text(300, 300, text="00:00", fill="black", font=(FONT_NAME, 40, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", width=20, height=2, bg=GREEN, highlightthickness=0, font=FONT_NAME, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", width=20, height=2, bg=GREEN, highlightthickness=0, font=FONT_NAME, command=reset_timer)
reset_button.grid(column=2, row=2)

check_marks = Label(fg=GREEN, bg="#A31D1D")
check_marks.grid(column=1, row=3)


window.mainloop()
