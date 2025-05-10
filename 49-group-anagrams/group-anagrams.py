from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)  # Initialize a defaultdict with lists as default values
        for k, v in enumerate(strs):
            # Use the sorted version of the string as a key
            key = ''.join(sorted(v))
            d[key].append(v)  # Append the string to the correct group
        return list(d.values())  # Return the grouped values as a list of lists