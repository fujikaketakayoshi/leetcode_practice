from collections import deque
class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        H = len(grid)
        W = len(grid[0])
        visited = [[False] * W for _ in range(H)]
        cnt = 0
        dy = [-1, 0, 1, 0]
        dx = [0, 1, 0, -1]

        def bfs(y, x):
            if visited[y][x] or grid[y][x] == '0':
                return 0
            visited[y][x] = True
            stack = deque()
            stack.append((y, x))
            while stack:
                r, c = stack.pop()
                for d in range(4):
                    ny = r + dy[d]
                    nx = c + dx[d]
                    if ny < 0 or nx < 0 or ny > H - 1 or nx > W - 1:
                        continue
                    if visited[ny][nx] or grid[ny][nx] == '0':
                        continue
                    visited[ny][nx] = True
                    stack.append((ny, nx))        
            return 1

        for y in range(H):
            for x in range(W):
                cnt +=bfs(y, x)
        return cnt

solution = Solution()
print(solution.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))  # 出力:  1
print(solution.numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]))  # 出力: 3
print(solution.numIslands([["1","0","1","1","0","1","1"]]))  # 出力: 3
print(solution.numIslands([["1","1","1"],["0","1","0"],["1","1","1"]]))  # 出力: 1