class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # create a hashmap
        nums_unique = set()
        
        # loop through nums (1 pass)
        for n in nums:
            if n in nums_unique:
                return True    
            
            nums_unique.add(n)

        return False