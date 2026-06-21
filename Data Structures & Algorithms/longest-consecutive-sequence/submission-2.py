class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # create a set
        num_set = set()

        for num in nums:
            num_set.add(num)
        
        longest = 0
        # check if prev in set
        for num in nums:
            temp = 1
            if num - 1 not in num_set:
                while num + temp in num_set:
                    temp += 1
                
            longest = max(temp, longest)
        
        return longest