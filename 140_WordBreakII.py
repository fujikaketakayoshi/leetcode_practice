class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:
        n = len(s)
        wds = set(wordDict)
        results = []

        def dfs(start, path):
            if start == n:
                results.append(path.copy())
                return
            
            for i in range(start + 1, n + 1):
                word = s[start:i]
                if word in wds:
                    path.append(word)
                    dfs(i, path)
                    path.pop()
        dfs(0, [])
        return [' '.join(r) for r in results]
            

solution = Solution()
print(solution.wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"]))  
# Output: ["cats and dog", "cat sand dog"]
print(solution.wordBreak("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"]))  
# Output: ["pine apple pen apple", "pineapple pen apple", "pine applepen apple"]
print(solution.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))  
# Output: []    