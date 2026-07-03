class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # brute force:
            # build frequency map of s
            # loop for every combination of substring until hits mark

        output = ""
        t_map = defaultdict(int)
        
        for char in t:
            t_map[char] += 1

        temp_map = t_map

        for l in range(len(s)):
            temp_map = t_map.copy()
            count = len(t)
            for i in range(l, len(s)):
                if s[i] in temp_map:
                    if temp_map[s[i]] > 0:
                        count -= 1
                    temp_map[s[i]] -= 1

                if count == 0:
                    current_len = i - l + 1
                    if output == "" or current_len < len(output):
                        output = s[l: i + 1]
                    
        return output

