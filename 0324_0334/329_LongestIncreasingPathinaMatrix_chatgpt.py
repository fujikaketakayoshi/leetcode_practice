from functools import cache
class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        H = len(matrix)
        W = len(matrix[0])
        DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        
        @cache
        def dfs(i, j):
            path = 1
            for dy, dx in DIRS:
                ny = dy + i
                nx = dx + j
                if not (0 <= ny < H and 0 <= nx < W):
                    continue
                if matrix[ny][nx] <= matrix[i][j]:
                    continue
                path = max(path, dfs(ny, nx) + 1)
            return path

        max_p = 0
        for h in range(H):
            for w in range(W):
                ans = dfs(h, w)
                max_p = max(max_p, ans)

        return max_p

s = Solution()
print(s.longestIncreasingPath([[9,9,4],[6,6,8],[2,1,1]]))
print(s.longestIncreasingPath([[3,4,5],[3,2,6],[2,2,1]]))
print(s.longestIncreasingPath([[1]]))
