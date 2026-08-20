class Solution:
    def isSelfCrossing(self, distance: list[int]) -> bool:
        d = distance
        n = len(d)

        for i in range(3, n):
            # Case 1:
            # 現在の線分が3本前と交差
            if d[i] >= d[i - 2] and d[i - 1] <= d[i - 3]:
                return True

            # Case 2:
            # 現在の線分が4本前に重なる
            if i >= 4:
                if d[i - 1] == d[i - 3] and d[i] + d[i - 4] >= d[i - 2]:
                    return True

            # Case 3:
            # 現在の線分が5本前と交差
            if i >= 5:
                if (
                    d[i - 2] >= d[i - 4]
                    and d[i] + d[i - 4] >= d[i - 2]
                    and d[i - 1] <= d[i - 3]
                    and d[i - 1] + d[i - 5] >= d[i - 3]
                ):
                    return True

        return False