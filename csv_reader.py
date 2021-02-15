import csv
import pprint
import logging
import os
import copy

DEF_CSV_FILE_PATH = "C:/Users/S.NOMURA/PycharmProjects/pythonProject./dc2-emes-lomos-prod_issues_2020-12-08.csv"
DST_CSV_FILE_PATH_QA = "C:/Users/S.NOMURA/PycharmProjects/pythonProject./output_qa.csv"
DST_CSV_FILE_PATH_DEFECT = "C:/Users/S.NOMURA/PycharmProjects/pythonProject./output_defect.csv"

INDEX_START_ROW_INCLUDE_TITLE = 0
INDEX_START_ROW_REMOVE_TITLE = 1
INDEX_END_ALL_ROWS = -1


def write_csv_with_array(_content, _dst_file_path, _overwrite_if_exist=True):
    content = copy.copy(_content)
    if os.path.isfile(_dst_file_path):
        if not _overwrite_if_exist:
            logging.warning('Wriwrite_csv_with_arrayte cancelled due to already existing file : ' + _dst_file_path)
        else:
            os.remove(_dst_file_path)
            # file = open(_dst_file_path, 'w')
            # file.truncate(0) # Remove all existing contents
            # file.close()

    with open(_dst_file_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(content)


# Returns double array, with contents read from csv file
def read_csv_in_array_format(
        _csv_file_path,
        _column_indexes=[],
        _start_row=0,
        _end_row=-1):

    if not os.path.exists(_csv_file_path):
        return []

    # If no column is specified, set to read all columns
    if _column_indexes is None:
        _column_indexes = []
    if len(_column_indexes) <= 0:
        max_column = get_csv_column_count(_csv_file_path)
        for col_index in range(max_column):
            _column_indexes.append(col_index)

    # Read data from specified columns, into array format
    # Each index of array has whole data of its columns
    csv_input = []
    for index in _column_indexes:
        csv_input.append(get_column_data(_csv_file_path, index, _start_row, _end_row))

    # Prepare empty array for output
    csv_output = []
    for row in range(len(csv_input[0])):
        csv_output.append([])

    col_index = 0
    loop_flg = True

    # Convert input data to proper row, column format
    while loop_flg:
        row_index = 0
        for row in range(len(csv_input)):
            csv_output[col_index].append(csv_input[row_index][col_index])
            row_index += 1
        col_index += 1
        if col_index >= len(csv_input[0]):
            loop_flg = False

    return csv_output


# Start index of column is 0
def get_column_data(
        _file_path = DEF_CSV_FILE_PATH,
        column_index=0,
        _start_row=0,
        _end_row=-1):

    if _end_row < 0:
        _end_row = get_csv_row_count(_file_path)

    output = []
    with open(_file_path) as f:
        reader = csv.reader(f)

        # Get data of column needed
        i = 0
        for row in reader:
            if _start_row <= i <= _end_row:
                output.append(row[column_index])
            i += 1

    return output


# Get column count in csv file
def get_csv_column_count(_file_path=DEF_CSV_FILE_PATH):
    aaa = get_csv_row_count(_file_path)
    with open(_file_path) as f:
        reader = csv.reader(f)
        for row in reader:
            return len(row)

    return 0


# Get row count in csv file
def get_csv_row_count(_file_path=DEF_CSV_FILE_PATH):
    result = 0
    with open(_file_path) as f:
        reader = csv.reader(f)
        for row in reader:
            result += 1

    return result


def print_csv_content(_file_path = DEF_CSV_FILE_PATH):
    with open(_file_path) as f:
        print(f.read())

