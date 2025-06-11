from typing import List

class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i, value in enumerate(nums):
            digit_sum = sum(int(d) for d in str(value))
            if digit_sum == i:
                return i
        return -1
