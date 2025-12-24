class Solution:
    def candy(self, ratings: list[int]) -> int:
        n = len(ratings)
        dp = [1] * n

        for i in range(n - 1):
            if i == 0:
                if ratings[i] > ratings[i + 1]:
                    dp[i] = dp[i + 1] + 1
                if ratings[i] < ratings[i + 1]:
                    dp[i + 1] = dp[i] + 1                
            elif 0 < i < n - 1:
                if ratings[i] > ratings[i + 1]:
                    dp[i] = dp[i + 1] + 1
                if ratings[i] < ratings[i + 1]:
                    dp[i + 1] = dp[i] + 1
        print(dp)
        return sum(dp)

solution = Solution()
print(solution.candy([1,0,2]))  # Expected output: 5
print(solution.candy([1,2,2]))  # Expected output: 4
print(solution.candy([1,3,4,5,2]))  # Expected output: 11,  x => 9
