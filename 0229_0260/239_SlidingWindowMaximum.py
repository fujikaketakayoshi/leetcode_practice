class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)
        result = []
        for l in range(n - k + 1):
            result.append(max(nums[l:l + k]))
        
        return result

solution = Solution()
print(solution.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))  # 出力: [3,3,5,5,6,7] 