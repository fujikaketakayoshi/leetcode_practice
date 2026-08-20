from functools import cache
class Solution:
    def integerBreak(self, n: int) -> int:
        nnums = [1] * n
        ans = 0

        @cache
        def dfs(nums):
            nums = list(nums)
            print(nums)
            nonlocal ans
            
            ln = len(nums)
            if ln >= 2:
                p = 1
                for num in nums:
                    p *= num
                ans = max(ans, p)
            if ln == 2:
                return
            
            for i in range(ln):
                new_nums = nums[:]
                numi = new_nums.pop(i)
                newi_nums = new_nums[:]
                for j in range(i + 1, ln - 1):
                    numj = newi_nums.pop(j)
                    newi_nums.append(numi + numj)
                    dfs(tuple(newi_nums))
                    newi_nums = new_nums[:]

        dfs(tuple(nnums))
        return ans