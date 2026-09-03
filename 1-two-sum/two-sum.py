class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}

        for i, num in enumerate(nums):
            rest = target - num

            if rest in d:
                return [d[rest], i]

            d[num] = i
