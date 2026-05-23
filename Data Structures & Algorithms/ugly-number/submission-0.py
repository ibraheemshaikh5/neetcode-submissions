class Solution:
    def isUgly(self, n: int) -> bool:
        if n < 0: # positive integer
            return False

        for factor in [2, 3, 5]:
            while n % factor == 0:
                n //= factor
        
        return n == 1