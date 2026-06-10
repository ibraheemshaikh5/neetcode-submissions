class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = nums[0]
        result = []
        zeros = set()

        for i in range (1, len(nums)):
            if (nums[i] == 0):
                zeros.add(i)
            else: 
                product *= nums[i]

        for j in range(len(nums)):
            if not zeros:
                result.append(int(product/nums[j]))
            elif len(zeros) == 1 and j in zeros:
                result.append(int(product))
            else:
                result.append(0)
        
        return result
