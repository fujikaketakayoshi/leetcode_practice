import heapq
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: list[int], indexDiff: int, valueDiff: int) -> bool:
        n = len(nums)
        l, r = 0, 1
        hq_max = []
        hq_min = []
        while l < n and r < n:
            heapq.heappush(hq_max, (-nums[r], r))
            heapq.heappush(hq_min, (nums[r], r))
            if abs(l - r) > indexDiff:
                l += 1
                if l - 1 == -hq_max[0][1]:
                    heapq.heappop(hq_max)
                if l - 1 == hq_min[0][1]:
                    heapq.heappop(hq_min)
            print(l, r, nums[l:r + 1], hq_max, hq_min)
            if hq_max[0][1] != l:
                if abs(nums[l] - -hq_max[0][0]) <= valueDiff:
                    return True
            elif len(hq_max) > 1:
                tmp_max = -hq_max[1][0]
                if abs(nums[l] - tmp_max) <= valueDiff:
                    return True
            if hq_min[0][1] != l:
                if abs(nums[l] - hq_min[0][0]) <= valueDiff:
                    return True
            elif len(hq_min) > 1:
                tmp_min = hq_min[1][0]
                if abs(nums[l] - tmp_min) <= valueDiff:
                    return True
            r += 1
            if r == n:
                r -= 1
                l += 1
                if l - 1 == -hq_max[0][1]:
                    heapq.heappop(hq_max)
                if l - 1 == hq_min[0][1]:
                    heapq.heappop(hq_min)

        return False
