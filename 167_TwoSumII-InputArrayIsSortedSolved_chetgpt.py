class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            s = numbers[l] + numbers[r]
            if s == target:
                return [l + 1, r + 1]
            elif s < target:
                l += 1
            else:
                r -= 1


solution = Solution()
print(solution.twoSum([2,7,11,15], 9))        # Output: [1,2]
print(solution.twoSum([2,3,4], 6))          # Output: [1,3]
print(solution.twoSum([-1,0], -1))          # Output: [1,2]
print(solution.twoSum([5,25,75], 100))      # Output: [2,3]
