class Solution:
    def climbStairs(self, n: int) -> int:
        count = 0
        def dfs(pos):
            nonlocal count
            if pos == n:
                count += 1
                return
            elif pos > n:
                return
            dfs(pos + 1)
            dfs(pos + 2)

        dfs(0)
        return count

solution = Solution()
for i in range(1, 46):
    print(f"n={i}, ways={solution.climbStairs(i)}")
