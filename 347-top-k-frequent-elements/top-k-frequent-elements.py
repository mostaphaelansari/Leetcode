from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_nums = Counter(nums)
        result = []
        for num , freq in dict_nums.items() : 
            if freq >= sorted(dict_nums.values(), reverse=True)[k - 1]:
                result.append(num)
        return result
        