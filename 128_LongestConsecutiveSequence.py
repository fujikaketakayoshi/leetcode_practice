class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums.sort()
        n = len(nums)
        if n == 0:
            return 0
        prev = nums[0]
        max_cons = 1
        cons = 1
        
        for i in range(1, n):
            if prev + 1 == nums[i]:
                cons += 1
                max_cons = max(max_cons, cons)
                prev = nums[i]
            elif prev == nums[i]:
                continue
            else :
                cons = 1
                prev = nums[i]
        return max_cons

solution = Solution()
print(solution.longestConsecutive([100, 4, 200, 1, 3, 2]))  # Output: 4
print(solution.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))  # Output: 9
# Example usage:
print(solution.longestConsecutive([]))  # Output: 0
print(solution.longestConsecutive([1,2,0,1]))  # Output: 3
print(solution.longestConsecutive([9,1,4,7,3,-1,0,5,8,-1,6]))  # Output: 7