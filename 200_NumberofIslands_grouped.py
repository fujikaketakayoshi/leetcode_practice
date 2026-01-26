from collections import deque
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        H = len(grid)
        W = len(grid[0])

        # 0 = 未割り当て、1以上 = 島ID
        grouped = [[0] * W for _ in range(H)]

        # 上下左右
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def bfs(sy, sx, island_id):
            queue = deque([(sy, sx)])
            grouped[sy][sx] = island_id

            while queue:
                y, x = queue.popleft()
                for dy, dx in dirs:
                    ny = y + dy
                    nx = x + dx
                    if 0 <= ny < H and 0 <= nx < W:
                        if grid[ny][nx] == '1' and grouped[ny][nx] == 0:
                            grouped[ny][nx] = island_id
                            queue.append((ny, nx))

        island_id = 0

        # 全探索
        for y in range(H):
            for x in range(W):
                if grid[y][x] == '1' and grouped[y][x] == 0:
                    island_id += 1
                    bfs(y, x, island_id)

        return island_id

solution = Solution()
print(solution.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))  # 出力:  1
print(solution.numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]))  # 出力: 3
print(solution.numIslands([["1","0","1","1","0","1","1"]]))  # 出力: 3
print(solution.numIslands([["1","1","1"],["0","1","0"],["1","1","1"]]))  # 出力: 1