class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        # 1回目：候補を探す
        cand1 = cand2 = None
        count1 = count2 = 0

        for num in nums:
            if cand1 == num:
                count1 += 1
            elif cand2 == num:
                count2 += 1
            elif count1 == 0:
                cand1 = num
                count1 = 1
            elif count2 == 0:
                cand2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1

        # 2回目：本当に n/3 超えか確認
        result = []
        for cand in (cand1, cand2):
            if cand is not None and nums.count(cand) > len(nums) // 3:
                result.append(cand)

        return result

solution = Solution()
print(solution.majorityElement([3, 2, 3]))  # Output: [3]
print(solution.majorityElement([1]))  # Output: [1]
print(solution.majorityElement([1, 2]))  # Output: [1, 2]
