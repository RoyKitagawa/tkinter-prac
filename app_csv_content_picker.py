import os
import csv_reader
import arr_util
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.filedialog
from tkinter import messagebox


class LABEL:
    NONE = ""
    QA = "QA"
    DEFECT = "Defect"
    CAUSE_PHASE_UI = "Cause-Phase-UI"
    CAUSE_PHASE_SS = "Cause-Phase-SS"
    CAUSE_PHASE_PG = "Cause-Phase-PG"
    CAUSE_PHASE_PT = "Cause-Phase-PT"
    CAUSE_PHASE_IT = "Cause-Phase-IT"
    AT_PHASE_UI = "At-Phase-UI"
    AT_PHASE_SS = "At-Phase-SS"
    AT_PHASE_PG = "At-Phase-PG"
    AT_PHASE_PT = "At-Phase-PT"
    AT_PHASE_IT = "At-Phase-IT"


class CSV_CONVERT_TARGET:
    NONE = 0
    QA_ISSUE = 1
    DEFECT = 2


class SEPARATOR:
    QA_ISSUE_CONTENT = "### Content"
    QA_ISSUE_RESULT = "### Result"
    DEFECT_CONTENT = "### Content"
    DEFECT_CAUSE = "### Cause"
    DEFECT_ACTION = "### Action"

