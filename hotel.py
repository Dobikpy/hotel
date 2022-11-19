import os
import tkinter as tk
from tkinter import ttk
import sqlite3


class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()
        self.db = db
        self.view_records()
        self.os = os

    def start(self):
        self.os.system('C:/Users/DnS/Desktop/project_1/dist/tk_calculator_1.exe')
        return

    def init_main(self):
        toolbar = tk.Frame(bg='#d7d8e0', bd=5)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        self.add_img = tk.PhotoImage(file='Добавить.png')
        btn_open_dialog = tk.Button(toolbar, text='Введите данные', command=self.open_dialog, bg='#d7d8e0', bd=4,
                                    compound=tk.TOP, image=self.add_img)
        btn_open_dialog.pack(side=tk.LEFT)

        self.update_img = tk.PhotoImage(file='Редактировать.png')
        btn_edit_dialog = tk.Button(toolbar, text='Редактировать', bg='#d7d8e0', bd=4, image=self.update_img,
                                    compound=tk.TOP, command=self.open_update_dialog)
        btn_edit_dialog.pack(side=tk.LEFT)

        self.delete_img = tk.PhotoImage(file='Удалить.png')
        btn_delete = tk.Button(toolbar, text='Удалить', bg='#d7d8e0', bd=4, image=self.delete_img,
                               compound=tk.TOP, command=self.delete_records)
        btn_delete.pack(side=tk.LEFT)

        self.search_img = tk.PhotoImage(file='поиск.png')
        btn_search = tk.Button(toolbar, text='Поиск', bg='#d7d8e0', bd=4, image=self.search_img,
                               compound=tk.TOP, command=self.open_search_dialog)
        btn_search.pack(side=tk.LEFT)

        self.refresh_img = tk.PhotoImage(file='Обновить.png')
        btn_refresh = tk.Button(toolbar, text='Обновить', bg='#d7d8e0', bd=4, image=self.refresh_img,
                                compound=tk.TOP, command=self.view_records)
        btn_refresh.pack(side=tk.LEFT)

        self.calc_img = tk.PhotoImage(file='Калькулятор.png')
        btn_calc = tk.Button(toolbar, text='Калькулятор', bg='#d7d8e0', bd=4, image=self.calc_img,
                             compound=tk.TOP, command=self.start)
        btn_calc.pack(side=tk.LEFT)

        self.tree = ttk.Treeview(self, columns=('ID', 'Data', 'FIO', 'Telephone', 'Summa', 'Grade'),
                                 height=15, show='headings')

        self.tree.column('ID', width=60, anchor=tk.CENTER)
        self.tree.column('Data', width=200, anchor=tk.CENTER)
        self.tree.column('FIO', width=290, anchor=tk.CENTER)
        self.tree.column('Telephone', width=150, anchor=tk.CENTER)
        self.tree.column('Summa', width=100, anchor=tk.CENTER)
        self.tree.column('Grade', width=100, anchor=tk.CENTER)

        self.tree.heading('ID', text='Номер')
        self.tree.heading('Data', text='Дата прибытия/убытия')
        self.tree.heading('FIO', text='ФИО')
        self.tree.heading('Telephone', text='Номер телефона')
        self.tree.heading('Summa', text='Сумма')
        self.tree.heading('Grade', text='Оценка')

        self.tree.pack(side=tk.LEFT)

        self.style = ttk.Style(self)
        self.style.configure('Treeview.Heading', font=('Arial', 13))

        scroll = tk.Scrollbar(self, command=self.tree.yview)
        scroll.pack(side=tk.LEFT, fill=tk.Y)
        self.tree.configure(yscrollcommand=scroll.set)

    # Фунция для вызова двух других (вывода значений из дочернего окна и отображения их в таблице Treeview
    def records(self, data, fio, telephone, summa, grade):
        self.db.insert_data(data, fio, telephone, summa, grade)
        self.view_records()

    # Функция для редактирования записей в БД и вывода в Treeview
    def update_record(self, data, fio, telephone, summa, grade):
        self.db.c.execute('''UPDATE hotel SET data=?, fio=?, telephone=?, summa=?, grade=? WHERE ID=?''',
                          (data, fio, telephone, summa, grade, self.tree.set(self.tree.selection()[0], '#1', )))
        self.db.conn.commit()
        self.view_records()

    # Функция для отображения данных из БД в виджете Treeview главного окна программы
    def view_records(self):
        self.db.c.execute('''SELECT * FROM hotel''')
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]

    # Функция удаления по очереди выделенных записей из БД
    def delete_records(self):
        for selection_item in self.tree.selection():
            self.db.c.execute('''DELETE FROM hotel WHERE id=?''', (self.tree.set(selection_item, '#1', ),))
            self.db.conn.commit()
            self.view_records()

    def search_records(self, telephone):
        telephone = ('%' + telephone + '%',)
        self.db.c.execute('''SELECT * FROM hotel WHERE telephone LIKE ?''', telephone)
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]

    # Функция открытия дочернего окна при нажатии кнопки btn_open_dialog
    def open_dialog(self):
        Child()

    # Функция открытия окна редактирования при нажатии кнопки btn_edit_dialog
    def open_update_dialog(self):
        Update()

    # Функция открытия окна поиска при нажатии кнопки btn_search
    def open_search_dialog(self):
        Search()


