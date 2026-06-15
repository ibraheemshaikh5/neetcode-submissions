class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        exp = []
        oper = {'+', '-', '*', '/'}

        for i in range(len(tokens)):
            if tokens[i] in oper:
                v2 = exp.pop()
                v1 = exp.pop()
                match tokens[i]:
                    case '+':
                        exp.append(v1 + v2)
                    case '-':
                        exp.append(v1 - v2)
                    case '*':
                        exp.append(int(v1 * v2))
                    case '/':
                        exp.append(int(v1 / v2))
            else:
                exp.append(int(tokens[i]))
            
        return exp[-1]