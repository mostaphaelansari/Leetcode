class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        reverserd_half = 0
        while x > reverserd_half :
            digit = x % 10 
            x = x // 10 
            reverserd_half = reverserd_half *10 + digit
        return x == reverserd_half or x == reverserd_half//10