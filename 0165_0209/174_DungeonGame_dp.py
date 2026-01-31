class Solution:
    def calculateMinimumHP(self, dungeon):
        m, n = len(dungeon), len(dungeon[0])
        
        INF = 10**15
        dp = [[INF] * (n + 1) for _ in range(m + 1)]
        
        # ゴールの右と下を1にしておく（番兵）
        dp[m][n - 1] = 1
        dp[m - 1][n] = 1
        
        for y in range(m - 1, -1, -1):
            for x in range(n - 1, -1, -1):
                need = min(dp[y + 1][x], dp[y][x + 1])
                dp[y][x] = max(1, need - dungeon[y][x])
        
        return dp[0][0]

solution = Solution()
print(solution.calculateMinimumHP([[-2,-3,3],[-5,-10,1],[10,30,-5]]))  # 出力: 7
print(solution.calculateMinimumHP([[0,-3]]))  # 出力: 4
print(solution.calculateMinimumHP([[100]]))  # 出力: 1 
