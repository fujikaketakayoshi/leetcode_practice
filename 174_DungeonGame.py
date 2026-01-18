class Solution:
    def calculateMinimumHP(self, dungeon: list[list[int]]) -> int:
        m = len(dungeon)
        n = len(dungeon[0])
        
        results = []

        def dfs(y, x, life, min_life):
            min_life = min(min_life, life)
            if y == m - 1 and x == n - 1:
                life += dungeon[y][x]
                results.append((life, min_life))

            if y < m - 1:
                dfs(y + 1, x, life + dungeon[y][x], min_life)
            if x < n - 1:
                dfs(y, x + 1, life + dungeon[y][x], min_life)

        dfs(0, 0, 0, float('INF'))
        print(results)
        min_lives = sorted(results, key=lambda x: min(x[0], x[1]), reverse=True)[0]
        min_life = min(min_lives[0], min_lives[1])
        if min_life > 0:
            ans = 1
        else:
            ans = abs(min_life) + 1
        return ans

solution = Solution()
print(solution.calculateMinimumHP([[-2,-3,3],[-5,-10,1],[10,30,-5]]))  # 出力: 7
print(solution.calculateMinimumHP([[0,-3]]))  # 出力: 4
print(solution.calculateMinimumHP([[100]]))  # 出力: 1 