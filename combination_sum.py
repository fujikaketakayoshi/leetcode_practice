class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        results = []
        def dfs(sums):
            if sum(sums) == target:
                tmp_sums = sorted(sums.copy())
                if not tmp_sums in results:
                    results.append(tmp_sums)
                return
            if sum(sums) > target:
                return
            for i in candidates:
                if i > target:
                    break
                sums.append(i)
                dfs(sums)
                sums.pop()
        
        dfs([])
        return results

Solution = Solution()
# Solution.combinationSum([2,3,6,7], 7)
# Solution.combinationSum([2,3,5], 8)
# Solution.combinationSum([2], 1)
# Solution.combinationSum([1], 1)
# Solution.combinationSum([1], 2)
# Solution.combinationSum([1,2], 4)
# Solution.combinationSum([1,2,3], 4)
print(Solution.combinationSum([1,2,3,4,5,6,7,8,9,10], 10))