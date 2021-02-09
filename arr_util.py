import logging

__GET_ROW = True
__REMOVE_ROW = False

__PERFECT_MATCH = True
__PARTIAL_MATCH = False


def get_row_if_col_contains(_double_arr, _column_index, _keyword):
    return __get_or_remove_row_if_col_contains(_double_arr, _column_index, _keyword, __PARTIAL_MATCH, __GET_ROW)


def get_row_if_col_equals(_double_arr, _column_index, _keyword):
    return __get_or_remove_row_if_col_contains(_double_arr, _column_index, _keyword, __PERFECT_MATCH, __GET_ROW)


def remove_row_if_col_contains(_double_arr, _column_index, _keyword, _only_perfect_match=False):
    return __get_or_remove_row_if_col_contains(_double_arr, _column_index, _keyword, __PARTIAL_MATCH, __REMOVE_ROW)


def remove_row_if_col_equals(_double_arr, _column_index, _keyword):
    __get_or_remove_row_if_col_contains(_double_arr, _column_index, _keyword, __PERFECT_MATCH, __REMOVE_ROW)
    return


def __get_or_remove_row_if_col_contains(_double_arr, _column_index, _keyword, _only_perfect_match=False, _is_get=False):
    output = []

    if len(_double_arr) <= 0:
        logging.warning('Cannot remove row since row size is <= 0')
        return _double_arr
    if len(_double_arr[0]) <= _column_index:
        logging.warning('Cannot remove row since column size is out of index')
        return _double_arr

    row_index = 0
    for row in range(len(_double_arr)):
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
