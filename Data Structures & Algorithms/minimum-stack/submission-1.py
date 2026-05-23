class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        tmp = []
        mini = self.stack[-1]

        # run while the stack has elements
        while len(self.stack):
            # compare the value of current min with last value in stack
            mini = min(mini, self.stack[-1])
            tmp.append(self.stack.pop())

        # add everything back to original stack
        while len(tmp):
            self.stack.append(tmp.pop())

        # return minimum value
        return mini
