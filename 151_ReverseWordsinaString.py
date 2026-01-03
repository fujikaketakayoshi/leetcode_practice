class Solution:
    def reverseWords(self, s: str) -> str:
        #return ' '.join(s.split()[::-1])
        n = len(s)
        i = n - 1
        prev = ''
        ans = ''
        while i >= 0:
            stack = ''
            while s[i:i + 1] !=' ' and i >= 0:
                stack = s[i:i + 1] + stack
                prev = s[i:i + 1]
                i -= 1
            if prev != ' ':
                ans = ans + (' ' if ans != '' else '') + stack
                stack = ''
                prev = ' '
            i -= 1
        return ans

solution = Solution()
print(solution.reverseWords("the sky is blue"))  # Output: "blue is sky the"
print(solution.reverseWords("  hello world  "))  # Output: "world hello"
print(solution.reverseWords("a good   example"))  # Output: "example good a"
print(solution.reverseWords("  Bob    Loves  Alice   "))  # Output: "Alice Loves Bob"
print(solution.reverseWords("Alice does not even like bob"))  # Output: "bob like even not does Alice"
