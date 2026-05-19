class Solution:
    def maxCoins(self, nums: list[int]) -> int:
        n = len(nums)
        unused_index = set(range(n))

        ans = 0
        def dfs(total):
            nonlocal ans
            if not unused_index:
                ans = max(ans, total)
                return
            for i in list(unused_index):
                li = i - 1
                while li >= 0:
                    if li in unused_index:
                        break
                    li -= 1
                ri = i + 1
                while ri < n:
                    if ri in unused_index:
                        break
                    ri += 1
                left = 1 if li < 0 else nums[li]
                mid = nums[i]
                right = 1 if ri >= n else nums[ri]
                unused_index.remove(i)
                dfs(total + left * mid * right)
                unused_index.add(i)
        dfs(0)
        return ans

s = Solution()
print(s.maxCoins([3,1,5,8]))
print(s.maxCoins([1,5]))
