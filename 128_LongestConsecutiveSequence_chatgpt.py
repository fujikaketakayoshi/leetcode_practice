class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        num_set = set(nums)
        max_len = 0

        for x in num_set:
            # x-1 がない → 連続列の「始点」
            if x - 1 not in num_set:
                cur = x
                length = 1

                while cur + 1 in num_set:
                    cur += 1
                    length += 1

                max_len = max(max_len, length)

        return max_len


solution = Solution()
print(solution.longestConsecutive([100, 4, 200, 1, 3, 2]))  # Output: 4
print(solution.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))  # Output: 9
# Example usage:
print(solution.longestConsecutive([]))  # Output: 0
print(solution.longestConsecutive([1,2,0,1]))  # Output: 3
print(solution.longestConsecutive([9,1,4,7,3,-1,0,5,8,-1,6]))  # Output: 7