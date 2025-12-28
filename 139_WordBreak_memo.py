class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        word_set = set(wordDict)
        n = len(s)
        memo = {}

        def dfs(start):
            if start == n:
                return True
            if start in memo:
                return memo[start]

            for i in range(start + 1, n + 1):
                if s[start:i] in word_set and dfs(i):
                    memo[start] = True
                    return True

            memo[start] = False
            return False

        return dfs(0)

solution = Solution()
print(solution.wordBreak("leetcode", ["leet", "code"]))  # True
print(solution.wordBreak("applepenapple", ["apple", "pen"]))  # True
print(solution.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))  # False 
