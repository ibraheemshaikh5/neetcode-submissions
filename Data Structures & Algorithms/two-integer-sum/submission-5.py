class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} # val : index

        # one pass through list
        for i, n in enumerate(nums): 
            diff = target - n # store difference

            if diff in prevMap:
                return [prevMap[diff], i]
            
            # add to prevmap
            prevMap[n] = i
        return