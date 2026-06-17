class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        N = len(coins)
        coins.sort(reverse=True)
        ans = []
        def dfs(i, rest, num):
            num += rest // coins[i]
            rest = rest % coins[i]
            if rest == 0:
                ans.append(num)
                return True
            for j in range(i + 1, N):
                if dfs(j, rest, num):
                    return

        for i in range(N):
            dfs(i, amount, 0)
        
        return min(ans) if len(ans) > 0 else -1

s = Solution()
print(s.coinChange([1, 2, 5], 11))
print(s.coinChange([233, 408, 101, 448, 235, 339, 40, 211], 7392))
