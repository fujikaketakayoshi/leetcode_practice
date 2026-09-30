class Solution:
    def largestDivisibleSubset(self, nums: list[int]) -> list[int]:
        n = len(nums)        
        max_ans = []
        for S in range(1 << n):
            subset = set()
            for i in range(n):
                if (S >> i) & 1:
                    subset.add(i)
            # print(S, subset)
            ok1 = True
            for i in range(n):
                ok2 = True
                for j in range(i + 1, n):
                    if i in subset or j in subset:
                        continue
                    if nums[i] % nums[j] != 0 and nums[j] % nums[i] != 0:
                        ok2 = False
                        break
                if not ok2:
                    ok1 = False
                    break
            if ok1:
                idxs = set(range(n))
                for idx in subset:
                    idxs.remove(idx)
                ans = []
                for i in idxs:
                    ans.append(nums[i])
                if len(ans) > len(max_ans):
                    max_ans = ans[:]
        return max_ans


