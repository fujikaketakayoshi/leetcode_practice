class Solution:
    def sortColors(self, nums: list[int]) -> None:
        n = len(nums)
        color = 0
        i = 0
        j = 0  # 次のcolor探索の開始位置を保持

        while color <= 2 and i < n:
            if nums[i] == color:
                i += 1
            else:
                # jをi以降から動かして、次のcolorを探す
                while j < n and nums[j] != color:
                    j += 1
                if j == n:
                    # もうこのcolorは残ってないので次の色へ
                    color += 1
                    j = i  # 探索開始位置をリセット
                else:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                    j += 1
        print(nums)

solution = Solution()
nums = [2,0,2,1,1,0]
solution.sortColors(nums)  # 出力: [0,0,1,1,2,2]
nums = [2,0,1]
solution.sortColors(nums)  # 出力: [0,1,2]
nums = [0]
solution.sortColors(nums)  # 出力: [0]
nums = [1]
solution.sortColors(nums)  # 出力: [1]
nums = [1,2,0]
solution.sortColors(nums)  # 出力: [0,1,2]
