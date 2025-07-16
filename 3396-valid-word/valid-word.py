class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False

        vowels = set('aeiouAEIOU')
        has_vowel = has_consonant = False

        for ch in word:
            if ch.isdigit():
                continue
            if not ch.isalpha():  # Reject any non-alphanumeric character
                return False
            lower_ch = ch.lower()
            if lower_ch in 'aeiou':
                has_vowel = True
            else:
                has_consonant = True

        return has_vowel and has_consonant