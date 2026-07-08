class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        pres = preorder.split(',')
        stack = []
        for p in pres:
            stack.append(p)
            while (len(stack) >= 3
                and stack[-3] != '#'
                and stack[-2] == '#'
                and stack[-1] == '#'):
                stack.pop()
                stack.pop()
                stack.pop()
                stack.append('#')
        return len(stack) == 1 and stack[0] == '#'
