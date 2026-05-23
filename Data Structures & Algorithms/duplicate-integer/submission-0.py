class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        prevMap = {} # val : index

        for i, n in enumerate(nums):
            if n in prevMap:
                return True
            prevMap[n] = i # add to map

        return False