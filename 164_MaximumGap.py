class Solution:
    def maximumGap(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        
        nums.sort()
        
        max_diff = float('-INF')
        for i in range(n - 1):
            diff = nums[i + 1] - nums[i]
            max_diff = max(max_diff, diff)
        
        return max_diff

solution = Solution()
print(solution.maximumGap([3,6,9,1]))  # Output: 3
print(solution.maximumGap([10]))       # Output: 0
print(solution.maximumGap([1,10000000]))  # Output: 9999999
print(solution.maximumGap([1,1,1,1]))  # Output: 0
print(solution.maximumGap([1,3,5,7,9,11]))  # Output: 2
print(solution.maximumGap([1,2,4,8,16,32]))  # Output: 16