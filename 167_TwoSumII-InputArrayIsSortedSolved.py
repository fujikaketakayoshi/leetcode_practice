class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        n = len(numbers)
        for i in range(n - 1, -1, -1):
            diff = target - numbers[i]
            right = i
            left = 0
            while left < right:
                mid = (left + right) // 2
                if numbers[mid] == diff:
                    return [mid + 1, i + 1]
                elif diff < numbers[mid]:
                    right = mid
                elif numbers[mid] < diff:
                    left = mid + 1

solution = Solution()
print(solution.twoSum([2,7,11,15], 9))        # Output: [1,2]
print(solution.twoSum([2,3,4], 6))          # Output: [1,3]
print(solution.twoSum([-1,0], -1))          # Output: [1,2]
print(solution.twoSum([5,25,75], 100))      # Output: [2,3]
