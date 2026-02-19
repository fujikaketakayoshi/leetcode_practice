from collections import deque
class Solution:
    def calculate(self, s: str) -> int:
        q = deque()

        def exec(q):
            total = int(q.popleft())
            while q:
                sign = q.popleft()
                num = int(q.popleft())
                if sign == '+':
                    total += num
                elif sign == '-':
                    total -= num
                elif sign == '*':
                    total *= num
                elif sign == '/':
                    total /= num
            return total

        total = 0
        for c in s:
            if c == ' ':
                continue
            q.append(c)
            if c == ')':
                sub_total = 0
                q2 = deque()
                while True:
                    v = q.pop()
                    if v == ')':
                        continue
                    elif v == '(':
                        break
                    q2.append(v)
                sub_total += exec(deque(reversed(q2)))
                q.append(sub_total)
        total += exec(q)

        return total

solution = Solution()
print(solution.calculate("1 + 1"))  # Output: 2
print(solution.calculate(" 2-1 + 2 "))  # Output: 3
print(solution.calculate("(1+(4+5+2)-3)+(6+8)"))  # Output: 23
