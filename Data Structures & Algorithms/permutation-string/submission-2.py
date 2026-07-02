class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        output = False
        k = len(s1)
        l, r = 0, 0
        freq_s1 = defaultdict(int)

        if k <= len(s2):
            # create frequency map fpr s1
            for s in s1:
                freq_s1[s] += 1

            # iterate through each k sliding window and check frequencies
            while l < len(s2):
                freq_s2 = defaultdict(int)
                while (r - l) < k and r < len(s2):
                    freq_s2[s2[r]] += 1
                    r += 1
                print(freq_s2)
                if freq_s1 == freq_s2:
                    output = True
                l += 1
                r = l

        return output 