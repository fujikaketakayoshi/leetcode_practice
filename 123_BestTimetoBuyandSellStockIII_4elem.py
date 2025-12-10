class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy1 = buy2 = float('-inf')
        sell1 = sell2 = 0

        for p in prices:
            buy1  = max(buy1, -p)
            sell1 = max(sell1, buy1 + p)
            buy2  = max(buy2, sell1 - p)
            sell2 = max(sell2, buy2 + p)
            print(p, buy1, sell1, buy2, sell2)

        return sell2

Solution = Solution()
# print(Solution.maxProfit([3,3,5,0,0,3,1,4]))
print(Solution.maxProfit([1,2,3,4,5]))
# print(Solution.maxProfit([7,6,4,3,1]))
# print(Solution.maxProfit([1,2,4,2,5,7,2,4,9,0]))