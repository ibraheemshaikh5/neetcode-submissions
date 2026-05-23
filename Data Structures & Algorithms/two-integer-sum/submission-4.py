class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # time complexity of O(n) using hashmaps
        hashmap = {} # val : index

        # now loop through everything once
        for i, n in enumerate(nums):
            difference = target - n

            if difference in hashmap:
                return [hashmap[difference], i]
            hashmap[n] = i
        
        return