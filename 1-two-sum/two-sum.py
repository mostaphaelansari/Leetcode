class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d ={}
        for i in range(len(nums)) :
            rest = target - nums[i]
            if rest in d :
                return [d[rest],i]
            d[nums[i]] = i
        return []