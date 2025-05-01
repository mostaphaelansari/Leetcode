class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        d={}
        for i in range(k):
            minimum = min(nums)
            index = nums.index(minimum)
            nums[index] = -nums[index]
        return sum(nums)
            