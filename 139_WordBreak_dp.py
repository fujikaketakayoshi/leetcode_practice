class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        word_set = set(wordDict)
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break

        print(dp)
        return dp[n]

solution = Solution()
print(solution.wordBreak("leetcode", ["leet", "code"]))  # True
print(solution.wordBreak("applepenapple", ["apple", "pen"]))  # True
print(solution.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))  # False
