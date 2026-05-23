class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # hashmap to store the amount of occurances
        # for each character in both strings
        map1 = {} # char : count
        map2 = {}

        # add first string to map: time O(n), memory O(n)
        for char in s:
            # check if already exists
            if char not in map1:
                map1[char] = 1
            else:
                map1[char] += 1
        
        # check that hashmap count is the same
        # add second string to map: time O(n), memory O(n)
        for char in t:
            # check if already exists
            if char not in map2:
                map2[char] = 1
            else:
                map2[char] += 1

        if map1 == map2:
            return True
        
        return False
        