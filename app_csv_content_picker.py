import os
import csv_reader
import arr_util
import tkinter as tk
import tkinter.filedialog
from tkinter import messagebox


class LABEL:
    NONE = ""
    QA = "QA"
    ISSUE = "ISSUE"


class CSV_CONVERT_TARGET:
    NONE = 0
    QA = 1
    ISSUE = 2


class SEPARATOR:
    QA_CONTENT = "### QA Content"
    QA_RESULT = "### QA Result"

class INDEX:
    EMPTY = -1              # For blank cell
    ISSUE_ID = 0
    URL = 1
    TITLE = 2
    State = 3               # Open or Closed
    DESCRIPTION = 4
    AUTHOR = 5
    AUTHOR_USER_NAME = 6    # Will not use
    ASSIGNEE = 7
    ASSIGNEE_USER_NAME = 8
    CONFIDENTIAL = 9        # Will not use
    LOCKED = 10             # Will not use
    DUE_DATE = 11
    CREATE_DATE = 12
    UPDATE_DATE = 13
    CLOSED_DATE = 14
    MILESTONE = 15          # Will not use
    WEIGHT = 16             # Will not use
    LABEL = 17
    TIME_ESTIMATE = 18
    TIME_SPENT = 19

    ROWS_ALL = []
    ROWS_QA = [
        EMPTY,          # No
        EMPTY,          # Status
        CREATE_DATE,
        AUTHOR,
        EMPTY,          # Hidden Row
        EMPTY,          # Hidden Row
        EMPTY,          # Hidden Row
        EMPTY,          # Hidden Row
        EMPTY,          # Category
        EMPTY,          # Feature name
        TITLE,
        EMPTY,          # Content JA
        DESCRIPTION,    # To be separated for only content
        ASSIGNEE,
        DUE_DATE,
        CLOSED_DATE,
        EMPTY,
        DESCRIPTION,    # To be separated for only result
        EMPTY,          # Remark
    ]


