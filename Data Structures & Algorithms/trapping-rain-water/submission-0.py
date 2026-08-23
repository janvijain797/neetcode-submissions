class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = [] 
        left = 0 
        for i in range(len(height)):
            left = max(left,height[i])
            left_max.append(left)
        right_max = [0] * len(height) 
        right = 0 
        for i in range(len(height)-1, -1 ,-1 ):
            right = max(right,height[i])
            right_max[i] = right
        amount = 0  
        for j in range(len(height)):
            amount += min(left_max[j],right_max[j])-height[j]
        return amount 
