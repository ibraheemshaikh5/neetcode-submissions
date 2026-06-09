class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create a hashmap using defaultdict
        # defaultdict prevents errors when accessing uninit keys
        hashmap = defaultdict(list) # when key doesn't exist create an empty list

        for str in strs:
            # create an array that's 26 indices long
            letters = [0] * 26

            for char in str:
                # use ascii of the character, map to letters array
                letters[ord(char) - ord('a')] += 1 # it's ord

            # set this as the key and the string as the value in hashmap
            # hashmaps cannot store lists as keys, so use tuple
            hashmap[tuple(letters)].append(str) # .append

        return list(hashmap.values())

            