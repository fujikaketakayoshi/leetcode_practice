class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:
        wds = set(wordDict)
        n = len(s)
        memo = {}

        def dfs(start):
            if start in memo:
                return memo[start]

            if start == n:
                return [""]  # 空文字が「終端」の合図

            res = []
            for i in range(start + 1, n + 1):
                word = s[start:i]
                if word in wds:
                    tails = dfs(i)
                    for tail in tails:
                        if tail:
                            res.append(word + " " + tail)
                        else:
                            res.append(word)

            memo[start] = res
            print(start, res)
            return res

        return dfs(0)


solution = Solution()
print(solution.wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"]))  
# Output: ["cats and dog", "cat sand dog"]
print(solution.wordBreak("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"]))  
# Output: ["pine apple pen apple", "pineapple pen apple", "pine applepen apple"]
print(solution.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))  
# Output: []    