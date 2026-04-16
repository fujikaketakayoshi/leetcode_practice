from collections import deque

class Solution:
    def removeInvalidParentheses(self, s: str):
        def is_valid(string):
            cnt = 0
            for ch in string:
                if ch == '(':
                    cnt += 1
                elif ch == ')':
                    cnt -= 1
                    if cnt < 0:
                        return False
            return cnt == 0

        q = deque([s])
        visited = {s}
        ans = []
        found = False

        while q:
            cur = q.popleft()

            if is_valid(cur):
                ans.append(cur)
                found = True

            if found:
                continue

            for i in range(len(cur)):
                if cur[i] not in '()':
                    continue

                nxt = cur[:i] + cur[i+1:]

                if nxt not in visited:
                    visited.add(nxt)
                    q.append(nxt)

        return ans
s = Solution()
print(s.removeInvalidParentheses("()())()"))
print(s.removeInvalidParentheses("(a)())()"))
print(s.removeInvalidParentheses(")("))