class Solution:
    def containsNearbyAlmostDuplicate(self, nums, indexDiff, valueDiff):
        if valueDiff < 0:
            return False

        bucket = {}
        w = valueDiff + 1

        for i, x in enumerate(nums):
            b = x // w

            if b in bucket:
                return True

            if b - 1 in bucket and abs(x - bucket[b - 1]) <= valueDiff:
                return True

            if b + 1 in bucket and abs(x - bucket[b + 1]) <= valueDiff:
                return True

            bucket[b] = x

            if i >= indexDiff:
                old_bucket = nums[i - indexDiff] // w
                del bucket[old_bucket]

        return False

solution = Solution()
print(solution.containsNearbyAlmostDuplicate([1,5,9,1,5,9], 2, 3))