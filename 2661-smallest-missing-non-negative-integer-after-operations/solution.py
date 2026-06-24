from collections import defaultdict

class Solution:
    def findSmallestInteger(self, nums: list[int], value: int) -> int:
        remainder_count = defaultdict(int)
        for num in nums:
            remainder_count[num % value] += 1
        
        mex = 0
        while remainder_count[mex % value] > 0:
            remainder_count[mex % value] -= 1
            mex += 1
        
        return mex
