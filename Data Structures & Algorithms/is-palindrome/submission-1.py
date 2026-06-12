class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l <= r:
            print(s[l].isalnum())
            # get alphanumeric
            while l < len(s) and not s[l].isalnum():
                l += 1
            while r > -1 and not s[r].isalnum():
                r -= 1
            if l < len(s) and r > -1 and s[l].lower() != s[r].lower():
                print(l, r)
                return False
            l += 1
            r -= 1

        return True