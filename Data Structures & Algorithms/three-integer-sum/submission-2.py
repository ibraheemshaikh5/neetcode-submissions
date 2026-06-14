class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []

        # use python's built in sort
        nums.sort()

        # two sum II
        for j in range(len(nums)):
            if j > 0 and nums[j] == nums[j-1]:
                continue

            l = j + 1
            r = len(nums) - 1
            while l < r:
                if nums[j] + nums[l] + nums[r] > 0:
                    r -= 1
                elif nums[j] + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    output.append([nums[j], nums[l], nums[r]])
                    l += 1
                    r -= 1

        return output