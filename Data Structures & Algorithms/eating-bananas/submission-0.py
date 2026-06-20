class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # use bst in a range
        l, r = 1, max(piles)
        output = r

        while l <= r:
            k = (l + r) // 2
            hours = 0

            for p in piles:
                hours += math.ceil(p / k)
            
            if hours <= h:
                output = min(output, k)
                r = k - 1
            else:
                l = k + 1

        return output

