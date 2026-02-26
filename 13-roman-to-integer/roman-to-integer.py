class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total = 0
        for i in range(len(s)):
            curr = roman_dict[s[i]]
            next_val = roman_dict[s[i + 1]] if i + 1 < len(s) else 0
            
            if curr < next_val:
                total -= curr  # e.g. IV → subtract 1
            else:
                total += curr  # e.g. VI → add 1
        
        return total
