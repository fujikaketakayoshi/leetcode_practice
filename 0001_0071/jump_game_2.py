from collections import deque
class Solution:
    def jump(self, nums: list[int]) -> int:
        n = len(nums)
        min_count = float('inf')
        queue = deque()
        queue.append((0, 0))
        while queue:
            i, count = queue.popleft()
            if i >= n - 1:
                min_count = min(min_count, count)
                continue
            for tmp_i in range(nums[i]):
                ni = tmp_i + i + 1
                queue.append((ni, count + 1))
        return min_count

solution = Solution()
print(solution.jump([2,3,1,1,4]))
print(solution.jump([2,3,0,1,4]))
print(solution.jump([5,6,4,4,6,9,4,4,7,4,4,8,2,6,8,1,5,9,6,5,2,7,9,7,9,6,9,4,1,6,8,8,4,4,2,0,3,8,5]))