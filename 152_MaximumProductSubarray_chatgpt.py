class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        cur_max = nums[0]
        cur_min = nums[0]
        ans = nums[0]

        for x in nums[1:]:
            # x が負のとき max/min が入れ替わる
            if x < 0:
                cur_max, cur_min = cur_min, cur_max
            
            print(cur_max, cur_min)

            cur_max = max(x, cur_max * x)
            cur_min = min(x, cur_min * x)
            print(cur_max, cur_min)

            ans = max(ans, cur_max)

        return ans

solution = Solution()
print(solution.maxProduct([2, 3, -2, 4]))  # Output: 6
print(solution.maxProduct([-2, 0, -1]))    # Output: 0
print(solution.maxProduct([-2, 3, -4]))    # Output: 24
