from math import comb

class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        res = 0
        for k in range(4):
            sign = (-1)**k
            val = n - k*(limit + 1)
            if val < 0:
                # When val < 0, comb(val + 3 - 1, 3 - 1) = 0
                continue
            res += sign * comb(3, k) * comb(val + 3 - 1, 3 - 1)
        return res
