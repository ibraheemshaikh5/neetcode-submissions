class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        prev = set() # val : index

        for num in nums:
            if num in prev:
                return True
            prev.add(num) # add to set
        return False