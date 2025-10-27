class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = len(s)
        start = False if s[-1] == ' ' else True
        count = 0
        for i in range(n - 1, -1, -1):
            if start and s[i] != ' ':
                count += 1
            elif not start and s[i] != ' ':
                start = True
                count += 1
            elif start and s[i] == ' ':
                break
        return count

solution = Solution()
print(solution.lengthOfLastWord("Hello World"))  # Output: 5
print(solution.lengthOfLastWord("a"))