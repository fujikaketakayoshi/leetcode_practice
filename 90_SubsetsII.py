class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        cache = [False] * len(nums)
        results = set()

        def dfs(start, path, prev):
            results.add(tuple(sorted(path)))

            for i in range(start, len(nums)):
                if cache[i]:
                    continue
                cache[i] = True
                path.append(nums[i])
                prev = i
                dfs(start + 1, path, prev)
                cache[i] = False
                path.pop()
        
        dfs(0, [], -1)

        results2 = []
        for r in results:
            results2.append(list(r))
        return results2

Solution = Solution()
print(Solution.subsetsWithDup([1,2,2]))  # [[],[1],[1,2],[1,2,2],[2],[2,2]]
print(Solution.subsetsWithDup([0]))      # [[],[0]]
print(Solution.subsetsWithDup([4,4,4,1,4]))  # [[],[1],[1,4],[1,4,4],[1,4,4,4],[4],[4,4],[4,4,4],[4,4,4,4]]
print(Solution.subsetsWithDup([1,2,3]))  # [[],[1],[1,2],[1,2,3],[1,3],[2],[2,3],[3]]
print(Solution.subsetsWithDup([1,1,1]))  # [[],[1],[1,1],[1,1,1]]
print(Solution.subsetsWithDup([]))       # [[]]  