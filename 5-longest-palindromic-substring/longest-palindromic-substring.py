class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        longest = ""

        for i, ch in enumerate(s):
            # Odd length palindrome (center at i)
            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > len(longest):
                    longest = s[left:right+1]
                left -= 1
                right += 1

            # Even length palindrome (center between i and i+1)
            left, right = i, i+1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > len(longest):
                    longest = s[left:right+1]
                left -= 1
                right += 1

        return longest
