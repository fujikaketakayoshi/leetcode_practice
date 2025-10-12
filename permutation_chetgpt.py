class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        results = []
        used = [False] * len(nums)  # 各要素が使用済みかどうか

        def dfs(path):
            if len(path) == len(nums):
                results.append(path.copy())
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                used[i] = True
                path.append(nums[i])
                dfs(path)
                path.pop()
                used[i] = False  # 戻す（バックトラック）

        dfs([])
        return results

solution = Solution()
print(solution.permute([1,2,3]))
print(solution.permute([0,1]))
