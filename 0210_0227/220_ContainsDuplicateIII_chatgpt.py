from bisect import bisect_left, insort

class Solution:
    def containsNearbyAlmostDuplicate(self, nums, indexDiff, valueDiff):
        window = []

        for i, x in enumerate(nums):
            # x - valueDiff 以上の最初の位置
            pos = bisect_left(window, x - valueDiff)

            print(pos < len(window))
            # その位置が条件を満たすか確認
            if pos < len(window) and abs(window[pos] - x) <= valueDiff:
                return True

            # 追加
            insort(window, x)

            # indexDiff を超えたら削除
            if i >= indexDiff:
                window.remove(nums[i - indexDiff])

        return False

solution = Solution()
print(solution.containsNearbyAlmostDuplicate([1,5,9,1,5,9], 2, 3))