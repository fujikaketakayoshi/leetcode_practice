class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        insert_pos = 0  # 次に非ゼロを置く位置

        # 非ゼロを前に詰める
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[insert_pos] = nums[i]
                insert_pos += 1

        # 残りを0で埋める
        for i in range(insert_pos, len(nums)):
            nums[i] = 0
        print(nums)

s = Solution()
print(s.moveZeroes([0,1,0,3,12]))
print(s.moveZeroes([0,0,1]))