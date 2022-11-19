import tkinter as tk

def select_level():
    level = level_var.get()
    level_text.set(f"Вы выбрали {level} уровень")
    if level == 1:
        print('Easy')
    elif level == 2:
        print('Middle')
    elif level == 3:
        print('Hard')

win = tk.Tk()
win.geometry(f"300x400+100+200")
win.title('Мое первое графическое приложение')
photo = tk.PhotoImage(file='pngtree-2022-gold-3d-rendering-png-image_6706631.png')
win.iconphoto(False,photo)

level_var = tk.IntVar()
level_text = tk.StringVar()

tk.Label(win, text='Выберите уровень сложности').pack()
tk.Radiobutton(win, text='Easy', variable=level_var, value=1, command=select_level).pack()
tk.Radiobutton(win, text='Middle', variable=level_var, value=2, command=select_level).pack()
tk.Radiobutton(win, text='Hard',variable=level_var, value=3, command=select_level).pack()
tk.Label(win, textvariable=level_text).pack()
win.mainloop()