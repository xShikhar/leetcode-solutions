
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        l = len(s)

        for i in range(l):
            
            s = s[l-1] + s[:l-1]

            if goal == s:

                return True

        return False
