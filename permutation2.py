class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        results = set()
        check = [False] * len(nums)

        def dfs(path):
            if len(path) == len(nums):
                results.add(tuple(path))
                return

            for i in range(len(nums)):
                if check[i]:
                    continue
                path.append(nums[i])
                check[i] = True
                dfs(path)
                path.pop()
                check[i] = False

        dfs([])
        
        return list(map(list, results))


class Solution2:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        results = []
        used = [False] * len(nums)

        def dfs(path):
            if len(path) == len(nums):
                results.append(path[:])
                return

            for i in range(len(nums)):
                # すでに使った要素はスキップ
                if used[i]:
                    continue
                # 同じ階層で重複する値をスキップ
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue

                used[i] = True
                path.append(nums[i])
                dfs(path)
                path.pop()
                used[i] = False

        dfs([])
        return results

import timeit

print(timeit.timeit("Solution().permuteUnique([1,1,2,3,4,5,6])", globals=globals(), number=1000))
print(timeit.timeit("Solution2().permuteUnique([1,1,2,3,4,5,6])", globals=globals(), number=1000))
