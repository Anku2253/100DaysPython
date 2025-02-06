from tkinter import *

def milesToKm():
    miles = float(milesInp.get())
    km = round(miles*1.609)
    kmResultLabel.config(text=f"{km}")

# window
window = Tk()
window.title("Mile To Kilometre Converter")
window.config(padx=20,pady=20)

#Widget
milesInp = Entry(width=7)
milesInp.grid(column=1,row=0)

#Labels
milesLabel = Label(text="Miles")
milesLabel.grid(column=2,row=0)

isEqual = Label(text="is equals to")
isEqual.grid(column=0,row=1)

kmResultLabel = Label(text="0")
kmResultLabel.grid(column=1,row=1)

kmLabel = Label(text="KM")
kmLabel.grid(column=2,row=1)

#Button
calculate = Button(text="Calculate",command=milesToKm)
calculate.grid(column=1,row=2)


window.mainloop()