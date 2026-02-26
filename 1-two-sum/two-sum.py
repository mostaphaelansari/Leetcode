class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            complements = target - nums[i]
            if complements in seen :
                return [seen[complements], i]
            seen[num] = i
        return []

