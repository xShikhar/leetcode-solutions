class Solution:
    def sumSubarrayMins(self, arr: list[int]) -> int:
        MOD = 10**9 + 7
        n = len(arr)

        # Previous Strictly Smaller Element index
        prev_smaller = [-1] * n
        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            prev_smaller[i] = stack[-1] if stack else -1
            stack.append(i)

        # Next Smaller-or-Equal Element index
        next_smaller_eq = [n] * n
        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] >= arr[i]:   # FIXED: >= instead of >
                next_smaller_eq[stack.pop()] = i
            stack.append(i)

        total = 0
        for i in range(n):
            left = i - prev_smaller[i]
            right = next_smaller_eq[i] - i
            total = (total + arr[i] * left * right) % MOD

        return total
