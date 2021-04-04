from typing import List
from tests.tests_rearrange_digits import TestCasesRotatedArraySearch
from solution.rearrange_digits import RearrangeDigits

if __name__ == "__main__":
    ###################################
    # Tests
    ###################################
    tests_rearrange_digits: TestCasesRotatedArraySearch = TestCasesRotatedArraySearch()

    tests_rearrange_digits.input_list_is_none_return_empty_list()
    tests_rearrange_digits.input_list_is_empty_list_return_empty_list()
    tests_rearrange_digits.input_list_has_one_element_return_list_with_element()

    tests_rearrange_digits.input_list_has_element_greater_nine_throw_value_exception()
    tests_rearrange_digits.input_list_has_element_smaller_zero_throw_value_exception()
    tests_rearrange_digits.input_list_has_element_is_str_throw_type_exception()
    tests_rearrange_digits.input_list_has_element_is_float_throw_type_exception()

    tests_rearrange_digits.input_list_sorted_return_max_sum()
    tests_rearrange_digits.input_list_unsorted_return_max_sum()
    tests_rearrange_digits.input_list_unsorted_with_duplicates_return_max_sum()

    ###################################
    # Demo
    ###################################
    rearrange_digits: RearrangeDigits = RearrangeDigits()

    input_list: list = [4, 6, 2, 5, 9, 8, 1]
    max_numbers: List[int] = rearrange_digits.main(input_list)
    print(max_numbers) # [9641, 852]