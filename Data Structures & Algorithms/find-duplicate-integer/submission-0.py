class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # easy to use a set
        unums = set()
        
        for n in nums:
            if n in unums:
                return n
            unums.add(n)
        
        return -1