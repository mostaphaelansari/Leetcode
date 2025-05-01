class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        
        for i in range(k):
            nums.sort()
            minimum = nums[0]
            index = nums.index(minimum)
            nums[index] = -nums[index]
        return sum(nums)
            