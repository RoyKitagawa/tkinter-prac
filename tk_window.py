import tkinter as tk
# from PIL import ImageTk

import tkinter as tk
# from template import
# https://www.pytry3g.com/entry/grid-widget


class Template(tk.Tk):
    def __init__(self, **kwargs):
        super(Template, self).__init__()
        self.title(kwargs.get("title", "tkinter"))
        self.geometry("+{}+{}".format(*kwargs.get("pos", (0, 0))))
        self.resizable(*kwargs.get("resize", (1, 1)))
        # try:
        #     self.iconbitmap(kwargs.get("icon", None))
        # except:
        #     return
            # if kwargs.get("icon", None) is not None:
            #     icon_name = kwargs.get("icon")
            #     icon_img = ImageTk.PhotoImage(file=icon_name)
            #     self.tk.call("wm", "iconphoto", self._w, icon_img)

    def run(self):
        self.mainloop()


class App(Template):
    def __init__(self):
        super(App, self).__init__()
        self.create_widgets()
        self.attach_widgets()

    def create_widgets(self):
        self.frame_1 = tk.Frame(self, width=100, height=100, bg="coral")
        self.frame_2 = tk.Frame(self, width=100, height=100, bg="tan")
        self.frame_3 = tk.Frame(self, width=100, height=100, bg="violet")


    def attach_widgets(self):
        self.frame_1.grid(column=0, row=0)
        self.frame_2.grid(column=2, row=0)
        self.frame_3.grid()

if __name__ == "__main__":
    app = App()
    app.run()
