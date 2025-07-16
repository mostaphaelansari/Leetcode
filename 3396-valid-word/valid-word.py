class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False

        vowels = set('aeiouAEIOU')
        consonants = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ') - vowels
        
        has_vowel = False
        has_consonant = False
        
        for ch in word:
            if ch.isdigit():
                continue
            elif ch.isalpha():
                if ch in vowels:
                    has_vowel = True
                elif ch in consonants:
                    has_consonant = True
            else:
                # Invalid character found
                return False
        
        return has_vowel and has_consonant
