class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        results = []

        def dfs(tmp):
            if len(tmp) == len(nums):
                results.append(tmp.copy())
                return
            for r_num in rest_nums:
                if not r_num in tmp:
                    tmp.append(r_num)
                    dfs(tmp)
                    tmp.pop()

        for num in nums:
            rest_nums = nums.copy()
            rest_nums.remove(num)
            dfs([num])

        
        return results

solution = Solution()
print(solution.permute([1,2,3]))
print(solution.permute([0,1]))