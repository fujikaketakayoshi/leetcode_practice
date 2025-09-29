class Solution:
    def longestValidParentheses(self, s: str) -> int:
        queue = []
        open_stack = []  # '(' の位置を管理する専用スタック

        for i, ch in enumerate(s):
            if ch == '(':
                queue.append('(')
                open_stack.append(len(queue) - 1)  # queue 上のインデックスをpush
            else:  # ')'
                if open_stack:
                    open_last_index = open_stack.pop()
                    queue[open_last_index] = 2  # マッチ済みにする
                    queue.append(2)             # ')' 側もマーク
                else:
                    queue.append(')')

        # 有効部分の長さをスキャン
        k = 0
        longest = 0
        while k < len(queue):
            if queue[k] == 2:
                length = 0
                while k < len(queue) and queue[k] == 2:
                    length += 1
                    k += 1
                longest = max(longest, length)
            else:
                k += 1

        return longest

Solution = Solution()
print(Solution.longestValidParentheses("(()"))          # 2
print(Solution.longestValidParentheses(")()())"))       # 4
print(Solution.longestValidParentheses("()(()))))"))    # 8
