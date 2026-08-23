class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0 
        r = len(heights)-1
        amount = 0 
        while l<r :
            width = r-l 
            height = min(heights[l],heights[r])
            amount = max(amount,width * height)
            if heights[l] < heights[r]:
                l += 1 
            else:
                r -=1 
        return amount 

        