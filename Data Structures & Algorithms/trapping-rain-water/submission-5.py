class Solution:
    def trap(self, height: List[int]) -> int:
        # implementing neetcode solution
        # O(n) memory, store maxLeft and maxRight
        maxLeft, maxRight = [0] * len(height), [0] * len(height)
        m = 0

        for i in range(len(height)):
            if height[i] > m:
                m = height[i]
            maxLeft[i] = m
            
        m = 0
        for i in range(len(height) - 1, -1, -1):
            if height[i] > m:
                m = height[i]
            maxRight[i] = m
        
        total_water = 0
        for j in range(len(height)):

            water = min(maxRight[j], maxLeft[j]) - height[j]
            total_water += max(water, 0)
         
        return total_water

        