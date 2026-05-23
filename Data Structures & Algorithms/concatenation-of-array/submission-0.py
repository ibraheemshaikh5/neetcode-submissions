class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [None] * n * 2

        for i in range(0, len(ans)):
            if i < n:
                ans[i] = nums[i]
                continue
            
            ans[i] = nums[i - n]

        return ans
