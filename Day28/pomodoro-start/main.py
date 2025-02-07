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
def resetTimer():
    window.after_cancel(timer)
    canvas.itemconfig(timerText,text="00:00")
    timerLabel.config(text="Timer")
    checkLabel.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def startTimer():
    global reps
    reps+=1

    workSec = WORK_MIN*60
    shortBreakSec = SHORT_BREAK_MIN*60
    longBreakSec = LONG_BREAK_MIN*60

    countDown(workSec)
    if reps%8==0:
        countDown(longBreakSec)
        timerLabel.config(text="Break",fg=RED)
    elif reps%2==0:
        countDown(shortBreakSec)
        timerLabel.config(text="Break",fg=PINK)
    else:
        countDown(workSec)
        timerLabel.config(text="Break",fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countDown(count):
    countMin = math.floor(count/60)
    countSec = count%60
    if countSec<10:
        countSec = f"0{countSec}"
    canvas.itemconfig(timerText, text=f"{countMin}:{countSec}")
    if count>0:
        global timer
        timer = window.after(1000,countDown,count-1)
    else:
        startTimer()
        marks = ""
        workSession = math.floor(reps/2)
        for _ in range(workSession):
            marks += "✔"
        checkLabel.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
    #Window
window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)

#Canvas
canvas = Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomatoImg = PhotoImage(file=r"Day28\pomodoro-start\tomato.png")
canvas.create_image(101.5,112,image=tomatoImg)
timerText = (canvas.create_text(101.5,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold")))
canvas.grid(row=1,column=1)

#Label
timerLabel = Label(text="Timer",fg=GREEN,bg=YELLOW,font=(FONT_NAME,50,"bold"),highlightthickness=0)
timerLabel.grid(row=0,column=1)

checkLabel = Label(text="",bg=YELLOW,fg=GREEN)
checkLabel.grid(row=3,column=1)

#Button
start = Button(text="Start",highlightthickness=0,command=startTimer)
start.grid(row=2,column=0)

reset = Button(text="Reset",highlightthickness=0,command=resetTimer)
reset.grid(row=2,column=2)

window.mainloop()