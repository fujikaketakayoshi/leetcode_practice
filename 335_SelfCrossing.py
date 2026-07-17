class Solution:
    def isSelfCrossing(self, distance: list[int]) -> bool:
        DIR = [(0, 1), (-1, 0), (0, -1), (1, 0)]
        n = len(distance)
        pre_x, pre_y = 0, 0
        ranges = []
        xys = set()
        for i in range(n):
            xys.add((pre_x,pre_y))
            d = i % 4
            dx = distance[i] * DIR[d][0]
            dy = distance[i] * DIR[d][1]
            x = dx + pre_x
            y = dy + pre_y
            ranges.append((pre_x, pre_y, x, y))
            pre_x = x
            pre_y = y
            if (x, y) in xys:
                return True
            if i >= 3:
                pr = ranges[i - 3]
                r = ranges[i]
                if i % 2 == 1:
                    if pr[1] <= r[1] <= pr[3] and r[0] <= pr[0] <= r[2]:
                        return True
                else:
                    if pr[0] <= r[0] <= pr[2] and r[1] <= pr[1] <= r[3]:
                        return True
        return False
        