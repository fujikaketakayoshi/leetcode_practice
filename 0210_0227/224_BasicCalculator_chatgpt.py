class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        result = 0
        num = 0
        sign = 1  # +1 or -1
        
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            
            elif c == '+':
                result += sign * num
                num = 0
                sign = 1
            
            elif c == '-':
                result += sign * num
                num = 0
                sign = -1
            
            elif c == '(':
                # 現在の状態を保存
                stack.append(result)
                stack.append(sign)
                
                # リセット
                result = 0
                sign = 1
            
            elif c == ')':
                result += sign * num
                num = 0
                
                # 直前の符号をかける
                result *= stack.pop()
                
                # 直前のresultに足す
                result += stack.pop()
        
        return result + sign * num

solution = Solution()
print(solution.calculate("1 + 1"))  # Output: 2
print(solution.calculate(" 2-1 + 2 "))  # Output: 3
print(solution.calculate("(1+(4+5+2)-3)+(6+8)"))  # Output: 23
