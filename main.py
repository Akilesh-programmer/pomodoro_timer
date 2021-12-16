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
# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    global reps
    reps = 0
    tick_labels.config(text="")
    start_timer()
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 1)
        timer_label.config(text="Break", fg=PINK)
        reset()

    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 1)
        timer_label.config(text="Break", fg=RED)
        round = reps / 2
        if round == 1:
            tick_labels.config(text="✔")
        elif round == 2:
            tick_labels.config(text="✔✔")
        elif round == 3:
            tick_labels.config(text="✔✔✔")
        elif round == 4:
            tick_labels.config(text="✔✔✔✔")
            
    else:
        count_down(WORK_MIN * 1)
        timer_label.config(text="Work", fg=YELLOW)
    


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec == 0:
        count_sec = "00"
    elif count_sec == 9:
        count_sec = "09"
    elif count_sec == 8:
        count_sec = "08"
    elif count_sec == 7:
        count_sec = "07"
    elif count_sec == 6:
        count_sec = "06"
    elif count_sec == 5:
        count_sec = "05"
    elif count_sec == 4:
        count_sec = "04"
    elif count_sec == 3:
        count_sec = "03"
    elif count_sec == 2:
        count_sec = "02"
    elif count_sec == 1:
        count_sec = "01"
        
    
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if count > 0:
        # Here we are delaying the process by 1 second. Here it is mentioned as 1000, because it is milliseconds value. Then we are again calling the function to repeat counting down. Finally whatever we give as 3rd or subsequent input, it will be a input for the count_down function.
        window.after(1000, count_down, count - 1)

# ---------------------------- UI SETUP ------------------------------- #

# Window
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=200, pady=100, bg=GREEN)

# Putting image on to the screen with canvas widget.
canvas = Canvas(width=203, height=227, bg=GREEN, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(103, 116, image=tomato_img)
timer_text = canvas.create_text(103, 135, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(row=1, column=1)



# Timer label
timer_label = Label(text="Timer", font=(FONT_NAME, 50, "normal"), bg=GREEN, fg=YELLOW)
timer_label.grid(row=0, column=1)


# Start button
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

# Reset button
reset_button = Button(text="Reset", highlightthickness=0, command=reset)
reset_button.grid(row=2, column=2)

# Tick mark label
tick_labels = Label(font=(FONT_NAME, 15, "normal"), bg=GREEN, fg=YELLOW)
tick_labels.grid(row=3, column=1)


window.mainloop()