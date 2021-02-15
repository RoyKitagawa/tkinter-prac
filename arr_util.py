import logging

__GET_ROW = True
__REMOVE_ROW = False

__PERFECT_MATCH = True
__PARTIAL_MATCH = False


# From double array, will return new double array with rows that matches criteria
def get_row_if_col_contains(_double_arr, _column_index, _keyword, _include_1st_row: bool = False):
    return __get_or_remove_row_if_col_contains(_double_arr, _column_index, _keyword, __PARTIAL_MATCH, __GET_ROW, _include_1st_row)


# From double array, will return new double array with rows that matches criteria
def get_row_if_col_equals(_double_arr, _column_index, _keyword, _include_1st_row: bool = False):
    return __get_or_remove_row_if_col_contains(_double_arr, _column_index, _keyword, __PERFECT_MATCH, __GET_ROW, _include_1st_row)


# From double array, will return new double array with rows that matches criteria
def remove_row_if_col_contains(_double_arr, _column_index, _keyword, _only_perfect_match=False, _include_1st_row: bool = False):
    return __get_or_remove_row_if_col_contains(_double_arr, _column_index, _keyword, __PARTIAL_MATCH, __REMOVE_ROW, _include_1st_row)


# From double array, will return new double array with rows that matches criteria
def remove_row_if_col_equals(_double_arr, _column_index, _keyword, _include_1st_row: bool = False):
    __get_or_remove_row_if_col_contains(_double_arr, _column_index, _keyword, __PERFECT_MATCH, __REMOVE_ROW, _include_1st_row)
    return


# Will return double array after adding/removing rows that does not match criteria
def __get_or_remove_row_if_col_contains(_double_arr, _column_index, _keyword, _only_perfect_match=False, _is_get=False, _include_1st_row: bool = False):
    output = []

    # Do nothing if row is invalid
    if len(_double_arr) <= 0:
        logging.warning('Cannot remove row since row size is <= 0')
        return _double_arr
    # Do nothing if specified column index for criteria is invalid
    if len(_double_arr[0]) <= _column_index:
        logging.warning('Cannot remove row since column size is out of index')
        return _double_arr

    # Creates new double array data, that matches given criteria
    row_index = 0
    for row in range(len(_double_arr)):
        if row_index == 0 and _include_1st_row:
            output.append(_double_arr[row_index])
        else:
            if _is_get:  # get rows that contains _keyword (remove rows not containing keyword)
                if _only_perfect_match and _keyword == _double_arr[row_index][_column_index]:
                    output.append(_double_arr[row_index])
                elif not _only_perfect_match and _keyword in _double_arr[row_index][_column_index]:
                    output.append(_double_arr[row_index])
            else:  # remove rows that does contain _keyword (remove rows containing keyword)
                if _only_perfect_match and _keyword != _double_arr[row_index][_column_index]:
                    output.append(_double_arr[row_index])
                elif not _only_perfect_match and _keyword not in _double_arr[row_index][_column_index]:
                    output.append(_double_arr[row_index])
        row_index += 1

    return output
