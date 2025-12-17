class Solution:
    def partition(self, s: str):
        res = []
        n = len(s)

        def dfs(start, path):
            if start == n:
                res.append(path[:])
                return

            for end in range(start + 1, n + 1):
                substr = s[start:end]
                if substr == substr[::-1]:
                    path.append(substr)
                    dfs(end, path)
                    path.pop()

        dfs(0, [])
        return res

solution = Solution()
print(solution.partition("aab"))  # Output: [["a","a","b"],["aa"]]
print(solution.partition("a"))    # Output: [["a"]]
print(solution.partition("abba")) # Output: [["a","b","b","a"],["a","bb","a"],["abba"]]
print(solution.partition("racecar")) # Output: [["r","a","c","e","c","a","r"], ["r","a","cec","a","r"], ["r","aceca","r"], ["racecar"]]
print(solution.partition("level")) # Output: [["l","e","v","e","l"], ["l","eve","l"], ["level"]]