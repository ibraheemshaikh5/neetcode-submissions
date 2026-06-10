class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # loop through and skip first item
        i = 1;

        while i < len(nums) - 1:
            # remove non-unique values
            if nums[i] == nums[i - 1]:
                nums.pop(i)
                i -= 1

        return len(nums)

