class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        used = [False] * 11
        results = set()

        def dfs(nums, cnt):
            if cnt == k:
                if sum(nums) == n:
                    results.add(tuple(sorted(nums)))
                return

            for i in range(1, 10):
                if used[i]:
                    continue
                used[i] = True
                dfs(nums + [i], cnt + 1)
                used[i] = False

        dfs([], 0)

        ans = []
        for i in results:
            ans.append(list(i))
        return ans