from typing import List

class RearrangeDigits(object):
    def __init__(self) -> None:
        """Constructor.
        """
        pass

    def main(self: object, input_list: List[int]) -> List[int]:
        """Rearrange Array Elements so as to form two number such that their sum is maximum in O(n log n) time.

            Parameters
            ----------
            input_list : List[int], required
                List to rearrange.
            
            Returns
            ----------
            list
                Returns a list with the two maximum numbers.
        """

        if not input_list or len(input_list) == 0:
            return []
        if len(input_list) == 1:
            return input_list

        input_list_length: List[int] = len(input_list)
        left_result: List[int] = []
        right_result: List[int] = []

        sorted_list: List[int] = self.mergesort(input_list)

        for i in range(0, input_list_length, 2):
            first: int = sorted_list[i]
            left_result.append(first)

            if i+1 < input_list_length:
                second: int = sorted_list[i+1]
                right_result.append(second)

        left_result_str: List[int] = map(str, left_result)
        left_result_integer: int = int("".join(left_result_str))

        right_result_str: List[int] = map(str, right_result)
        right_result_integer: int = int("".join(right_result_str))
        
        return [left_result_integer, right_result_integer]


    def mergesort(self: object, input_list: List[int]) -> List[int]:
        """Sort input list descending.

            Parameters
            ----------
            input_list : List[int], required
                List to sort.
            
            Returns
            ----------
            list
                Returns a list in a descending order.
        """

        if len(input_list) <= 1:
            return input_list
        
        mid: int = len(input_list) // 2
        left: List[int] = input_list[:mid]
        right: List[int] = input_list[mid:]
        
        left = self.mergesort(left)
        right = self.mergesort(right)
        
        return self.merge(left, right)
    

    def merge(self: object, left: List[int], right: List[int]) -> List[int]:
        """Helper function for mergesort to merge two sorted list in a sorted one.

            Parameters
            ----------
            left : List[int], required
                First list.
            right : List[int], required
                Second list.
            
            Returns
            ----------
            list
                Returns a list with the two input list sorted in a descending way.
        """

        merged: List[int] = []
        left_index: int = 0
        right_index: int = 0
        
        while left_index < len(left) and right_index < len(right):
            if not isinstance(left[left_index], int) or not isinstance(right[right_index], int):
                raise TypeError("Only integers are allowed...")
            if left[left_index] > 9 or left[left_index] < 0 or right[right_index] > 9 or right[right_index] < 0:
                raise ValueError("Only integers between 0 and 9 are allowed...")
                
            if left[left_index] < right[right_index]:
                merged.append(right[right_index])
                right_index += 1
            else:
                merged.append(left[left_index])
                left_index += 1

        merged += left[left_index:]
        merged += right[right_index:]

        return merged