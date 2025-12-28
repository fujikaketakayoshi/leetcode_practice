class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        set_s = set(s)
        set_d = set()
        for word in wordDict:
            for w in word:
                set_d.add(w)
        for c in set_s:
            if c not in set_d:
                return False

        n = len(s)

        def dfs(start, path):
            if s == ''.join(path):
                return True

            for i in range(start + 1, n + 1):
                subs = s[start:i]
                if subs in wordDict:
                    path.append(subs)
                    if dfs(i, path):
                        return True
                    path.pop()
            return False

        return dfs(0, [])

solution = Solution()
print(solution.wordBreak("leetcode", ["leet", "code"]))  # True
print(solution.wordBreak("applepenapple", ["apple", "pen"]))  # True
print(solution.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))  # False