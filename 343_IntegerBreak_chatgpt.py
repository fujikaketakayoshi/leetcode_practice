from functools import cache

class Solution:
    def integerBreak(self, n: int) -> int:
        ans = 0

        @cache
        def dfs(nums):
            nonlocal ans

            nums = list(nums)
            ln = len(nums)

            if ln >= 2:
                product = 1
                for num in nums:
                    product *= num
                ans = max(ans, product)

            if ln == 2:
                return

            for i in range(ln):
                for j in range(i + 1, ln):
                    new_nums = []

                    for k in range(ln):
                        if k != i and k != j:
                            new_nums.append(nums[k])

                    new_nums.append(nums[i] + nums[j])
                    new_nums.sort()

                    dfs(tuple(new_nums))

        dfs(tuple([1] * n))
        return ans