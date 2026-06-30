from itertools import accumulate

class Solution:
    def countRangeSum(self, nums, lower, upper):
        # 累積和
        prefix = [0] + list(accumulate(nums))

        def merge_sort(left, right):
            if right - left <= 1:
                return 0

            mid = (left + right) // 2

            # 左右を再帰的に処理
            ans = merge_sort(left, mid)
            ans += merge_sort(mid, right)

            # ----------------------------
            # 左側と右側をまたぐ区間を数える
            # ----------------------------
            l = r = mid

            for i in range(left, mid):

                while l < right and prefix[l] - prefix[i] < lower:
                    l += 1

                while r < right and prefix[r] - prefix[i] <= upper:
                    r += 1

                ans += r - l

            # ----------------------------
            # Merge Sort
            # ----------------------------
            tmp = []
            i = left
            j = mid

            while i < mid and j < right:
                if prefix[i] <= prefix[j]:
                    tmp.append(prefix[i])
                    i += 1
                else:
                    tmp.append(prefix[j])
                    j += 1

            tmp.extend(prefix[i:mid])
            tmp.extend(prefix[j:right])

            prefix[left:right] = tmp

            return ans

        return merge_sort(0, len(prefix))

s = Solution()
print(s.countRangeSum([-2, 5, -1], -2, 2))
