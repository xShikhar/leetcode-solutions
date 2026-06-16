class Solution:
    def longestPalindrome(self, s: str) -> int:
        letter = {}

        for i in range(len(s)):
            letter[s[i]] = letter.get(s[i],0) + 1

        c = 0
        has_odd = False

        for i in letter:
            if letter[i]%2==0 :
                c += letter[i]
            elif letter[i]%2 != 0:
                c = c + letter[i] - 1
                has_odd = True

        return c + 1 if has_odd else c
