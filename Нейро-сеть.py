from tkinter import *
from tkinter.ttk import *
import math
import numpy as np

root = Tk()
canvas = Canvas(root, bg='white', height=500, width=300)
canvas.pack()

e = []
for i in range(1500):
    e.append(0)

wesfile = open('weights', 'r', encoding='utf-8')
weigstr=str(wesfile.read()).split('\n')
wes = [[],[],[],[],[],[],[],[],[],[]]
for i in range(10):
    for j in range(1500):
        wes[i].append(float(weigstr[1500*i+j]))
w=wes[5]
count=0

def prweights(g):
    global wes
    wesfile = open('weights', 'w', encoding='utf-8')
    wes1=str(wes).replace('[', '').replace(']', '').replace(', ', '\n')
    wesfile.write(wes1)
    wesfile = open('weights', 'r', encoding='utf-8')

def mousedown(event):
    x=event.x//10
    y=event.y//10
    e[30*y+x+1]=1
    canvas.create_rectangle(x*10, y*10, x*10+10, y*10+10, outline="#000", fill="#000")

def efunc(g):
    global e
    print(e)

def clean(g):
    global e
    canvas.delete('all')
    e = []
    for i in range(1500):
        e.append(0)

def sigmoid(weights, neurons):
    answer=[]
    for z in range(10):
        x = 0.0
        for i in range(1500):
            x += neurons[i]*weights[z][i]
        answer.append(x / neurons.count(1))
    print(answer)
    return answer

def sigmoid1(g):
    global wes, e
    answer = []
    for z in range(10):
        x = 0.0
        for i in range(1500):
            x += e[i] * wes[z][i]
        answer.append(x / e.count(1))
    print('\n'+str(answer))
    print(answer.index(max(answer)))

def learn(h):
    global number, count
    count+=1
    for z in range(1):
        for i in range(0, 1500):
            if e[i] == 0:
                wes[number][i] -= 0.1
            else:
                for es in range(10):
                    if es != number:
                        wes[es][i] -= 0.1

def en1(h):
    global number
    number = 1
def en2(h):
    global number
    number = 2
def en3(h):
    global number
    number = 3
def en4(h):
    global number
    number = 4
def en5(h):
    global number
    number = 5
def en6(h):
    global number
    number = 6
def en7(h):
    global number
    number = 7
def en8(h):
    global number
    number = 8
def en9(h):
    global number
    number = 9
def en0(h):
    global number
    number = 0

canvas.bind_all("<s>", sigmoid1)
canvas.bind_all("<B1-Motion>", mousedown)
canvas.bind_all("<Return>", learn)
canvas.bind_all("<c>", clean)
canvas.bind_all("<z>", prweights)

canvas.bind_all("<q>", en1)
canvas.bind_all("<w>", en2)
canvas.bind_all("<e>", en3)
canvas.bind_all("<r>", en4)
canvas.bind_all("<t>", en5)
canvas.bind_all("<y>", en6)
canvas.bind_all("<u>", en7)
canvas.bind_all("<i>", en8)
canvas.bind_all("<o>", en9)
canvas.bind_all("<p>", en0)

mainloop()
