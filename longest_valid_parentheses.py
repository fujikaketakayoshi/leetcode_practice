class Solution:
    def longestValidParentheses(self, s: str) -> int:
        queue = []
        i = 0
        while i < len(s):
            if s[i] == '(':
                queue.append('(')
            elif s[i] == ')':
                #print(len(queue) > 0 and '(' in queue)
                if len(queue) > 0 and '(' in queue:
                    open_indexes = [j for j, v in enumerate(queue) if v == '(']
                    open_last_index = open_indexes[-1]
                    queue[open_last_index] = 2
                else:
                    queue.append(')')
            i += 1
        print(queue)

        k = 0
        right = 0
        valid = 0
        longest = 0
        while k < len(queue):
            while k + right < len(queue) and queue[k + right] == 2:
                valid += 2
                print(k, right, valid)
                longest = max(longest, valid)
                right += 1
            valid = 0
            k += right + 1
            right = 0
        return longest

solution = Solution()
print(solution.longestValidParentheses("(()"))          # 2
print(solution.longestValidParentheses(")()())"))       # 4
print(solution.longestValidParentheses("()(()))))"))    # 8
