class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        if not intervals:
            return []

        # 1. start でソート
        intervals.sort(key=lambda x: x[0])

        merged = [intervals[0]]

        # 2. 1パスでマージ
        for current in intervals[1:]:
            last = merged[-1]

            # 重なっている場合 → 終端をmaxで更新
            if current[0] <= last[1]:
                last[1] = max(last[1], current[1])
            else:
                # 重なっていなければ新しい区間を追加
                merged.append(current)

        return merged
solution = Solution()
print(solution.merge([[1,3],[2,6],[8,10],[15,18]]))  # Expected: [[1,6],[8,10],[15,18]]
print(solution.merge([[1,4],[4,5]]))  # Expected: [[1,5
print(solution.merge([[1,4],[0,4]]))  # Expected: [[0,4]]
