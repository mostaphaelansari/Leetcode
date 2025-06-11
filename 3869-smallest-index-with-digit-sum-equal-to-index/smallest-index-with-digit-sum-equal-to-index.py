from typing import List

class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        d = dict(enumerate(nums))  # index -> value
        for i, value in d.items():
            digit_sum = sum(int(digit) for digit in str(value))
            if digit_sum == i:
                return i
        return -1