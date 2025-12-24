class Solution:
    def candy(self, ratings: list[int]) -> int:
        n = len(ratings)
        left = [1] * n
        right = [1] * n

        # 左 → 右
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                left[i] = left[i - 1] + 1

        # 右 → 左
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                right[i] = right[i + 1] + 1
        # print(left, right)
        # 両方の制約を満たす
        return sum(max(left[i], right[i]) for i in range(n))

solution = Solution()
print(solution.candy([1,0,2]))  # Expected output: 5
print(solution.candy([1,2,2]))  # Expected output: 4
print(solution.candy([1,3,4,5,2]))  # Expected output: 11
print(solution.candy([1,2,87,87,87,2,1])) # Expected output: 13