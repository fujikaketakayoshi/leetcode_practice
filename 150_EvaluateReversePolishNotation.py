class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        i = 2
        while i < len(tokens):
            result = None
            if tokens[i] == '+':
                result = int(tokens[i - 2]) + int(tokens[i - 1])
            elif tokens[i] == '-':
                result = int(tokens[i - 2]) - int(tokens[i - 1])
            elif tokens[i] == '*':
                result = int(tokens[i - 2]) * int(tokens[i - 1])
            elif tokens[i] == '/':
                result = int(int(tokens[i - 2]) / int(tokens[i - 1]))
            
            if result is not None:
                tokens.pop(i - 2)
                tokens.pop(i - 2)
                tokens.pop(i - 2)
                tokens.insert(i - 2, result)
                i -= 3
            i += 1
        return int(tokens[0])

solution = Solution()
print(solution.evalRPN(["2","1","+","3","*"]))  # Output: 9
print(solution.evalRPN(["4","13","5","/","+"]))  # Output: 6
print(solution.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))  # Output: 22   
print(solution.evalRPN(["3","-4","+"]))  # Output: -1