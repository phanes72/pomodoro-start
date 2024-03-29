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
NUMBER_OF_SECONDS = 60
checkmarks = " "
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global checkmarks
    global reps

    window.after_cancel(timer)

    checkmarks = " "
    checkmark_label.config(text=checkmarks)

    timer_label.config(text="Timer", fg=GREEN)

    canvas.itemconfig(timer_text, text=f"0:00")

    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps

    work_sec = WORK_MIN * NUMBER_OF_SECONDS
    short_break_sec = SHORT_BREAK_MIN * NUMBER_OF_SECONDS
    long_break_sec = LONG_BREAK_MIN * NUMBER_OF_SECONDS
    time = 0

    if reps >= 7:
        time = long_break_sec
        timer_label.config(text="Long Break")
        timer_label.config(fg=RED)
        print(f"Long Break={time}")
    elif reps % 2 != 0:
        time = short_break_sec
        timer_label.config(text="Short Break")
        timer_label.config(fg=PINK)
        print(f"Short Break={time}")
    elif reps % 2 == 0:
        time = work_sec
        timer_label.config(text="Work")
        timer_label.config(fg=GREEN)
        print(f"Work={time}")
    reps = reps + 1
    count_down(time)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


def count_down(count):
    global reps
    global checkmarks
    global timer

    checkmark = "✔"

    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_min < 0:
        count_min = 0
        count_sec = 00

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if count >= 0:
        timer = window.after(1000, count_down, count - 1)

    elif reps < 8:
        start_timer()

        if reps % 2 == 0:
            checkmark_label.config(text=checkmark)
            checkmarks = checkmarks + checkmark
            checkmark_label.config(text=checkmarks)

        if reps >= 7:
            return


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=2)

timer_label = Label(text="Timer", font=(FONT_NAME, 50), fg=GREEN, bg=YELLOW)
timer_label.grid(column=2, row=0)

checkmark_label = Label(fg=GREEN, bg=YELLOW)
checkmark_label.grid(column=2, row=4)

start_button = Button(text="Start", bg=YELLOW, highlightbackground=YELLOW, command=start_timer)
start_button.grid(column=1, row=3)

reset_button = Button(text="Reset", bg=YELLOW, highlightbackground=YELLOW, command=reset_timer)
reset_button.grid(column=3, row=3)

window.mainloop()
