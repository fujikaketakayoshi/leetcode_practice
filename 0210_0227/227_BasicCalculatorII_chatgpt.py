class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        prev_op = '+'
        
        for i, c in enumerate(s):
            if c.isdigit():
                num = num * 10 + int(c)
            
            if c in '+-*/' or i == len(s) - 1:
                if prev_op == '+':
                    stack.append(num)
                elif prev_op == '-':
                    stack.append(-num)
                elif prev_op == '*':
                    stack.append(stack.pop() * num)
                elif prev_op == '/':
                    stack.append(int(stack.pop() / num))  # truncate toward zero
                
                prev_op = c
                num = 0
        
        return sum(stack)

solution = Solution()
print(solution.calculate('3+2*2'))
print(solution.calculate(' 3/2 '))
print(solution.calculate(' 3+5 / 2 '))
