class PrefixSum2D:
    def __init__(self, grid):
        H = len(grid)
        W = len(grid[0])

        self.ps = [[0] * (W + 1) for _ in range(H + 1)]

        for y in range(H):
            for x in range(W):
                self.ps[y + 1][x + 1] = (
                    self.ps[y][x + 1]
                    + self.ps[y + 1][x]
                    - self.ps[y][x]
                    + grid[y][x]
                )
    def sum(self, top, left, bottom, right):
        return (
            self.ps[bottom + 1][right + 1]
            - self.ps[top][right + 1]
            - self.ps[bottom + 1][left]
            + self.ps[top][left]
        )


class Solution:
    def maxSumSubmatrix(self, matrix: list[list[int]], k: int) -> int:
        ps = PrefixSum2D(matrix)
        H = len(matrix)
        W = len(matrix[0])
        
        ans = None
        for t in range(H):
            for l in range(W):
                for b in range(t, H):
                    for r in range(l, W):
                        tmp = ps.sum(t,l,b,r)
                        if tmp <= k:
                            if ans is None:
                                ans = tmp
                            else:
                                ans = max(ans, tmp)
        
        return ans