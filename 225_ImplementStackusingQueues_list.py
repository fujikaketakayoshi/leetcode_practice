class MyStack:

    def __init__(self):
        self.q1 = []
        self.h1 = 0
        self.q2 = []
        self.h2 = 0

    def _size1(self):
        return len(self.q1) - self.h1

    def push(self, x: int) -> None:
        # q2 に新要素追加
        self.q2.append(x)

        # q1 の残りを全部 q2 に移動
        while self.h1 < len(self.q1):
            self.q2.append(self.q1[self.h1])
            self.h1 += 1

        # 入れ替え
        self.q1, self.q2 = self.q2, []
        self.h1, self.h2 = 0, 0

    def pop(self) -> int:
        print(self.q1, self.h1)
        val = self.q1[self.h1]
        self.h1 += 1
        return val

    def top(self) -> int:
        return self.q1[self.h1]

    def empty(self) -> bool:
        return self._size1() == 0

solution = MyStack()
solution.push(1)
solution.push(2)
print(solution.pop())  # Output: 2
print(solution.top())  # Output: 1
print(solution.empty())  # Output: False
