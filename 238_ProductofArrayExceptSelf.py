class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        ln = len(nums)
        ans = [1] * ln
        for i in range(ln):
            for j in range(ln):
                if j == i:
                    continue
                ans[i] *= nums[j]
        return ans

solution = Solution()
print(solution.productExceptSelf([1, 2, 3, 4]))  # 出力: [24, 12, 8, 6]
