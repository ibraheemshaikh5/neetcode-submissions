class Solution:
    def climbStairs(self, n: int) -> int:
        # create a recursive function
        def counter(n: int) -> int:
            # at each step you can go one down or two down
            # need to add up all of those possibilities
            if (n < 2):
                return 1;
            else:
                return counter(n - 2) + counter(n - 1)
        
        return counter(n)

