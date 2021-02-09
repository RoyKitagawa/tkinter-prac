import tkinter
from tkinter import messagebox


class TkinterGui(object):

    CLICK_LEFT = '<Button-1>'
    CLICK_RIGHT = '<Button-3>'
    CLICK_WHEEL = '<Button-2>'

    def __init__(self):
        # Window
        self.window = tkinter.Tk()
        self.window.title('Sample Tinker')
        self.window.geometry('480x480')

        # Checkbox boolean
        self.bool_1 = tkinter.BooleanVar()
        self.bool_2 = tkinter.BooleanVar()
        self.bool_3 = tkinter.BooleanVar()

    def show_gui(self) -> None:
        # Label
        label = tkinter.Label(text='label pack')
        label.pack()
        label_2 = tkinter.Label(text='label_2 place')
        label_2.place(x=200,y=200)

        # Box
        entry_text = tkinter.StringVar()
        entry_text.set('Hello World')
        entry = tkinter.Entry(width=60, textvariable=entry_text)
        entry.pack()

        # Button
        button = tkinter.Button(text='Button A', width=60)
        button.bind(self.CLICK_LEFT, self.hello_window)
        button.pack()

        # Checkbox
        # Checkbox initialize
        self.bool_1.set(False)
        self.bool_2.set(False)
        self.bool_3.set(False)
        # Checkbox creation
        checkbutton_1 = tkinter.Checkbutton(text='No.1', variable=self.bool_1)
        checkbutton_1.pack()
        checkbutton_2 = tkinter.Checkbutton(text='No.2', variable=self.bool_2)
        checkbutton_2.pack()
        checkbutton_3 = tkinter.Checkbutton(text='No.3', variable=self.bool_3)
        checkbutton_3.pack()
        # Checkbox enter check
        button = tkinter.Button(text='Button', width=60)
        button.bind(self.CLICK_LEFT, self.check_boolean)
        button.pack()

        # Run window
        self.window.mainloop()

    def check_boolean(self, event) -> None:
        message = ''
        message += 'No.1はチェックされて'
        message += 'いる\n' if self.bool_1.get() else 'いない\n'
        message += 'No.2はチェックされて'
        message += 'いる\n' if self.bool_2.get() else 'いない\n'
        message += 'No.3はチェックされて'
        message += 'いる\n' if self.bool_3.get() else 'いない\n'

        messagebox.showinfo('Check Boolean Method', message)

    # def check_boolean(event):
    #     mesasge = ''
    #     if bool_1.get():

    @staticmethod
    def hello_window(event) -> None:
        messagebox.showinfo('Hello', 'Hello Tkinter')

