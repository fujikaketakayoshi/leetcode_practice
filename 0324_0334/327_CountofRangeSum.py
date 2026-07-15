class Solution:
    def countRangeSum(self, nums: list[int], lower: int, upper: int) -> int:
        n = len(nums)
        ans = []
        for r in range(1, n + 1):
            for i in range(n):
                if i > n - r:
                    break
                r_sum = sum(nums[i:i + r])
                print(r_sum)
                if lower <= r_sum <= upper:
                    ans.append(r_sum)
        return len(ans)