class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = set()
        n = len(nums)

        for i in range(n):
            left, right = i+1, n-1
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if s == 0:
                    res.add((nums[i], nums[left], nums[right]))  # tupleで保存
                    left += 1
                    right -= 1
                elif s < 0:
                    left += 1
                else:
                    right -= 1

        return [list(triplet) for triplet in res]  # 最後にlistへ変換

solution = Solution()
print(solution.threeSum([-1, 0, 1, 2, -1, -4]))
print(solution.threeSum([0, 1, 1]))
print(solution.threeSum([0, 0, 0]))
print(solution.threeSum([3,0,-4,-1,1,2]))