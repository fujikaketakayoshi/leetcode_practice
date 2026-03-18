class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        nums.sort()
        for i, v in enumerate(nums):
            if i != v:
                return i
        return len(nums)

s = Solution()
print(s.missingNumber([3, 0, 1])) # 2
print(s.missingNumber([0, 1]))    # 2
print(s.missingNumber([9,6,4,2,3,5,7,0,1])) # 8
