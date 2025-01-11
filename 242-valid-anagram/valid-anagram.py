class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        # Convert strings to lists of characters and sort them
        s_sorted = sorted(list(s))
        t_sorted = sorted(list(t))
        
        # Compare the sorted lists
        return s_sorted == t_sorted
        