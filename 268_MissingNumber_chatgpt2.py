class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        res = len(nums)
        for i, num in enumerate(nums):
            res ^= i ^ num
            print(i, num, i ^ num, res)
        return res

s = Solution()
print(s.missingNumber([3, 0, 1])) # 2
print(s.missingNumber([0, 1]))    # 2
print(s.missingNumber([9,6,4,2,3,5,7,0,1])) # 8
