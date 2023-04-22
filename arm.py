from tkinter import *
from tkinter.ttk import *
import math
import pyfirmata
import time
root = Tk()
canvas = Canvas(root, bg='grey7', height=800, width=1600)
canvas.pack()

board=pyfirmata.Arduino('COM5')
s1=90
s2=45
s3=50

ac=1
mod=1
def get_rgb(rgb):
    return "#%02x%02x%02x" % rgb
def go():
    global s1, s2, s3
    board.servo_config(4, 0, 180, s1)
    time.sleep(s1/180)
    a2=0
    a3=0
    while (a2<s2) or (a3<s3):
        if a2<s2:
            a2+=1
            board.servo_config(5, 0, 180, a2)
        if a3<s3:
            a3+=1
            board.servo_config(5, 0, 180, a3)

circle=Label(text="❌", font=("Times", 10), foreground='white', background='black')
Button(text="Go", command=go).place(x=1500, y=50)

def mousedown(event):
    global ac, mod, s1, s2, s3
    x = (event.x - 800) // 2
    y = (800 - event.y) // 2
    if x == 0: x = 1
    ac = int((x ** 2 + y ** 2) ** 0.5 // 1)
    if ac<=400:
        modx = abs(x)
        if modx == 0: modx = 1
        mod = int(x / modx)
        circle.place(x=event.x - 9, y=event.y - 7)
        s1 = round(math.acos(abs(x) / ac) * 57.3)
        if mod > 0: s1 = 180 - s1
        s2 = round(math.acos(ac / 400) * 57.3)
        s3 = round(math.acos(1 - (ac ** 2 / 80000)) * 57.3)
        print(ac, s1, s2, s3)



canvas.create_oval(0, 0, 1600, 1600, outline="grey", fill='black', width=2)
canvas.create_line(800, 0, 800, 800, dash=(4, 2), fill='green')
canvas.create_line(0, 800, 1600, 800, dash=(4, 2), fill='green')
canvas.bind_all("<Button-1>", mousedown)
canvas.create_text(810, 790, text="0", fill="green", font=('Arial 8 bold'))
canvas.create_text(810, 590, text="10", fill="green", font=('Arial 8 bold'))
canvas.create_text(810, 390, text="20", fill="green", font=('Arial 8 bold'))
canvas.create_text(810, 190, text="30", fill="green", font=('Arial 8 bold'))
canvas.create_text(810, 10, text="40", fill="green", font=('Arial 8 bold'))

canvas.create_text(600, 790, text="10", fill="green", font=('Arial 8 bold'))
canvas.create_text(400, 790, text="20", fill="green", font=('Arial 8 bold'))
canvas.create_text(200, 790, text="30", fill="green", font=('Arial 8 bold'))
canvas.create_text(10, 790, text="40", fill="green", font=('Arial 8 bold'))

canvas.create_text(1000, 790, text="10", fill="green", font=('Arial 8 bold'))
canvas.create_text(1200, 790, text="20", fill="green", font=('Arial 8 bold'))
canvas.create_text(1400, 790, text="30", fill="green", font=('Arial 8 bold'))
canvas.create_text(1590, 790, text="40", fill="green", font=('Arial 8 bold'))
mainloop()
