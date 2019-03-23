from tkinter import *

def sel():
   selection = "Value = " + str(varX.get())
   label.config(text = selection)

def test(value):
    scaleY.set(value)

root = Tk()
varX = DoubleVar()
varY = DoubleVar()

scaleX = Scale(root, variable = varX, command=test)
scaleX.pack(anchor=CENTER)

scaleY = Scale(root, variable = varY)
scaleY.pack()

button = Button(root, text="Get Scale Value")
button.pack(anchor=CENTER)

label = Label(root)
label.pack()

txt = Entry(root)
txt.pack()

root.mainloop()
