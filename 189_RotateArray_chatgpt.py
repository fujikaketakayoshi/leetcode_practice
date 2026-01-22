class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        k %= n

        def reverse(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)

        return nums
solution = Solution()
print(solution.rotate([1,2,3,4,5,6,7], 3))  # 出力: [5,6,7,1,2,3,4]
print(solution.rotate([-1,-100,3,99], 2))   # 出力: [3,99,-1,-100]
print(solution.rotate([1,2], 3))            # 出力: [2,1]
print(solution.rotate([1], 0))              # 出力: [1]
print(solution.rotate([1,2,3], 4))          # 出力: [3,1,2]
