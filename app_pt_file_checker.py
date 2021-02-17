import pandas as pd
import numpy as np
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.filedialog
from tkinter import messagebox


class PT_INDEX:
    TEST_ID = 1
    TEST_INFO = 4
    INVALID = 18
    ASSIGNEE = 52
    TEST_DATE = 55
    TEST_RESULT = 59


class PT_SPEC:
    SHEET_TITLE_PAGE = 'Title Page'
    SHEET_BASIC_TEST = 'Basic Test (Online) 1'
    SHEET_BUSINESS_TEST = 'Business Test 1'
    RESULT_SUCCESS = "Passed"
    RESULT_FAIL = "Failed"


class FileChecker:

    # def __init__(self):
    #     # Create GUI here
    #     return

    @staticmethod
    def read_excel(file_path: str, sheet_name: str):
        return pd.read_excel(file_path, sheet_name='Basic Test (Online) 1')

    @staticmethod
    def is_empty(text) -> bool:
        if text is None or len(str(text)) <= 0:
            return True
        # if np.isnan(float(text)):
        #     return True
        return False

    @staticmethod
    def check_pt_spec(file_path: str) -> str:
        output_result = f"Checking file {file_path}\n"
        basic_sheet_result = FileChecker.check_pt_spec_sheet(file_path=file_path, sheet_name=PT_SPEC.SHEET_BASIC_TEST)
        business_sheet_result = FileChecker.check_pt_spec_sheet(file_path=file_path, sheet_name=PT_SPEC.SHEET_BUSINESS_TEST)

        output_result += basic_sheet_result[0]
        output_result += business_sheet_result[0]

        error_count = basic_sheet_result[1] + business_sheet_result[1]
        if error_count <= 1:
            output_result += "File check complete. No Error found.\n"
        else:
            output_result += f"File check complete. {error_count} Error found.\n"

        print(output_result)

        # output_result += f" -> Checking sheet {PT_SPEC.SHEET_BASIC_TEST}"

        # data = FileChecker.read_excel(file_path=file_path, sheet_name=PT_SPEC.SHEET_BASIC_TEST)
        # if data is None:
        #     output_result += "Read data is empty. Please check if file path and sheet name as expected."
        #     return output_result
        #
        # is_prev_row_fail_case = False
        # current_test_id = 0
        # error_count = 0
        # row_count = 0
        # for row in data.files:
        #     if is_prev_row_fail_case or not FileChecker.is_empty(row[PT_INDEX.TEST_INFO]):
        #         # If the test case is no need to run (invalid), skip
        #         if not FileChecker.is_empty(row[PT_INDEX.INVALID]):
        #             row_count += 1
        #             continue
        #
        #         current_test_id = row[PT_INDEX.TEST_ID]
        #
        #         # Check if name/date/result is filled in.
        #         if FileChecker.is_empty(row[PT_INDEX.ASSIGNEE]):
        #             output_result += f"Assignee info is missing at row {current_test_id}, test ID {current_test_id}\n"
        #             error_count += 1
        #         if FileChecker.is_empty(row[PT_INDEX.TEST_DATE]):
        #             output_result += f"Date info is missing at row {current_test_id}, test ID {current_test_id}\n"
        #             error_count += 1
        #         if is_prev_row_fail_case and FileChecker.is_empty(row[PT_INDEX.TEST_RESULT]):
        #             output_result += f"Test Result (success after failure) is missing at row {current_test_id}, test ID {current_test_id}\n"
        #             error_count += 1
        #         elif FileChecker.is_empty(row[PT_INDEX.TEST_RESULT]):
        #             output_result += f"Test Result is missing at row {current_test_id}, test ID {current_test_id}\n"
        #             error_count += 1
        #
        #     row_count += 1

        # if error_count <= 1:
        #     output_result += "File check complete. No Error found.\n"
        # else:
        #     output_result += f"File check complete. {error_count} Error found.\n"

    @staticmethod
    def check_pt_spec_sheet(file_path: str, sheet_name: str) -> (str, int):
        result = f"  -> Checking sheet {sheet_name}\n"

        data = FileChecker.read_excel(file_path=file_path, sheet_name=sheet_name)
        if data is None:
            result += "Read data is empty. Please check if file path and sheet name as expected."
            return result, 0

        data = data.fillna("")

        is_prev_row_fail_case = False
        is_first_line_of_test_case = False
        row_error_content = ""
        row_error_count = 0
        current_test_id = 0
        total_error_count = 0
        row_count = 2  # To make the value match
        for row in data.itertuples():
            # print(data[row_count])
            if is_prev_row_fail_case or not FileChecker.is_empty(row[PT_INDEX.TEST_INFO]):
                # If the test case is no need to run (invalid), skip
                value = row[PT_INDEX.INVALID]
                if not FileChecker.is_empty(value):
                    row_count += 1
                    continue

                if not FileChecker.is_empty(row[PT_INDEX.TEST_INFO]):
                    current_test_id = row[PT_INDEX.TEST_ID]

                is_first_line_of_test_case = FileChecker.is_empty(row[PT_INDEX.TEST_INFO])

                # Check if name/date/result is filled in.
                # Assignee is only needed for 1st line
                if FileChecker.is_empty(row[PT_INDEX.ASSIGNEE]) and is_first_line_of_test_case:
                    row_error_content += f"      -> Assignee info is missing at row {row_count}\n"
                    row_error_count += 1
                if FileChecker.is_empty(row[PT_INDEX.TEST_DATE]):
                    row_error_content += f"      -> Date info is missing at row {row_count}\n"
                    row_error_count += 1

                # Result check
                if is_prev_row_fail_case and FileChecker.is_empty(row[PT_INDEX.TEST_RESULT]):
                    row_error_content += f"      -> Test Result (success after failure) is missing at row {row_count}\n"
                    row_error_count += 1
                elif FileChecker.is_empty(row[PT_INDEX.TEST_RESULT]):
                    row_error_content += f"      -> Test Result is missing at row {row_count}\n"
                    row_error_count += 1
                # Check if result is failure, IF the result is filled in
                if FileChecker.is_empty(row[PT_INDEX.TEST_RESULT]):
                    is_prev_row_fail_case = False
                else:
                    is_prev_row_fail_case = PT_SPEC.RESULT_SUCCESS != row[PT_INDEX.TEST_RESULT]

                # Refine output info once the prev fail case flag is off (is the last line to check for this test ID)
                if not is_prev_row_fail_case:
                    if len(row_error_content) > 0:
                        total_error_count += row_error_count
                        result += f"    -> [ID:{current_test_id}] {row_error_count} errors\n"
                        result += row_error_content

                    row_error_content = ""
                    row_error_count = 0

            row_count += 1

        return result, total_error_count

    # # print(df)df
        # # row_index = 0
        # for row in df.values:
        #     # if {row}
        #     # if 0 <= row_index <= 40:
        #     print('Row index = ' + str(row_index))
        #     print(f'{row[3]} : {row[17]} : {row[51]} : {row[54]} : {row[58]}')
        # row_index += 1


if __name__ == '__main__':
    FileChecker.check_pt_spec(file_path="PT_Spec_Sample.xlsm")
    # file_checker = FileChecker()
    # file_checker