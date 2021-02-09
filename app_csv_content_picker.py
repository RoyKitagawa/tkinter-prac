
import csv_reader
import gui
import arr_util
import tkinter
from tkutil import TkUtil
import tkinter as tk


# App for picking needed info from csv, and formatting in new csv with only needed data, in specified order
class AppCsvContentPicker(tk.Tk):

    # Basic csv index info about csv exported from GitLab
    INDEX_ISSUE_ID = 0
    INDEX_TITLE = 2
    INDEX_DESCRIPTION = 4
    INDEX_ASSIGNEE = 7
    INDEX_LABEL = 17
    INDEX_TIME_ESTIMATE = 18
    INDEX_TIME_SPENT = 19

    INDEX_SET_QA = [
        INDEX_ISSUE_ID,
        INDEX_TITLE,
        INDEX_ASSIGNEE,
        INDEX_LABEL
    ]

    def __init__(self):
        self.root = TkUtil.create_tk_root()

        # タイトル
        self.root.title('Window Title')

        # self.select_path = TkUtil.get_string_var('')
        self.input_file_path = tk.Text(self.root, width=100, height=1)
        self.input_file_path.delete('1.0', 'end')
        self.input_file_path.grid(padx=10, pady=10, row=0, column=0)

#         # Text 12
# #        tk.Label(self.root, text="12: Text").grid(row=3, column=2, sticky="e")
#         text = tk.Text(self.root, width=20, height=6)
#         text.insert(tk.END, "sample text\n1\n2\n3")
#         text.grid(row=3, column=3, padx=10, pady=10)

        # ボタン設置
        btn = TkUtil.create_button(
            tk_root=self.root,
            message='Button',
            on_click=self.on_button_browse_button)
        btn.grid(padx=10, pady=10, row=0, column=1)
        # TkUtil.place_button(button=btn, x=100, y=200)

        # self.label_message = TkUtil.get_string_var('Default Value')
        # label = TkUtil.create_label(message=self.label_message)
        # TkUtil.place_label(label)
        TkUtil.run(self.root)

    def on_button_browse_button(self):
        result = TkUtil.open_file_browse_window()
        # if len(result) <= 0:
        #     self.select_path.set('選択をキャンセルしました')
        # else:
        #     output = ''
        #     for name in result:
        #         if len(output) > 0:
        #             output += '\n'
        #         output += name
        #     self.select_path.set(output)
        output = ''
        for name in result:
            if len(output) > 0:
                output += '\n'
            output += name

        self.input_file_path.delete('1.0', 'end')
        self.input_file_path.insert(tk.END, output)

        # indexes = [
        #     0,  # issue id
        #     # 2,  # title
        #     # 4,  # description
        #     7,  # assignee
        #     17,  # label
        #     # 18,  # time estimate
        #     # 19,  # time spent
        # ]
        #
        # csv_output = csv_reader.read_csv_in_array_format(
        #     csv_reader.DEF_CSV_FILE_PATH,
        #     indexes,
        #     csv_reader.INDEX_START_ROW_INCLUDE_TITLE,
        #     csv_reader.INDEX_END_ALL_ROWS)
        #
        # csv_reader.write_csv_with_array(
        #     arr_util.get_row_if_col_contains(csv_output, 2, "QA"),
        #     True)
        #
        # # _gui = gui.TkinterGui()
        # # _gui.show_gui()


if __name__ == '__main__':
    AppCsvContentPicker()
