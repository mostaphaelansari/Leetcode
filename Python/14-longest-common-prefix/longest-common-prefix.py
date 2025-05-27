from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        # Commence avec le premier mot comme préfixe
        prefix = strs[0]
        
        # Compare le préfixe avec chaque mot dans la liste
        for word in strs[1:]:
            while not word.startswith(prefix):
                # Réduit le préfixe d’un caractère à la fois
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        
        return prefix
