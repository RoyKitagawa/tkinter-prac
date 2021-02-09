import tkinter as tk
import tkinter.messagebox as tmb

root = tk.Tk()

# Labelframe and Label 1, 2
tk.Label(root, text="1, 2: Labelframe \nand Label").grid(row=0, sticky="e")
labelframe = tk.LabelFrame(root, text="LabelFrame")
labelframe.grid(row=0, column=1, padx=10, pady=10)
tk.Label(labelframe, text="Label").pack()

# Button 3
tk.Label(root, text="3: Button").grid(row=1, sticky="e")
tk.Button(root, text="Button", command=lambda : tmb.showinfo("メッセージ", "clicked")).\
    grid(row=1, column=1, padx=10, pady=10)

# Entry 4
tk.Label(root, text="4: Entry").grid(row=2, sticky="e")
tk.Entry(root).grid(row=2, column=1, padx=10, pady=10)

# Checkbutton 5
tk.Label(root, text="5: CheckButton").grid(row=3, sticky="e")
tk.Checkbutton(root, text="A").grid(row=3, column=1, padx=10, pady=10)

# radioButton 6
tk.Label(root, text="6: RadioButton").grid(row=4, sticky="e")
frame_for_radio = tk.Frame(root)
frame_for_radio.grid(row=4, column=1, padx=10, pady=10)
iv1 = tk.IntVar()
iv1.set(1)
tk.Radiobutton(frame_for_radio, text="a", value=1, variable=iv1).pack()
tk.Radiobutton(frame_for_radio, text="b", value=2, variable=iv1).pack()
tk.Radiobutton(frame_for_radio, text="c", value=3, variable=iv1).pack()

# OptionMenu 7
tk.Label(root, text="7: OptionMenu").grid(row=5, sticky="e")
sv1 = tk.StringVar()
sv1.set('オプション１')
tk.OptionMenu(root, sv1, 'オプション１', 'オプション２').grid(row=5, column=1, padx=10, pady=10)

# Listbox 8
tk.Label(root, text="8: Listbox").grid(row=6, sticky="e")
listbox = tk.Listbox(root, height=4)
for line in ["選択肢1", "選択肢2","選択肢3","選択肢4", "選択肢5"]:
    listbox.insert(tk.END, line)
listbox.select_set(1)
listbox.grid(row=6, column=1, padx=10, pady=10)

# Spinbox 9
tk.Label(root, text="9: Spinbox").grid(row=0, column=2, sticky="e")
tk.Spinbox(root, values=(2, 4, 10)).grid(row=0, column=3, padx=10, pady=10)

# Scale 10
tk.Label(root, text="10: Scale").grid(row=1, column=2, sticky="e")
tk.Scale(root, from_=10, to=80, label='Scale', orient=tk.HORIZONTAL).grid(row=1, column=3, padx=10, pady=10)

# Message 11
tk.Label(root, text="11: Message").grid(row=2, column=2, sticky="e")
tk.Message(root, text="私の名前は中村です").grid(row=2, column=3, padx=10, pady=10)

# Text 12
tk.Label(root, text="12: Text").grid(row=3, column=2, sticky="e")
text = tk.Text(root, width=20, height=6)
text.insert(tk.END, "sample text\n1\n2\n3")
text.grid(row=3, column=3, padx=10, pady=10)

# ScrollBar with Listbox 13
tk.Label(root, text="13: Listbox \n& ScrollBar").grid(row=4, column=2, sticky="e")
scrollbar_frame = tk.Frame(root)
scrollbar_frame.grid(row=4, column=3, padx=10, pady=10)
listbox2 = tk.Listbox(scrollbar_frame)
for i in range(1000):
    listbox2.insert(tk.END, i)
listbox2.pack(side=tk.LEFT)
scroll_bar =tk.Scrollbar(scrollbar_frame, command=listbox2.yview)
scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)
listbox2.config(yscrollcommand=scroll_bar.set)

# Canvas 14
tk.Label(root, text="14: Canvas").grid(row=5, column=2, sticky="e")
canvas = tk.Canvas(root, bg='white', width=200, height=100)
canvas.grid(row=5, column=3, padx=10, pady=10)
canvas.create_oval(25, 15, 180, 60, fill='red')
canvas.create_oval(25, 45, 180, 85, fill='blue')
canvas.create_text(100, 90, text='Canvasウィジェット', fill="green")

