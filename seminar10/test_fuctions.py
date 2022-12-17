import pytest
from functions import digits_sum, find_max, filter_asc

list_example = [('123.45', 15), ('123', 6), ('0.5', 5)]


@pytest.mark.parametrize('str_num, result', list_example)
def test_digits_sum_good(str_num, result):
    assert digits_sum(str_num) == result


list_example_err = [('123,434', ValueError), (123.67, TypeError)]


@pytest.mark.parametrize('num, result_exception', list_example_err)
def test_digits_sum_with_err(num, result_exception):
    with pytest.raises(result_exception):
        digits_sum(num)


list_example = [('1 2 3 4 5', 5), ('1 5 3 4 2', 5), ('2 1 0 -1 -2', 2)]


@pytest.mark.parametrize('str_num, result', list_example)
def test_find_max_good(str_num, result):
    assert find_max(str_num) == result


list_example_err = [('1-2-3-4-5', ValueError), ('1 2 3 4 a', ValueError), (1, AttributeError)]


@pytest.mark.parametrize('num, result_exception', list_example_err)
def test_find_max_with_err(num, result_exception):
    with pytest.raises(result_exception):
        find_max(num)


list_example = [([1, 2, 2, 4, 3, 5], [1, 2, 4, 5]), ([5, 4, 3], [5]), ([1, 5, 2, 3, 4, 6, 1, 7], [1, 5, 6, 7])]


@pytest.mark.parametrize('lst, result', list_example)
def test_filter_asc_good(lst, result):
    assert filter_asc(lst) == result


list_example_err = [([{1: 2}, 2, 3], TypeError), ([{1: 2}, {3: 4}], TypeError)]


@pytest.mark.parametrize('lst, result_exception', list_example_err)
def test_filter_asc_with_err(lst, result_exception):
    with pytest.raises(result_exception):
        filter_asc(lst)
