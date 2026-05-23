class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # hashmap to store the amount of occurances
        # for each character in both strings
        map1 = {} # char : count
        map2 = {}

        # add first string to map: time O(n), memory O(n)
        for i in range(len(s)):
            map1[s[i]] = 1 + map1.get(s[i], 0) 
            map2[t[i]] = 1 + map2.get(t[i], 0) 

        return map1 == map2