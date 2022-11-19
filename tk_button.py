def say_hello():
    global a
    a += 1
    print('hello')
    l = [btn2, btn3, btn4,btn5]
    if a % 2 == 0:
        for i in l:
            i['state'] = tk.DISABLED
    else:
        for i in l:
            i['state'] = tk.NORMAL


a = 0


def add_label():
    label = tk.Label(win, text='new')
    label.pack()


def counter():
    global count
    count += 1
    btn4["text"] = f"Счетчик: {count}"


count = 0

import random


def color():
    r = ('red', 'blue', 'green', 'orange')

    win.config(bg=[random.choice(r)])


import tkinter as tk

win = tk.Tk()
win.geometry("400x500+100+200")
win.title('Мое первое графическое изображение')

btn1 = tk.Button(win, text='Hello',
                     command=say_hello)

btn2 = tk.Button(win, text='Add new label',
                     command=add_label)

btn3 = tk.Button(win, text='Add new label lambda',
                     command=lambda: tk.Label(win, text='new lambda').pack())

btn4 = tk.Button(win, text=f"Счетчик: {count}",
                     command=counter,
                     activebackground='blue',
                     bg='red')

btn5 = tk.Button(win, text='b',
                     command=color)

btn1.pack()
btn2.pack()
btn3.pack()
btn4.pack()
btn5.pack()

win.mainloop()
