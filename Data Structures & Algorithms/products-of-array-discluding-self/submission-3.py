class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        prefix, postfix = 1, 1

        # iterate once through the array
        for i in range(len(nums)):
            output[i] = prefix
            prefix *= nums[i]

        for j in range(len(nums) - 1, -1, -1):
            output[j] *= postfix
            postfix *= nums[j]

        return output