# PanedWindow 15
tk.Label(root, text="15: PanedFrame").grid(row=6, column=2, sticky="e")
panedwindow_frame = tk.Frame(root)
panedwindow_frame.grid(row=6, column=3, padx=10, pady=10)
panedwindow1 = tk.PanedWindow(panedwindow_frame)
text1 = tk.Text(panedwindow1, height=6, width=15)
text1.insert(tk.END, "中村拓男")
panedwindow1.add(text1)
panedwindow1.pack(fill=tk.BOTH, expand=2)
panedwindow2 = tk.PanedWindow(panedwindow1)
text2 = tk.Text(panedwindow1, height=6, width=15)
text2.insert(tk.END, "中村香織")
panedwindow2.add(text2)
panedwindow1.add(panedwindow2)


root.title("いろいろなウィジェット")
root.mainloop()


# from tkutil import TkUtil
# import os
# import tkinter as tk
# import tkinter.filedialog
#
#
# class MainClass:
#
#     def __init__(self):
#         root = TkUtil.create_tk_root()
#
#         # タイトル
#         root.title('Window Title')
#
#         # ボタン設置
#         btn = TkUtil.create_button(
#             tk_root=root,
#             message='Button',
#             on_click=self.on_button_browse_button)
#         TkUtil.place_button(button=btn, x=100, y=200)
#
#         self.file_name = tk.StringVar()
#         self.file_name.set('未選択です')
#         label = tk.Label(textvariable=self.file_name, font=('', 12))
#         label.pack(pady=0)
#
#         # 起動
#         TkUtil.run(tk_root=root)
#
#     def on_button_browse_button(self):
#         result = TkUtil.open_file_browse_window()
#         if len(result) <= 0:
#             self.file_name.set('選択をキャンセルしました')
#         else:
#             output = ''
#             for name in result:
#                 if len(output) > 0:
#                     output += '\n'
#                 output += name
#             self.file_name.set(output)
#
#
#     # # fTyp = [("", "*")]
#     #     # iDir = os.path.abspath(os.path.dirname(__file__))
#     #     # file_name = tk.filedialog.askopenfilenames(filetypes=fTyp, initialdir=iDir)
#     #     # print(file_name)
#     #     # if len(file_name) == 0:
#     #     #     self.file_name.set('選択をキャンセルしました')
#     #     # else:
#     #     #     self.file_name.set(file_name)
#     #     # return
#     #
#     # def file_dialog(self, event):
#     #     fTyp = [("", "*")]
#     #     iDir = os.path.abspath(os.path.dirname(__file__))
#     #     file_name = tk.filedialog.askopenfilename(filetypes=fTyp, initialdir=iDir)
#     #     if len(file_name) == 0:
#     #         self.file_name.set('選択をキャンセルしました')
#     #     else:
#     #         self.file_name.set(file_name)
#
#
# if __name__ == '__main__':
#     MainClass()
#
# # # ライブラリインポート
# # import tkinter as tk
# # from tkinter import ttk
# #
# # # 計算用配列の宣言
# # entry_list = []
# # entry_list_str = []
# # entry_list_join = []
# # calc_list_a = [0]
# # calc_list_b = [0]
# # operand_list = ['']
# # list_calc = []
# # list_calc_join = []
# # list_calc_result = []
# #
# #
# # # 数値入力処理
# # def add_number(num):
# #     display_list.set('')
# #     entry_list.append(num)
# #     entry_list_str = map(str, entry_list)
# #     entry_list_join.append(''.join(entry_list_str))
# #     display_list.set(entry_list_join[-1])
# #
# #
# # # 計算処理
# # def calc_function():
# #     if calc_list_b == '':
# #         pass
# #     else:
# #         if operand_list[-1] == '':
# #             pass
# #         else:
# #             calc_result.set(eval(str(calc_list_b[-1]) +
# #                                  str(operand_list[-1]) + str(calc_list_a[-1])))
# #             if calc_result.get()[-2:] == '.0':
# #                 calc_result.set(calc_result.get()[:-2])
# #             display_list.set(calc_result.get())
# #             calc_list_a.append(display_list.get())
# #
# #
# # # 加算処理
# # def plus_function():
# #     calc_list_b.append(calc_list_a[-1])
# #     calc_list_a.append(entry_list_join[-1])
# #     calc_function()
# #     operand_list.append('+')
# #     entry_list.clear()
# #
# #
# # # 減算処理
# # def minus_function():
# #     calc_list_b.append(calc_list_a[-1])
# #     calc_list_a.append(entry_list_join[-1])
# #     calc_function()
# #     operand_list.append('-')
# #     entry_list.clear()
# #
# #
# # # 乗算処理
# # def multiply_function():
# #     calc_list_b.append(calc_list_a[-1])
# #     calc_list_a.append(entry_list_join[-1])
# #     calc_function()
# #     operand_list.append('*')
# #     entry_list.clear()
# #
# #
# # # 除算処理
# # def devide_function():
# #     calc_list_b.append(calc_list_a[-1])
# #     calc_list_a.append(entry_list_join[-1])
# #     calc_function()
# #     operand_list.append('/')
# #     entry_list.clear()
# #
# #
# # # イコール押下時処理
# # def equal_function():
# #     calc_result.set(
# #         eval(str(calc_list_a[-1]) + str(operand_list[-1]) + str(entry_list_join[-1])))
# #     clear_function()
# #     display_list.set(calc_result.get())
# #
# #
# # # クリア処理
# # def clear_function():
# #     entry_list.clear()
# #     calc_list_a.clear()
# #     calc_list_b.clear()
# #     operand_list.clear()
# #     calc_list_a.append('0')
# #     calc_list_b.append('0')
# #     operand_list.append('')
# #     display_list.set('0')
# #
# #
# # # 符号変換処理
# # def sign_change_function():
# #     display_list.set(eval(str(display_list.get()) + ' * -1'))
# #     calc_list_a.append(display_list.get())
# #
# #
# # # Tkインスタンスの生成
# # root = tk.Tk()
# #
# # # windowのタイトル設定
# # root.title("Calculator")
# #
# # # Tkインスタンスを引数としてフレームインスタンスの生成
# # mainframe = ttk.Frame(root, padding="3 3 12 12")
# #
# # # フレームのグリッドを指定
# # mainframe.grid(column=0, row=0, sticky=("N", "W", "E", "S"))
# # root.columnconfigure(0, weight=1)
# # root.rowconfigure(0, weight=1)
# #
# # display_list = tk.StringVar()
# # calc_result = tk.StringVar()
# #
# # # ラベルとボタンを生成
# # ttk.Label(mainframe, textvariable=display_list).grid(
# #     column=2, row=1, sticky=("W", "E"))
# #
# # ttk.Button(mainframe, text="0", command=lambda: add_number(0)).grid(
# #     column=1, row=6, sticky="W")
# # ttk.Button(mainframe, text="1", command=lambda: add_number(1)).grid(
# #     column=1, row=5, sticky="W")
# # ttk.Button(mainframe, text="2", command=lambda: add_number(2)).grid(
# #     column=2, row=5, sticky="W")
# # ttk.Button(mainframe, text="3", command=lambda: add_number(3)).grid(
# #     column=3, row=5, sticky="W")
# # ttk.Button(mainframe, text="4", command=lambda: add_number(4)).grid(
# #     column=1, row=4, sticky="W")
# # ttk.Button(mainframe, text="5", command=lambda: add_number(5)).grid(
# #     column=2, row=4, sticky="W")
# # ttk.Button(mainframe, text="6", command=lambda: add_number(6)).grid(
# #     column=3, row=4, sticky="W")
# # ttk.Button(mainframe, text="7", command=lambda: add_number(7)).grid(
# #     column=1, row=3, sticky="W")
# # ttk.Button(mainframe, text="8", command=lambda: add_number(8)).grid(
# #     column=2, row=3, sticky="W")
# # ttk.Button(mainframe, text="9", command=lambda: add_number(9)).grid(
# #     column=3, row=3, sticky="W")
# #
# # ttk.Button(mainframe, text="+", command=lambda: plus_function()).grid(
# #     column=4, row=5, sticky="W")
# # ttk.Button(mainframe, text="-", command=lambda: minus_function()).grid(
# #     column=4, row=4, sticky="W")
# # ttk.Button(mainframe, text="×", command=lambda: multiply_function()).grid(
# #     column=4, row=3, sticky="W")
# # ttk.Button(mainframe, text="÷", command=lambda: devide_function()).grid(
# #     column=4, row=2, sticky="W")
# # ttk.Button(mainframe, text="=", command=lambda: equal_function()).grid(
# #     column=4, row=6, sticky="W")
# # ttk.Button(mainframe, text="C", command=lambda: clear_function()).grid(
# #     column=1, row=2, sticky="W")
# # ttk.Button(mainframe, text="+/-", command=lambda: sign_change_function()).grid(
# #     column=2, row=2, sticky="W")
# #
# # for child in mainframe.winfo_children():
# #     child.grid_configure(padx=0, pady=0)
# #
# # root.mainloop()