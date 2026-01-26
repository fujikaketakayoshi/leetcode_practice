class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rx = self.find(x)
        ry = self.find(y)
        if rx == ry:
            return
        if self.rank[rx] < self.rank[ry]:
            self.parent[rx] = ry
        elif self.rank[rx] > self.rank[ry]:
            self.parent[ry] = rx
        else:
            self.parent[ry] = rx
            self.rank[rx] += 1


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        H = len(grid)
        W = len(grid[0])

        uf = UnionFind(H * W)

        land = set()

        def idx(y, x):
            return y * W + x

        # unionフェーズ
        for y in range(H):
            for x in range(W):
                if grid[y][x] == '1':
                    land.add(idx(y, x))
                    for dy, dx in [(1, 0), (0, 1)]:  # 下と右だけ
                        ny, nx = y + dy, x + dx
                        if 0 <= ny < H and 0 <= nx < W:
                            if grid[ny][nx] == '1':
                                uf.union(idx(y, x), idx(ny, nx))

        print(uf.parent, uf.rank)
        # rootの種類を数える
        roots = set()
        for v in land:
            roots.add(uf.find(v))
            print(uf.find(v))

        print(roots)
        return len(roots)

solution = Solution()
print(solution.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))  # 出力:  1
print(solution.numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]))  # 出力: 3
print(solution.numIslands([["1","0","1","1","0","1","1"]]))  # 出力: 3
print(solution.numIslands([["1","1","1"],["0","1","0"],["1","1","1"]]))  # 出力: 1