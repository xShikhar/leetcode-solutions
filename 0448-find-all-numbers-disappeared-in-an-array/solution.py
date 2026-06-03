class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        result = []
        n= len(nums)
        nums = set(nums)
        for i in range(n):
            if i+1 not in nums:
                result.append(i+1)

        return result

