from tkinter import *
import math
import os
import sys
from tkinter import messagebox

root = Tk()
root.title("DeltaV Calculator")

# Gets file location, sets .ico as the programs icon
dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))
root.iconbitmap(dirname + "/rocket.ico")

# Sets gravity variable
g = 9.806


# Pop up error box if there is invalid inputs
def error1():
    response = messagebox.showerror("Error", "Invalid inputs")
    Label(root, text=response).pack()


# Runs when the 'Calculate' button is pressed
# Gets inputs and completes calculation
def answer():
    try:
        rocketmass = float(entry1.get())
    except ValueError:
        error1()
        print("Invalid Rocket mass")
    try:
        fuel = float(entry2.get())
    except ValueError:
        error1()
        print("Invalid Fuel mass")
    try:
        isp = float(entry3.get())
    except ValueError:
        error1()
        print("Invalid ISP")
    totalmass = fuel + rocketmass
    deltav = isp * g * math.log(totalmass / rocketmass)
    answerLabel = Label(root, text=round(deltav, 3))
    answerLabel.grid(row=5, column=2)


# Labels and entry fields
instruction = Label(root, text="Enter values:")
inputlabel1 = Label(root, text="Rocket mass (Kg)")
inputlabel2 = Label(root, text="Fuel used (Kg) ")
inputlabel3 = Label(root, text="ISP (Seconds) ")
gapLabel = Label(root, text="   ")
entry1 = Entry(root, width=20, borderwidth=5)
entry2 = Entry(root, width=20, borderwidth=5)
entry3 = Entry(root, width=20, borderwidth=5)
calculate = Button(root, padx=20, text="Calculate", command=answer)
label4 = Label(root, text="Δv (m/s):")

# Positions the labels and inputs
instruction.grid(row=0, column=0)
inputlabel1.grid(row=1, column=0)
inputlabel2.grid(row=2, column=0)
inputlabel3.grid(row=3, column=0)
gapLabel.grid(row=1, column=1)
entry1.grid(row=1, column=2)
entry2.grid(row=2, column=2)
entry3.grid(row=3, column=2)
calculate.grid(row=4, column=0, columnspan=2)
label4.grid(row=5, column=0)


root.mainloop()