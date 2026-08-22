class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = [1] * len(nums)
        suff = [1] * len(nums)
        prod = [1]*len(nums) 
        for i in range(1,len(pref)):
            pref[i] = pref[i-1]* nums[i-1]
        for j in range(len(suff)-2, -1,-1):
            suff[j] = suff[j+1] * nums[j+1]
        for k in range(len(prod)):
            prod[k] = pref[k]*suff[k]
        return prod




        