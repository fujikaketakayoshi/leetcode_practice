class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        ln = len(nums)
        total = 1
        zero_cnt = 0
        for n in nums:
            if n == 0:
                zero_cnt += 1
            else:
                total *= n
        
        print(total)
        ans = [1] * ln
        for i in range(ln):
            if nums[i] != 0:
                if zero_cnt == 0:
                    ans[i] = total // nums[i]
                else:
                    ans[i] = 0
            elif nums[i] == 0:
                if zero_cnt == 1:
                    ans[i] = total
                elif zero_cnt > 1:
                    ans[i] = 0
        return ans

solution = Solution()
print(solution.productExceptSelf([1, 2, 3, 4]))  # 出力: [24, 12, 8, 6]
print(solution.productExceptSelf([-1, 1, 0, -3, 3]))  # 出力: [0, 0, 9, 0, 0]