# App for picking needed info from csv, and formatting in new csv with only needed data, in specified order
class AppCsvContentPicker:

    # Basic csv index info about csv exported from GitLab

    # INDEX_EMPTY_CELL = -1
    # INDEX_ISSUE_ID = 0
    # INDEX_URL = 1
    # INDEX_TITLE = 2
    # INDEX_State = 3             # Open or Closed
    # INDEX_DESCRIPTION = 4
    # INDEX_AUTHOR = 5
    # INDEX_AUTHOR_USER_NAME = 6  # Will not use
    # INDEX_ASSIGNEE = 7
    # INDEX_CONFIDENTIAL = 8      # Will not use
    # INDEX_
    # INDEX_LABEL = 17
    # INDEX_TIME_ESTIMATE = 18
    # INDEX_TIME_SPENT = 19

    # # Index for each label, for each set
    # INDEX_LABEL_QA_FOR_SET_QA = 3

    # File type
    FILE_TYPE_CSV = ("CSV Files", "*.csv")

    def __init__(self):

        self.csv_convert_target = CSV_CONVERT_TARGET.NONE

        # Create Window
        self.root = tk.Tk()

        # Title
        self.root.title('CSV Picker')

        # Input Block
        # Label input
        input_label = tk.Label(self.root, text='Input File', anchor='w')
        input_label.grid(padx=10, pady=(10, 0), row=0, column=0, sticky=tk.W+tk.E)
        # Input file path
        self.input_file_path = tk.Text(self.root, width=100, height=1)
        self.input_file_path.delete('1.0', 'end')
        self.input_file_path.grid(padx=(10, 0), pady=(0, 10), row=1, column=0)
        # Input button
        input_btn = tk.Button(self.root, text='select file', command=self.on_button_input_file_browse_button)
        input_btn.grid(padx=10, pady=(0, 10), row=1, column=1)

        # Output button
        output_btn = tk.Button(self.root, text='save output', command=self.on_button_save_file)
        output_btn.grid(padx=10, pady=(0, 10), row=2, column=0)

        self.root.mainloop()
        # TkUtil.run(self.root)

    def on_button_input_file_browse_button(self):
        result = tk.filedialog.askopenfilename(
            filetypes=[self.FILE_TYPE_CSV], initialdir=os.path.abspath(os.path.dirname(__file__)))
        self.input_file_path.delete('1.0', 'end')
        self.input_file_path.insert(tk.END, result)

    def on_button_save_file(self):
        if self.csv_convert_target is CSV_CONVERT_TARGET.NONE:
            self.csv_convert_target = CSV_CONVERT_TARGET.QA
            # messagebox.showinfo('Notification', 'No target is selected.\nPlease select csv convert target.')
            # return

        result = tk.filedialog.asksaveasfilename(
            filetypes=[self.FILE_TYPE_CSV], initialdir=os.path.abspath(os.path.dirname(__file__)))

        if result is None or len(result) <= 0:
            return

        # change this depending on target.
        target_label = LABEL.NONE
        if self.csv_convert_target is CSV_CONVERT_TARGET.QA:
            target_label = LABEL.QA
        elif self.csv_convert_target is CSV_CONVERT_TARGET.ISSUE:
            target_label = LABEL.ISSUE

        # Get data for saving
        data = self.get_csv_data_from_input_path(expected_label=target_label)

        # No data found
        if data is None or len(data) <= 0:
            messagebox.showinfo('Notification', 'No data found from input.\nPlease check if file path exists with expected CSV.')
            return

        if self.csv_convert_target is CSV_CONVERT_TARGET.QA:
            data = CsvFormatter.format_for_qa(data)
        elif self.csv_convert_target is CSV_CONVERT_TARGET.ISSUE:
            data = CsvFormatter.format_for_qa(data) # To be changed later
        else:
            messagebox.showinfo('Notification', 'Unexpected target is selected.\nWill stop csv export.')
            return

        if data is None or len(data) <= 0:
            messagebox.showinfo('Notification', 'Output is empty.\nWill stop csv export.')
            return

        self.save_csv_data(data=data, dst_file_path=result)
        # Show popup if success
        messagebox.showinfo('Notification', 'Save CSV complete!')

    def get_csv_data_from_input_path(self, expected_label):
        csv_output = csv_reader.read_csv_in_array_format(
            self.input_file_path.get(1.0, tk.END+"-1c"),
            INDEX.ROWS_ALL,
            csv_reader.INDEX_START_ROW_INCLUDE_TITLE,
            csv_reader.INDEX_END_ALL_ROWS)

        if len(expected_label) > 0:
            return arr_util.get_row_if_col_contains(
                csv_output,
                INDEX.LABEL,
                expected_label,
                True)
        else:
            return csv_output   # Just return read content if no label target is set

    @staticmethod
    def save_csv_data(data, dst_file_path: str):
        # Add in ".csv" if file name does not end with ".csv"
        if not dst_file_path.endswith('.csv'):
            dst_file_path += '.csv'

        # Save data
        csv_reader.write_csv_with_array(
            _content=data,
            _dst_file_path=dst_file_path,
            _overwrite_if_exist=True)


class CsvFormatter:
    @staticmethod
    def format_for_qa(data):
        formatted_data = CsvFormatter.format(data, INDEX.ROWS_QA)

        col_index = 0
        loop_flg = True
        while loop_flg:
            # Index 12, format for qa content.
            # Index 17, format for qa response.
            text = formatted_data[col_index][12].split(SEPARATOR.QA_CONTENT)
            if len(text) > 1:
                result = text[1]
                result = result.split(SEPARATOR.QA_RESULT)

                if len(result) > 1:
                    formatted_data[col_index][12] = result[0].strip("\n")
                    formatted_data[col_index][17] = result[1].strip("\n")

            col_index += 1
            if col_index >= len(data):
                loop_flg = False

        return formatted_data

    @staticmethod
    def format(data, rows_info):
        if data is None or len(data) <= 0:
            return None

        # Prepare empty array
        output = []
        for row in range(len(data[0])):
            output.append([])

        col_index = 0
        row_index = 0
        loop_flg = True
        while loop_flg:
            row_index = 0
            for row in range(len(rows_info)):
                if rows_info[row_index] is INDEX.EMPTY:
                    output[col_index].append("")
                else:
                    index = rows_info[row_index]
                    output[col_index].append(data[col_index][rows_info[row_index]])
                row_index += 1
            col_index += 1
            if col_index >= len(data):
                loop_flg = False

        return output


if __name__ == '__main__':
    AppCsvContentPicker()