class INDEX:
    EMPTY = -1              # For blank cell
    ISSUE_ID = 0
    URL = 1
    TITLE = 2
    STATE = 3               # Open or Closed
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
    ROWS_QA_ISSUE = [
        EMPTY,          # No
        STATE,
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
    ROWS_DEFECT = [
        EMPTY,          # No
        EMPTY,          # Invalid Marker
        EMPTY,          # Status
        EMPTY,          # Management Identification (Add in target phase from label)
        EMPTY,          # Management ID
        EMPTY,          # Defect Management No
        AUTHOR,
        CREATE_DATE,
        CREATE_DATE,
        DUE_DATE,
        TITLE,
        DESCRIPTION,    # Defect Content
        EMPTY,          # Scenario ID
        EMPTY,          # Test Case No
        EMPTY,          # Test Case ID
        EMPTY,          # Test Item No
        EMPTY,          # Subsystem Name
        EMPTY,          # Operation Process Name
        EMPTY,          # Process Name
        EMPTY,          # Frequency
        EMPTY,          # Affect Degree
        EMPTY,          # Importance
        EMPTY,          # Free Field
        EMPTY,          # Attachment
        ASSIGNEE,
        CREATE_DATE,
        DUE_DATE,
        CLOSED_DATE,
        EMPTY,          # Release Plan Date
        EMPTY,          # Release Complete Date
        DESCRIPTION,    # Defect Cause
        DESCRIPTION,    # Defect Action
        EMPTY,          # Cause Subsystem Name
        EMPTY,          # Cause Operation Process Name
        EMPTY,          # Cause Process Name
        EMPTY,          # Development Company
        ASSIGNEE,       # Developer
        LABEL,          # Cause Phase
        EMPTY,          # Cause Category
        EMPTY,          # Cause Type
        EMPTY,          # Cause Detail
        EMPTY,          # Defect Content
        EMPTY,          # Defect Cause
        EMPTY,          # Related Defect No
        EMPTY,          # Free Slot
        EMPTY,          # Attachment
        AUTHOR,         # Verifier
        DUE_DATE,
        CLOSED_DATE,
        EMPTY,          # Free Slot
        EMPTY,          # Attachment
        EMPTY,          # Modify Target
    ]


# App for picking needed info from csv, and formatting in new csv with only needed data, in specified order
class AppCsvContentPicker:

    # File type
    FILE_TYPE_CSV = ("CSV Files", "*.csv")
    OUTPUT_TYPE_QA_ISSUE = "QA_Issues"
    OUTPUT_TYPE_DEFECT = "Defect"

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
        # Output Type Label
        output_type_label = tk.Label(self.root, text='Output Type', anchor='w')
        output_type_label.grid(padx=10, pady=(10, 0), row=2, column=0, sticky=tk.W+tk.E)
        # Output dropdown
        self.output_combo = ttk.Combobox(self.root, state='readonly')
        self.output_combo['values'] = (self.OUTPUT_TYPE_QA_ISSUE, self.OUTPUT_TYPE_DEFECT)
        self.output_combo.current(0)
        self.output_combo.grid(padx=10, pady=(0, 10), row=3, column=0, sticky=tk.W+tk.E)

        # Output button
        output_btn = tk.Button(self.root, text='save output', command=self.on_button_save_file)
        output_btn.grid(padx=10, pady=(0, 10), row=3, column=1)

        self.root.mainloop()
        # TkUtil.run(self.root)

    def on_button_input_file_browse_button(self):
        result = tk.filedialog.askopenfilename(
            filetypes=[self.FILE_TYPE_CSV], initialdir=os.path.abspath(os.path.dirname(__file__)))
        self.input_file_path.delete('1.0', 'end')
        self.input_file_path.insert(tk.END, result)

    def on_button_save_file(self):
        target = self.output_combo.get()
        self.csv_convert_target = CSV_CONVERT_TARGET.NONE
        if self.OUTPUT_TYPE_DEFECT in target:
            self.csv_convert_target = CSV_CONVERT_TARGET.DEFECT
        elif self.OUTPUT_TYPE_QA_ISSUE in target:
            self.csv_convert_target = CSV_CONVERT_TARGET.QA_ISSUE

        if self.csv_convert_target is CSV_CONVERT_TARGET.NONE:
            messagebox.showinfo('Notification', 'No target is selected.\nPlease select csv convert target.')
            return

        result = tk.filedialog.asksaveasfilename(
            filetypes=[self.FILE_TYPE_CSV], initialdir=os.path.abspath(os.path.dirname(__file__)))

        if result is None or len(result) <= 0:
            return

        # change this depending on target.
        target_label = LABEL.NONE
        if self.csv_convert_target is CSV_CONVERT_TARGET.QA_ISSUE:
            target_label = LABEL.QA
        elif self.csv_convert_target is CSV_CONVERT_TARGET.DEFECT:
            target_label = LABEL.DEFECT

        # Get data for saving
        data = self.get_csv_data_from_input_path(expected_label=target_label)

        # No data found
        if data is None or len(data) <= 0:
            messagebox.showinfo('Notification', 'No data found from input.\nPlease check if file path exists with expected CSV.')
            return

        if self.csv_convert_target is CSV_CONVERT_TARGET.QA_ISSUE:
            data = CsvFormatter.format_for_qa_issue(data)
        elif self.csv_convert_target is CSV_CONVERT_TARGET.DEFECT:
            data = CsvFormatter.format_for_defect(data)
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
    def format_for_qa_issue(data):
        formatted_data = CsvFormatter.format(data, INDEX.ROWS_QA_ISSUE)

        col_index = 0
        loop_flg = True
        while loop_flg:
            # Index 12, format for qa content.
            # Index 17, format for qa response.
            description = formatted_data[col_index][12]

            formatted_data[col_index][12] = CsvFormatter.get_qa_issue_content(description)
            formatted_data[col_index][17] = CsvFormatter.get_qa_issue_result(description)

            col_index += 1
            if col_index >= len(data):
                loop_flg = False

        return formatted_data

    @staticmethod
    def format_for_defect(data):
        formatted_data = CsvFormatter.format(data, INDEX.ROWS_DEFECT)

        col_index = 0
        loop_flg = True
        while loop_flg:
            # 3 Phase Info
            # 37 Cause phase
            # 11 Defect Content
            # 30 Defect Cause
            # 31 Defect Action
            label = formatted_data[col_index][37]
            description = formatted_data[col_index][11]

            formatted_data[col_index][3] = CsvFormatter.get_at_phase_info(label)
            formatted_data[col_index][37] = CsvFormatter.get_cause_phase_info(label)
            formatted_data[col_index][11] = CsvFormatter.get_defect_content(description)
            formatted_data[col_index][30] = CsvFormatter.get_defect_cause(description)
            formatted_data[col_index][31] = CsvFormatter.get_defect_action(description)

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
        for row in range(len(data)):
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

    @staticmethod
    def get_cause_phase_info(label: str):
        cause_phase = ""
        if LABEL.CAUSE_PHASE_UI in label:
            cause_phase = "UI"
        elif LABEL.CAUSE_PHASE_SS in label:
            cause_phase = "SS"
        elif LABEL.CAUSE_PHASE_PG in label:
            cause_phase = "PG"
        elif LABEL.CAUSE_PHASE_PT in label:
            cause_phase = "PT"
        elif LABEL.CAUSE_PHASE_IT in label:
            cause_phase = "IT"
        return cause_phase

    @staticmethod
    def get_at_phase_info(label: str):
        at_phase = ""
        if LABEL.AT_PHASE_UI in label:
            at_phase = "UI"
        elif LABEL.AT_PHASE_SS in label:
            at_phase = "SS"
        elif LABEL.AT_PHASE_PG in label:
            at_phase = "PG"
        elif LABEL.AT_PHASE_PT in label:
            at_phase = "PT"
        elif LABEL.AT_PHASE_IT in label:
            at_phase = "IT"
        return at_phase

    @staticmethod
    def get_qa_issue_content(description: str = ""):
        if len(description) <= 0:
            return ""

        text = description.split(SEPARATOR.QA_ISSUE_CONTENT)
        if len(text) <= 1:
            return text[0].strip("\n")

        text = text[1].split(SEPARATOR.QA_ISSUE_RESULT)
        return text[0].strip("\n")

    @staticmethod
    def get_qa_issue_result(description: str = ""):
        if len(description) <= 0:
            return ""

        text = description.split(SEPARATOR.QA_ISSUE_RESULT)
        if len(text) <= 1:
            return text[0].strip("\n")

        return text[1].strip("\n")

    @staticmethod
    def get_defect_content(description: str = ""):
        if len(description) <= 0:
            return ""

        text = description.split(SEPARATOR.DEFECT_CONTENT)
        if len(text) <= 1:
            return text[0].strip("\n")

        text = text[1].split(SEPARATOR.DEFECT_CAUSE)
        return text[0].strip("\n")

    @staticmethod
    def get_defect_cause(description: str = ""):
        if len(description) <= 0:
            return ""

        text = description.split(SEPARATOR.DEFECT_CAUSE)
        if len(text) <= 1:
            return text[0].strip("\n")

        text = text[1].split(SEPARATOR.DEFECT_ACTION)
        return text[0].strip("\n")

    @staticmethod
    def get_defect_action(description: str = ""):
        if len(description) <= 0:
            return ""

        text = description.split(SEPARATOR.DEFECT_ACTION)
        if len(text) <= 1:
            return text[0].strip("\n")

        return text[1].strip("\n")


if __name__ == '__main__':
    AppCsvContentPicker()
