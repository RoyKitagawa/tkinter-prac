import os
import tkinter as tk
import tkinter.filedialog
import logging
from typing import Callable, Tuple


class TkUtil:

    @staticmethod
    def create_tk_root(size: str = "500x360") -> tk:
        root = tk.Tk()
        # root.geometry(size)
        return root

    @staticmethod
    def run(tk_root: tk):
        if tk_root is None:
            logging.error('tk instance is null')
            return
        tk_root.mainloop()

    @staticmethod
    def create_label(
            message: tk.StringVar,
            font: Tuple[str, int] = ('', 12)
    ) -> tk.Label:
        return tk.Label(textvariable=message, font=font)

    @staticmethod
    def place_label(label: tk.Label, x: int = 0, y: int = 0):
        label.place(x=x, y=y)

    @staticmethod
    def create_button(
            tk_root: tk,
            message: str = "Button",
            on_click: Callable[[], None] = None
    ) -> tk.Button:
        return tk.Button(tk_root, text=message, command=on_click)

    @staticmethod
    def place_button(button: tk.Button, x: int = 0, y: int = 0):
        button.place(x=x, y=y)

    @staticmethod
    def open_file_browse_window() -> str:
        fTyp = [("", "*")]
        iDir = os.path.abspath(os.path.dirname(__file__))
        file_name = tk.filedialog.askopenfilenames(filetypes=fTyp, initialdir=iDir)
        # print(file_name)
        return file_name
        # if len(file_name) == 0:
        #     self.file_name.set('選択をキャンセルしました')
        # else:
        #     self.file_name.set(file_name)

    @staticmethod
    def get_string_var(def_value: str = '') -> tk.StringVar:
        result = tk.StringVar()
        result.set(def_value)
        return result

    # @staticmethod
    # def pack(
    #         tk_root: tk,
    #         pack_rule: tkinter.constants = None,
    #         *tk_ui):
    #     if tk_ui is not None and len(tk) > 0:
    #         for ui in tk_ui:
    #             tk_root
