class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        numsset = set(range(0, len(nums)))
        for num in nums:
            if num in numsset:
                numsset.remove(num)
        return list(numsset)[0] if len(numsset) == 1 else len(nums)

s = Solution()
print(s.missingNumber([3, 0, 1])) # 2
print(s.missingNumber([0, 1]))    # 2
print(s.missingNumber([9,6,4,2,3,5,7,0,1])) # 8
