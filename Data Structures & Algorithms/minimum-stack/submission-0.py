class MinStack:

    def __init__(self):
        self.stack = []
        self.length = 0

    def push(self, val: int) -> None:
        self.stack[self.length] = val
        self.length += 1

    def pop(self) -> None:
        self.stack[self.length] = None
        self.length -= 1

    def top(self) -> int:
        return self.stack[self.length]

    def getMin(self) -> int:
        return self.stack[0]
