class Solution:
    def isValid(self, s: str) -> bool:
        # order matters so stack (lifo)
        brackets = {'(': ')', '{': '}', '[': ']'}
        exp_closing = []

        for c in s:
            if c in brackets:
                exp_closing.append(brackets[c])
            elif c in exp_closing:
                if c != exp_closing[-1]:
                    return False
                else:
                    exp_closing.pop()
            else:
                return False
        
        if not exp_closing:
            return True
        else:
            return False