class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # left pointer
        l = 1;

        # r is right pointer
        for r in range (1, len(nums)):
            # if value @ right pointer != value before
            if nums[r] != nums[r - 1]:
                nums[l] = nums[r]
                l += 1

        return l 

