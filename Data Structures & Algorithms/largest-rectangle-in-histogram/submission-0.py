class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = [] # start index, height

        for i, h in enumerate(heights):
            start = i
            while stack and h < stack[-1][1]:
                area = stack[-1][1] * (i - stack[-1][0])
                max_area = max(area, max_area)
                start = stack[-1][0]
                stack.pop()

            stack.append([start, h])

        while stack:
            area = stack[-1][1] * (len(heights) - stack[-1][0])
            max_area = max(area, max_area)
            stack.pop()

        return max_area