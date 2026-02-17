class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        ly = len(matrix)
        lx = len(matrix[0])
        
        dp = [[0] * lx for _ in range(ly)]
        max_side = 0
        
        for y in range(ly):
            for x in range(lx):
                if matrix[y][x] == '1':
                    if y == 0 or x == 0:
                        dp[y][x] = 1
                    else:
                        dp[y][x] = min(
                            dp[y-1][x],
                            dp[y][x-1],
                            dp[y-1][x-1]
                        ) + 1
                    
                    max_side = max(max_side, dp[y][x])
        
        return max_side ** 2
