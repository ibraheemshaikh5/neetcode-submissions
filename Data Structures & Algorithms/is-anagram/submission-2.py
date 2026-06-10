class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        characters = set()

        for character in s:
            characters.add(character)

        for character in t:
            if character not in characters:
                return False
        
        return True