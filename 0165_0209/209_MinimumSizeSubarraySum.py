class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        n = len(nums)
        l, r = 0, 0
        total = 0
        min_length = float('INF')
        while l < n:
            total = nums[l]
            if total >= target:
                return 1
                # min_length = min(min_length, 1)
            else:
                r = l + 1
                while r < n:
                    total += nums[r]
                    if total >= target:
                        min_length = min(min_length, r - l + 1)
                        break
                    else:
                        r += 1
            l += 1
        return 0 if min_length == float('INF') else min_length

solution = Solution()
print(solution.minSubArrayLen(7, [2,3,1,2,4,3]))  # 2
print(solution.minSubArrayLen(4, [1,4,4]))  # 1
print(solution.minSubArrayLen(11, [1,1,1,1,1,1,1,1]))  # 0 