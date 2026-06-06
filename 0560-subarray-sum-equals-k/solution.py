class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        predi = {0:1}
        pres =  0
        cnt = 0 

        for i in range(len(nums)):
            pres += nums[i]
            if pres - k in predi:
                cnt += predi[pres-k]
            predi[pres] = predi.get(pres,0)  + 1
    
        return cnt
