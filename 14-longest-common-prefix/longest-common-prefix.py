from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        # Start by assuming the whole first string is the prefix
        prefix = strs[0]
        
        for string in strs[1:]:
            # Shrink the prefix until it's a prefix of string
            while not string.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        
        return prefix
