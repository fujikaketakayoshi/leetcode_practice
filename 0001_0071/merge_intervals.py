class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        results = []
        intervals.sort()
        if len(intervals) == 1:
            return intervals

        i = 0
        while i < len(intervals) - 1:
            if intervals[i][1] >= intervals[i + 1][0] or intervals[i][0] >= intervals[i + 1][1]:
                #print('merge', intervals[i], intervals[i + 1])
                tmp = sorted(intervals[i] + intervals[i + 1])
                results.append([tmp[0], tmp[3]])
                i += 1
            else:
                if i == len(intervals) - 2:
                    results.append(intervals[i])
                    results.append(intervals[i + 1])
                else:
                    results.append(intervals[i])
            i += 1
        return results

solution = Solution()
print(solution.merge([[1,3],[2,6],[8,10],[15,18]]))  # Expected: [[1,6],[8,10],[15,18]]
print(solution.merge([[1,4],[4,5]]))  # Expected: [[1,5
print(solution.merge([[1,4],[0,4]]))  # Expected: [[0,4]]
