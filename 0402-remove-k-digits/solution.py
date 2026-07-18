class Solution:
    def removeKdigits(self, num: str, k: int) -> str:

        if k == len(num):
            return "0"

        num = num.strip()

        stack = []

        for i in range(len(num)):

            while stack and k > 0 and stack[-1] > num[i]:
                stack.pop()
                k -= 1

            stack.append(num[i])

        while k > 0:
            stack.pop()
            k -= 1

        res = ""

        while stack:
            res += stack[-1]
            stack.pop()

        res = res.rstrip('0')

        if not res:
            return "0"

        return res[::-1]
