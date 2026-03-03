class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        answer = [1] * n
        
        # ① 左からの累積積を入れる
        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]
        print(answer)

        # ② 右からの累積積を掛ける
        suffix = 1
        for i in range(n-1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]
        
        return answer
solution = Solution()
print(solution.productExceptSelf([1, 2, 3, 4]))  # 出力: [24, 12, 8, 6]
print(solution.productExceptSelf([-1, 1, 0, -3, 3]))  # 出力: [0, 0, 9, 0, 0]
