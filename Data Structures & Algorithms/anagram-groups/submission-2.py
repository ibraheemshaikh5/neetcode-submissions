class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for str in strs:
            counts = [0] * 26

            for char in str:
                index = ord(char) - ord('a')

                counts[index] += 1

            result[tuple(counts)].append(str)

        return list(result.values())

