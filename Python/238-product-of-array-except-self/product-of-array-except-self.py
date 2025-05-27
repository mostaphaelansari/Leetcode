from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n
        
        # Calculate prefix products in a single pass
        prefix = 1
        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]
            
        # Calculate the final result using postfix products in a single backward pass
        postfix = 1
        for i in range(n-1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]
            
        return result