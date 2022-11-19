import tkinter as tk

win = tk.Tk()
win.title("Мое первое графическое приложение")
photo = tk.PhotoImage(file='i_id=53f711792ee3a1106677b21b15c07fc4-5884061-imag.png')
win.iconphoto(False, photo)
win.config(bg='#8B9600')
win.geometry("500x600+300+200")
win.minsize(300, 400)
win.maxsize(700, 800)
win.resizable(True, True)
label_1 = tk.Label(win, text='''Hello!
 world!''',
                   bg='red', fg='white',
                   font=('Arial', 15, 'bold'),
                   padx=20,
                   pady=50,
                   width=30,
                   height=10,
                   anchor='sw',
                   relief=tk.RAISED,
                   bd=10,
                   justify=tk.RIGHT)
label_1.pack()
win.mainloop()
