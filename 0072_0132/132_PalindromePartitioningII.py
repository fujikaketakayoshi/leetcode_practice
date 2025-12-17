class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        results = []
        i = 0
        while i < n:
            max_part = 0
            j = i + 1
            while j < n + 1:
                s_tmp = s[i:j]
                if s_tmp == s_tmp[::-1]:
                    max_part = max(max_part, j)
                j += 1
            if max_part != 0:
                results.append(max_part)
                i = max_part
            else:
                i += 1
        return len(results) - 1

solution = Solution()
print(solution.minCut("aab"))  # Output: 1
print(solution.minCut("a"))    # Output: 0
print(solution.minCut("abba")) # Output: 0
print(solution.minCut("racecar")) # Output: 0
print(solution.minCut("level")) # Output: 0
print(solution.minCut("aaabaa")) # Output: 1 => X 2が出る