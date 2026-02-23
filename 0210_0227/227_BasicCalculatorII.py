class Solution:
    def calculate(self, s: str) -> int:
        num = 0
        stack = []
        for c in s:
            if c == ' ':
                continue
            elif c.isdigit():
                num = num * 10 + int(c)
            elif c in '+-*/':
                stack.append(num)
                stack.append(c)
                num = 0

        stack.append(num)

        i = 0
        while i < len(stack):
            if stack[i] == '*':
                tmp = stack[i - 1] * stack[i + 1]
                stack[i - 1] = tmp
                stack.pop(i + 1)
                stack.pop(i)
                i -= 1
            elif stack[i] == '/':
                tmp = stack[i - 1] // stack[i + 1]
                stack[i - 1] = tmp
                stack.pop(i + 1)
                stack.pop(i)
                i -= 1
            i += 1
        
        i = 0
        while i < len(stack):
            if stack[i] == '+':
                tmp = stack[i - 1] + stack[i + 1]
                stack[i - 1] = tmp
                stack.pop(i + 1)
                stack.pop(i)
                i -= 1
            elif stack[i] == '-':
                tmp = stack[i - 1] - stack[i + 1]
                stack[i - 1] = tmp
                stack.pop(i + 1)
                stack.pop(i)
                i -= 1
            i += 1
        return stack[0]

solution = Solution()
print(solution.calculate('3+2*2'))
print(solution.calculate(' 3/2 '))
print(solution.calculate(' 3+5 / 2 '))
