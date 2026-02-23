class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        if ax2 < bx1 and ay2 < by1:
            area1 = abs(ax1 - ax2) * abs(ay1 - ay2)
            area2 = abs(bx1 - bx2) * abs(by1 - by2)
            return area1 + area2
        else:
            x1 = min(ax1, bx1)
            x2 = max(ax2, bx2)
            y1 = min(ay1, by1)
            y2 = max(ay2, by2)
            area = abs(x1 - x2) * abs(y1 - y2)
            c1_area = abs(x1 - max(ax1, bx1)) * abs(y1 - max(ay1, by1))
            c2_area = abs(x1 - min(ax1, bx1)) * abs(y2 - min(ay2, by2))
            c3_area = abs(x2 - max(ax2, bx2)) * abs(y1 - max(ay2, by2))
            c4_area = abs(x2 - min(ax2, bx2)) * abs(y2 - min(ay2, by2))
            print(area, c1_area, c2_area, c3_area, c4_area)
            return area - (c1_area + c2_area + c3_area + c4_area)

solution = Solution()
print(solution.computeArea(-3, 0, 3, 4, 0, -1, 9, 2))  # Output: 45
print(solution.computeArea(-2, -2, 2, 2, -2, -2, 2, 2))  # Output: 16
print(solution.computeArea(0, 0, 0, 0, -1, -1, 1, 1))  # Output: 1

