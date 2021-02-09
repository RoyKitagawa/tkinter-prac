# from tkinter import ttk
# from tkinter import StringVar
import tkinter as tk


# tkinerを継承したクラス
class Application(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        # self.master.geometry

        self.pack()
        self.create_widgets()


def create_widgets(self):
    self.hi_there = tk.Button(self)
    self.hi_there['text'] = 'Hello World/n(click me)'
    self.hi_there['command'] = self.say_hi
    self.hi_there.pack(side='top')

    self.quit = tk.Button(self, text="Quit")


def say_hi(self):
    print('hi there, everyone!!')


# このクラス実行時に必ず呼び去られる処理
root = tk.Tk()
application = Application(master=root)
application.mainloop()
