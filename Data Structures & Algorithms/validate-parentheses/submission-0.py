class Solution:
    def isValid(self, s: str) -> bool:
        # create hashmap for closing brackets and corresponding
        # opening brackets
        bracketPairs = {")" : "(", "]" : "[", "}" : "{"}

        # stack for all open brackets
        stack = []

        # loop through string 
        for c in s:
            # if it is a closing bracket
            # note: you're checking if any of the keys == c
            if c in bracketPairs:
                # if its a closing bracket, and stack isn't empty
                # search for corresponding opening at top of stack
                if stack and stack[-1] == bracketPairs[c]:
                    # note: stack[-1] is top of stack
                    # note: bracketPairs[c] is corresponding hashmap value
                    stack.pop()
                else:
                    # fails because the cbracket isn't closing anything directly
                    return False
            else:
                # if it isn't a closing bracket
                # add it to the stack (its an opening bracket)
                stack.append(c)

        # if the stack doesn't have any opening brackets -> return true
        return False if stack else True