class Solution:
    def wiggleSort(self, nums: list[int]) -> None:
        arr = sorted(nums)
        n = len(nums)

        small = arr[:(n + 1) // 2][::-1]
        large = arr[(n + 1) // 2:][::-1]

        nums[::2] = small
        nums[1::2] = large
        return nums

s = Solution()
print(s.wiggleSort([1, 5, 1, 1, 6, 4]))
print(s.wiggleSort([1,4,3,4,1,2,1,3,1,3,2,3,3]))
print(s.wiggleSort([5,5,5,4,4,4,4]))
