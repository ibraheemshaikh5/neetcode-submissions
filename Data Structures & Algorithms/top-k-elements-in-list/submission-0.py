class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create a hashmap for all of the counts
        counts = defaultdict(int)
        result = []

        # iterate through the array to add to the hashmap
        for num in nums:
            counts[num] += 1

        print(counts.keys())

        for key in counts.keys():
            if counts[key] >= k: result.append(key)

        return result