# Класс для создания дочернего окна
class Child(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_child()
        self.view = app

    def init_child(self):
        self.title('Журнал')
        self.geometry('400x300+400+300')
        self.resizable(False, False)

        label_data = tk.Label(self, text='Дата прибытия/убытия:')
        label_data.place(x=50, y=50)
        label_data = tk.Label(self, text='ФИО:')
        label_data.place(x=50, y=80)
        label_data = tk.Label(self, text='Номер телефона:')
        label_data.place(x=50, y=110)
        label_summa = tk.Label(self, text='Сумма:')
        label_summa.place(x=50, y=140)
        label_summa = tk.Label(self, text='Оценка:')
        label_summa.place(x=50, y=170)

        # self.combobox = ttk.Combobox(self, values=[u'Прибытие', u'Убытие'])
        # self.combobox.current(0)
        # self.combobox.place(x=200, y=50)

        self.entry_fio = ttk.Entry(self)
        self.entry_fio.place(x=200, y=80)

        self.entry_telephon = ttk.Entry(self)
        self.entry_telephon.place(x=200, y=110)

        self.entry_data = ttk.Entry(self)
        self.entry_data.place(x=200, y=50)

        self.entry_summa = ttk.Entry(self)
        self.entry_summa.place(x=200, y=140)

        self.entry_grade = ttk.Entry(self)
        self.entry_grade.place(x=200, y=170)

        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=300, y=200)

        self.btn_ok = ttk.Button(self, text='Добавить')
        self.btn_ok.place(x=220, y=200)
        self.btn_ok.bind('<Button-1>', lambda event: self.view.records(self.entry_data.get(),
                                                                       self.entry_fio.get(),
                                                                       self.entry_telephon.get(),
                                                                       self.entry_summa.get(),
                                                                       self.entry_grade.get()))

        self.grab_set()
        self.focus_set()


# Класс для отображения окна для редактирования(подкласс класса Child)
class Update(Child):
    def __init__(self):
        super().__init__()
        self.init_edit()
        self.view = app
        self.db = db
        self.default_data()

    def init_edit(self):
        self.title('Редактировать')
        btn_edit = ttk.Button(self, text='Редактировать')
        btn_edit.place(x=205, y=200)
        btn_edit.bind('<Button>', lambda event: self.view.update_record(self.entry_data.get(),
                                                                        self.entry_fio.get(),
                                                                        self.entry_telephon.get(),
                                                                        self.entry_summa.get(),
                                                                        self.entry_grade.get()))
        self.btn_ok.destroy()

    def default_data(self):
        self.db.c.execute('''SELECT * FROM hotel WHERE id=?''',
                          self.view.tree.set(self.view.tree.selection()[0], '#1'))
        row = self.db.c.fetchone()
        self.entry_data.insert(0, row[1])
        self.entry_fio.insert(0, row[2])
        self.entry_telephon.insert(0, row[3])
        self.entry_summa.insert(0, row[4])
        self.entry_grade.insert(0, row[5])


class Search(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.init_search()
        self.view = app

    def init_search(self):
        self.title('Поиск')
        self.geometry('300x100+400+300')
        self.resizable(False, False)

        label_search = tk.Label(self, text='Поиск')
        label_search.place(x=50, y=20)

        self.entry_search = ttk.Entry(self)
        self.entry_search.place(x=105, y=20, width=150)

        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=185, y=50)

        btn_search = ttk.Button(self, text='Поиск')
        btn_search.place(x=105, y=50)
        btn_search.bind('<Button-1>', lambda event: self.view.search_records(self.entry_search.get()))
        btn_search.bind('<Button-1>', lambda event: self.destroy(), add='+')


class DB:
    def __init__(self):
        self.conn = sqlite3.connect('hotel.db')
        self.c = self.conn.cursor()
        self.c.execute(
            '''CREATE TABLE IF NOT EXISTS hotel(id integer primary key, data real, fio text, telephone integer,
             summa real, grade text)''')
        self.conn.commit()

    # Функция добавления данных в БД с помощью sql запроса из дочернего окна
    def insert_data(self, data, fio, telephone, summa, grade):
        self.c.execute('''INSERT INTO hotel(data, fio, telephone, summa, grade) VALUES (?, ?, ?, ?, ?)''',
                       (data, fio, telephone, summa, grade))
        self.conn.commit()


if __name__ == "__main__":
    root = tk.Tk()
    db = DB()
    app = Main(root)
    app.pack()
    root.title('ГОСТИНИЦА')
    root.geometry("925x450+300+200")
    root.resizable(False, False)
    root.mainloop()
