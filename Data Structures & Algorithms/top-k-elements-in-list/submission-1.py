class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = defaultdict(int)
        results = [0] * k

        for num in nums:
            frequencies[num] += 1

        for i in range(k):
            highest = None
            for key in frequencies.keys():
                if highest == None or frequencies[key] > frequencies[highest]:
                    highest = key
            
            results[i] = highest
            del frequencies[highest]
        
        return results