class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # first thoughts are to sort but that won't be O(n)
        # maybe insert in order to a new data structure
        # you could store each and then keep adding as you go to length after

        # what if you create a set
        # then for each number you check if the next possible number in sequence
        # is available, then jump there... O(n^2) i think tho
        numbers = set()

        # create a set
        for num in nums:
            numbers.add(num)

        # iterate through the array
        max_length = 0
        for num in nums:
            # check if it's a beginning number
            if (num - 1) not in numbers:
                length = 1
                i = 1 
                while (num + i) in numbers:
                    length += 1
                    i += 1
                if length > max_length:
                    max_length = length

        return max_length