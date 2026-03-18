class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        total = n * (n + 1) // 2
        print(total)
        return total - sum(nums)

s = Solution()
print(s.missingNumber([3, 0, 1])) # 2
print(s.missingNumber([0, 1]))    # 2
print(s.missingNumber([9,6,4,2,3,5,7,0,1])) # 8
