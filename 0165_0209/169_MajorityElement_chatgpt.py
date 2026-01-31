class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        candidate = None
        count = 0

        for n in nums:
            if count == 0:
                candidate = n
                count = 1
            elif n == candidate:
                count += 1
            else:
                count -= 1

        return candidate

solution = Solution()
print(solution.majorityElement([3,2,3]))  # 出力: 3
print(solution.majorityElement([2,2,1,1,1,2,2]))  # 出力: 2
print(solution.majorityElement([6,5,5]))  # 出力: 5