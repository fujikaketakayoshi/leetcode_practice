class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]  # 基準点
        longest = 0
        
        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)  # '(' のインデックスをpush
            else:
                stack.pop()      # ')' に対応する '(' をpop
                if not stack:
                    # スタック空なら基準点を追加
                    stack.append(i)
                else:
                    # 有効長 = 現在位置 - スタック末尾
                    longest = max(longest, i - stack[-1])
                    print(i, stack, longest)
        
        return longest

solution = Solution()
#print(solution.longestValidParentheses("(()"))          # 2
#print(solution.longestValidParentheses(")()())"))       # 4
print(solution.longestValidParentheses("())((()))))"))    
