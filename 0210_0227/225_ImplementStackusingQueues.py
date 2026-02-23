from collections import deque
class MyStack:

    def __init__(self):
        self.stack = deque()

    def push(self, x: int) -> None:
        self.stack.appendleft(x)

    def pop(self) -> int:
        return self.stack.popleft()

    def top(self) -> int:
        return self.stack[0]

    def empty(self) -> bool:
        return True if len(self.stack) == 0 else False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

solution = MyStack()
solution.push(1)
solution.push(2)
print(solution.top())  # Output: 2
print(solution.pop())  # Output: 2
print(solution.empty())  # Output: False
