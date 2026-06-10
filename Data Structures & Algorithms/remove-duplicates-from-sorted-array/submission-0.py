class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # declare a list for unique elements
        uniqueNums = []
        
        for i in range(len(nums)):
            # add first item in nums to new list
            if i == 0:
                uniqueNums.append(nums[i])
                continue

            # find unique values and add to unique list
            if nums[i] != nums[i - 1]:
                uniqueNums.append(nums[i])


        nums = uniqueNums

        return len(uniqueNums)

