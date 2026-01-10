class MinStack:

    def __init__(self):
        self.stack = []
        self.index = -1
        self.min = float('INF')

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.index += 1
        self.min = min(self.min, val)

    def pop(self) -> None:
        if self.index != -1:
            self.stack.pop()
            self.index -= 1
            if len(self.stack) != 0:
                self.min = min(self.stack)
            else:
                self.min = float('INF')

    def top(self) -> int:
        return self.stack[self.index]

    def getMin(self) -> int:
        return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

solution = MinStack()
solution.push(-2)
solution.push(0)
solution.push(-3)
print(solution.getMin())  # return -3
solution.pop()
print(solution.top())     # return 0
print(solution.getMin())  # return -2
