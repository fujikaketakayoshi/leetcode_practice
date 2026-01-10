class Solution:
    def reverseWords(self, s: str) -> str:
        i = len(s) - 1
        ans = []

        while i >= 0:
            # スペースをスキップ
            while i >= 0 and s[i] == ' ':
                i -= 1
            if i < 0:
                break

            # 単語を集める
            stack = ''
            while i >= 0 and s[i] != ' ':
                stack = s[i] + stack
                i -= 1

            ans.append(stack)

        return ' '.join(ans)

solution = Solution()
print(solution.reverseWords("the sky is blue"))  # Output: "blue is sky the"
print(solution.reverseWords("  hello world  "))  # Output: "world hello"
print(solution.reverseWords("a good   example"))  # Output: "example good a"
print(solution.reverseWords("  Bob    Loves  Alice   "))  # Output: "Alice Loves Bob"
print(solution.reverseWords("Alice does not even like bob"))  # Output: "bob like even not does Alice"
