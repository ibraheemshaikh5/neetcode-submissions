class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # width is differences btwn indices
        # length is the shorter bar
        # brute force solution
        max_water = 0

        for i in range(len(heights)):
            for j in range(i + 1, len(heights)):
                area = min(heights[i], heights[j]) * (j - i)
                max_water = max(max_water, area)
        
        return max_water