class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # two pointer solution
        l = 0 
        r = len(numbers) - 1

        while l < len(numbers): # this is safe since there must be a solution  
            if numbers[l] + numbers[r] > target:
                r -= 1
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                return(list((l + 1, r + 1)))
        
        return