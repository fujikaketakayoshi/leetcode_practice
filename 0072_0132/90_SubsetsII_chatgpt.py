class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []

        def dfs(start, path):
            res.append(path[:])

            for i in range(start, len(nums)):
                # ★同じ階層(start)で使う数字が同じならスキップ
                if i > start and nums[i] == nums[i - 1]:
                    continue

                path.append(nums[i])
                dfs(i + 1, path)
                path.pop()

        dfs(0, [])
        return res

Solution = Solution()
print(Solution.subsetsWithDup([1,2,2]))  # [[],[1],[1,2],[1,2,2],[2],[2,2]]
print(Solution.subsetsWithDup([0]))      # [[],[0]]
print(Solution.subsetsWithDup([4,4,4,1,4]))  # [[],[1],[1,4],[1,4,4],[1,4,4,4],[4],[4,4],[4,4,4],[4,4,4,4]]
print(Solution.subsetsWithDup([1,2,3]))  # [[],[1],[1,2],[1,2,3],[1,3],[2],[2,3],[3]]
print(Solution.subsetsWithDup([1,1,1]))  # [[],[1],[1,1],[1,1,1]]
print(Solution.subsetsWithDup([]))       # [[]] 