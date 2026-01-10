class Solution:
    def maximumGap(self, nums: list[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0

        mn, mx = min(nums), max(nums)
        if mn == mx:
            return 0

        # バケット幅
        gap = (mx - mn + n - 2) // (n - 1)

        bucket_min = [float('inf')] * n
        bucket_max = [float('-inf')] * n
        used = [False] * n

        for x in nums:
            idx = (x - mn) // gap
            bucket_min[idx] = min(bucket_min[idx], x)
            bucket_max[idx] = max(bucket_max[idx], x)
            used[idx] = True

        prev_max = mn
        ans = 0

        for i in range(n):
            if not used[i]:
                continue
            ans = max(ans, bucket_min[i] - prev_max)
            prev_max = bucket_max[i]

        return ans


solution = Solution()
print(solution.maximumGap([3,6,9,1]))  # Output: 3
print(solution.maximumGap([10]))       # Output: 0
print(solution.maximumGap([1,10000000]))  # Output: 9999999
print(solution.maximumGap([1,1,1,1]))  # Output: 0
print(solution.maximumGap([1,3,5,7,9,11]))  # Output: 2
print(solution.maximumGap([1,2,4,8,16,32]))  # Output: 16