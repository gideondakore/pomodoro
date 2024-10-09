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
mark_count = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global reps
    global mark_count
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", fg=GREEN)
    check_marks.config(text="")
    reps = 0
    mark_count = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec in range(0, 10):
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        if reps % 2 != 0:
            global mark_count
            mark_count += 1
            marks = "✔"
            check_marks.config(text=marks*mark_count)
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text="Timer", font=(FONT_NAME, 40, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(row=0, column=1)

canvas = Canvas(width=210, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(103, 112, image=tomato_img)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)


start_btn = Button(width=7, text="Start", bg="white", font=(FONT_NAME, 15, "bold"), cursor="hand2", highlightthickness=0, borderwidth=0, command=start_timer)
start_btn.grid(row=2, column=0)

start_btn = Button(width=7, text="Reset", bg="white", font=(FONT_NAME, 15, "bold"), cursor="hand2", highlightthickness=0, borderwidth=0, command=reset_timer)
start_btn.grid(row=2, column=2)


check_marks = Label(fg=GREEN, font=(FONT_NAME, 20, "bold"), bg=YELLOW)
check_marks.grid(row=3, column=1)




window.mainloop()