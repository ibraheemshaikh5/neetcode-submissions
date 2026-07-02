class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        output = False
        k = len(s1)
        l, r = 0, 0
        freq_s1 = defaultdict(int)
        freq_s2 = defaultdict(int)

        if k <= len(s2):
            # create frequency map fpr s1
            for s in s1:
                freq_s1[s] += 1

            # iterate through each k sliding window and check frequencies
            while r < len(s2):
                while (r - l) < k:
                    freq_s2[s2[r]] += 1
                    r += 1
                
                if freq_s1 == freq_s2:
                    output = True

                if freq_s2[s2[l]] > 1:
                    freq_s2[s2[l]] -= 1
                else:
                    freq_s2.pop(s2[l], None)
                l += 1

        return output 