class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word[0].isupper():
         
            if word.isupper():
                return True
            elif word[1:].islower():
                return True
            else:
                return False
                
        else:
            return word.islower()
