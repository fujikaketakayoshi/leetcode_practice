class MyQueue:

    def __init__(self):
        self.front = []
        self.back = []

    def push(self, x: int) -> None:
        self.front.append(x)

    def pop(self) -> int:
        self.back = list(reversed(self.front)) + self.back
        self.front = []
        return self.back.pop()

    def peek(self) -> int:
        self.back = list(reversed(self.front)) + self.back
        self.front = []
        return self.back[-1] if self.back else None
    def empty(self) -> bool:
        return False if self.front or self.back else True

        


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(1)
obj.push(2)
print(obj.pop())
print(obj.peek())
print(obj.empty())

