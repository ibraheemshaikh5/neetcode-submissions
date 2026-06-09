class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # pointers 
        repl = 0

        # loop through array once
        for r in range(0, len(nums)):
            if nums[r] != val:
                nums[repl] = nums[r]
                repl += 1

        return repl