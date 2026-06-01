class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last = {c:i for i,c in enumerate(s)}

        stack = []
        used = set()

        for i, c in enumerate(s):
            
            if c in used:
                continue

            while (
                stack and
                stack[-1] > c and
                last[stack[-1]] > i
            ):
                used.remove(stack.pop())

            stack.append(c)
            used.add(c)

        return ''.join(stack)

s = Solution()
print(s.removeDuplicateLetters("bcabc"))
print(s.removeDuplicateLetters("aaabbb"))