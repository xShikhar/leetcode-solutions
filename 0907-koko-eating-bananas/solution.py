from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def calculateTotalHours(piles, mid):   # no self
            totalH = 0
            for pile in piles:
                totalH += ceil(pile / mid)
            return totalH

        low = 1
        high = max(piles)

        while low <= high:
            mid = (low + high) // 2
            totalH = calculateTotalHours(piles, mid)   # no self

            if totalH <= h:
                high = mid - 1
            else:
                low = mid + 1

        return low
