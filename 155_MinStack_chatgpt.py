class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minStack:
            self.minStack.append(val)
        else:
            self.minStack.append(min(val, self.minStack[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]

solution = MinStack()
solution.push(-2)
print(solution.minStack)
solution.push(0)
print(solution.minStack)
solution.push(-3)
print(solution.minStack)
print(solution.getMin())  # return -3
solution.pop()
print(solution.top())     # return 0
print(solution.getMin())  # return -2
