class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = 0
        color = 0
        while i < n:
            if nums[i] == color:
                i += 1
                continue
            j = i + 1
            is_color = False
            while j < n:
                if nums[j] == color:
                    nums[i], nums[j] = nums[j], nums[i]
                    is_color = True
                    break
                j += 1
            if not is_color:
                color += 1
                i -= 1
            i += 1

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