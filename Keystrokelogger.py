from tkinter import *
def smth(event):
    print("You pressed: " + event.keysym)
    label.config(text=event.keysym)
window = Tk()
window.bind("<Key>",smth)
label = Label(window,font=("",50))
label.pack()
window.mainloop()