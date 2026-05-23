class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # left pointer
        l = 0

        # r is the right pointer
        for r in range(0, len(nums)):
            if nums[r] != val:
                nums[l] = nums[r]
                l += 1

        return l