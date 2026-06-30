class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k < 0:
            return 0

        if k == 0:
            seen = set()
            duplicates = set()
            for n in nums:
                if n in seen:
                    duplicates.add(n)
                seen.add(n)
            return len(duplicates)

        unique = set(nums)
        count = 0
        for n in unique:
            if n + k in unique:
                count += 1

        return count
