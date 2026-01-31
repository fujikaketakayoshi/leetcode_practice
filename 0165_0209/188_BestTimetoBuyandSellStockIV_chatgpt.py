class Solution:
    def maxProfit(self, k: int, prices: list[int]) -> int:
        n = len(prices)
        if n == 0:
            return 0

        # 無限取引ケース
        if k >= n // 2:
            profit = 0
            for i in range(1, n):
                if prices[i] > prices[i - 1]:
                    profit += prices[i] - prices[i - 1]
            return profit

        # dp[t][0 or 1]
        dp = [[float("-inf")] * 2 for _ in range(k + 1)]
        dp[0][0] = 0

        for price in prices:
            for t in range(1, k + 1)[::-1]:
                print(t, dp)
                dp[t][0] = max(dp[t][0], dp[t][1] + price)
                dp[t][1] = max(dp[t][1], dp[t - 1][0] - price)

        return max(dp[t][0] for t in range(k + 1))

solution = Solution()
#print(solution.maxProfit(2, [3,2,6,5,0,3]))  # 出力: 7
#print(solution.maxProfit(2, [2,4,1]))      # 出力: 2
#print(solution.maxProfit(0, [1,2,3,4,5]))  # 出力: 0
#print(solution.maxProfit(3, [1,2,3,4,5]))  # 出力: 4
#print(solution.maxProfit(1, [7,6,4,3,1]))  # 出力: 0
print(solution.maxProfit(3, [1,2,3,0,2,5,4,7]))  # 出力: 10
#print(solution.maxProfit(2, []))  # 出力: 0
#print(solution.maxProfit(100, [1,3,2,8,4,9]))  # 出力: 13
#print(solution.maxProfit(2, [3,3,5,0,0,3,1,4]))  # 出力: 6
#print(solution.maxProfit(2, [1,2,4,2,5,7,2,4,9,0]))  # 出力: 13
