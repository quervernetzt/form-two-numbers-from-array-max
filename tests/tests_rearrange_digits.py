import unittest
from solution.rearrange_digits import RearrangeDigits

class TestCasesRotatedArraySearch(unittest.TestCase):
    def input_list_is_none_return_empty_list(self: object) -> None:
        # Arrange
        rearrange_digits: RearrangeDigits = RearrangeDigits()
        input_list: list = None

        # Act
        result: list = rearrange_digits.main(input_list)

        # Assert
        self.assertEqual(result, [])
    
    def input_list_is_empty_list_return_empty_list(self: object) -> None:
        # Arrange
        rearrange_digits: RearrangeDigits = RearrangeDigits()
        input_list: list = []

        # Act
        result: list = rearrange_digits.main(input_list)

        # Assert
        self.assertEqual(result, [])

    def input_list_has_one_element_return_list_with_element(self: object) -> None:
        # Arrange
        rearrange_digits: RearrangeDigits = RearrangeDigits()
        input_list: list = [1]

        # Act
        result: list = rearrange_digits.main(input_list)

        # Assert
        self.assertEqual(result, [1])

    # ---------------------------------------------------------------------
    # ---------------------------------------------------------------------

    def input_list_has_element_greater_nine_throw_value_exception(self: object) -> None:
        # Arrange
        rearrange_digits: RearrangeDigits = RearrangeDigits()
        input_list: list = [4, 6, 2, 15, 9, 8]

        # Act & Assert
        self.assertRaises(ValueError, rearrange_digits.main, input_list)

    def input_list_has_element_smaller_zero_throw_value_exception(self: object) -> None:
        # Arrange
        rearrange_digits: RearrangeDigits = RearrangeDigits()
        input_list: list = [4, -6, 2, 5, 9, 8]

        # Act & Assert
        self.assertRaises(ValueError, rearrange_digits.main, input_list)

    def input_list_has_element_is_str_throw_type_exception(self: object) -> None:
        # Arrange
        rearrange_digits: RearrangeDigits = RearrangeDigits()
        input_list: list = [4, 6, 2, 5, "test", 8]

        # Act & Assert
        self.assertRaises(TypeError, rearrange_digits.main, input_list)
    
    def input_list_has_element_is_float_throw_type_exception(self: object) -> None:
        # Arrange
        rearrange_digits: RearrangeDigits = RearrangeDigits()
        input_list: list = [4, 6, 2, 5, 1.1, 8]

        # Act & Assert
        self.assertRaises(TypeError, rearrange_digits.main, input_list)

    # ---------------------------------------------------------------------
    # ---------------------------------------------------------------------
    
    def input_list_sorted_return_max_sum(self: object) -> None:
        # Arrange
        rearrange_digits: RearrangeDigits = RearrangeDigits()
        input_list: list = [1, 2, 3, 4, 5]

        # Act
        result: list = rearrange_digits.main(input_list)

        # Assert
        self.assertEqual(result, [531, 42])
    
    def input_list_unsorted_return_max_sum(self: object) -> None:
        # Arrange
        rearrange_digits: RearrangeDigits = RearrangeDigits()
        input_list: list = [4, 6, 2, 5, 9, 8]

        # Act
        result: list = rearrange_digits.main(input_list)

        # Assert
        self.assertEqual(result, [964, 852])

    def input_list_unsorted_with_duplicates_return_max_sum(self: object) -> None:
        # Arrange
        rearrange_digits: RearrangeDigits = RearrangeDigits()
        input_list: list = [4, 6, 2, 2, 5, 9, 9, 8]

        # Act
        result: list = rearrange_digits.main(input_list)

        # Assert
        self.assertEqual(result, [9852, 9642])