class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        sortedNums = nums1 + nums2
        sortedNums.sort()

        l, r = 0, len(sortedNums) - 1

        if len(sortedNums) % 2 != 0:
            while l < r:
                l += 1
                r -= 1
            return sortedNums[l]
        else:
            while l + 1 < r:
                l += 1
                if l + 1 < r:
                    r -= 1
            return ((sortedNums[l] + sortedNums[r]) / 2)