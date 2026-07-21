from collections import deque
from typing import List

class Solution:

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()  # will store indices, values in decreasing order
        result = []

        for i in range(len(nums)):
            # Remove indices that are out of the current window
            while dq and dq[0] <= i - k:
                dq.popleft()

            # Remove indices whose values are smaller than nums[i]
            # (they can never be the max while nums[i] is in the window)
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            dq.append(i)

            # Once we've seen at least k elements, record the max
            if i >= k - 1:
                result.append(nums[dq[0]])

        return result
