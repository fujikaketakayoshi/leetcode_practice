class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        diffs = []
        for i in range(1, n):
            diffs.append(prices[i] - prices[i - 1])
        
        nd = n - 1
        last_plus = 0
        profits = []
        for i in range(nd):
            if i == nd - 1:
                if diffs[i] > 0 and last_plus == 0:
                    profits.append(diffs[i])
                elif diffs[i] > 0 and last_plus > 0:
                    profits.append(last_plus + diffs[i])
                elif diffs[i] <= 0 and last_plus > 0:
                    profits.append(last_plus)
            elif diffs[i] > 0 and last_plus == 0:
                last_plus = diffs[i]
            elif diffs[i] > 0 and last_plus > 0:
                last_plus += diffs[i]
            elif diffs[i] < 0 and last_plus > 0:
                profits.append(last_plus)
                last_plus = 0
        print(diffs)
        print(profits)
        profits.sort(reverse=True)
        return sum(profits[0:2])

Solution = Solution()
print(Solution.maxProfit([3,3,5,0,0,3,1,4]))
print(Solution.maxProfit([1,2,3,4,5]))
print(Solution.maxProfit([7,6,4,3,1]))
print(Solution.maxProfit([1,2,4,2,5,7,2,4,9,0]))