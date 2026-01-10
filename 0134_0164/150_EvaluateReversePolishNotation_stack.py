class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []

        for t in tokens:
            if t in "+-*/":
                b = stack.pop()
                a = stack.pop()

                if t == "+":
                    stack.append(a + b)
                elif t == "-":
                    stack.append(a - b)
                elif t == "*":
                    stack.append(a * b)
                else:  # "/"
                    stack.append(int(a / b))  # 0方向に切り捨て
            else:
                stack.append(int(t))

        return stack[0]


solution = Solution()
print(solution.evalRPN(["2","1","+","3","*"]))  # Output: 9
print(solution.evalRPN(["4","13","5","/","+"]))  # Output: 6
print(solution.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))  # Output: 22   
print(solution.evalRPN(["3","-4","+"]))  # Output: -1