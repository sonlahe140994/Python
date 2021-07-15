from tkinter import *
def up():
    print("Len")

def down():{
    print("Xuong")
}
def left():{
    print("Right")
}

win = Tk()

frame1 = Frame(win)
frame1.pack()

frame2 = Frame(win)
frame2.pack()

frame3 = Frame(win)
frame3.pack()

lenBtn = Button(frame1,text="Len")
lenBtn.pack()


win.mainloop()