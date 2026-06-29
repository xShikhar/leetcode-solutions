class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        sum_n = 0
        length = float('inf')
        left = 0 
        x = 0
        for right in range(len(nums)):
            sum_n += nums[right]
            while sum_n >= target:
                x = right - left + 1
                length = min(length,x)
                sum_n  -= nums[left]
                left += 1
        if length != float('inf'):
            return length
        else:
            return 0 
        
        

            
