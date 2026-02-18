class Solution:
    def computeArea(
        self,
        ax1: int, ay1: int, ax2: int, ay2: int,
        bx1: int, by1: int, bx2: int, by2: int
    ) -> int:

        # 各長方形の面積
        areaA = (ax2 - ax1) * (ay2 - ay1)
        areaB = (bx2 - bx1) * (by2 - by1)

        # 重なり部分
        overlap_w = max(0, min(ax2, bx2) - max(ax1, bx1))
        overlap_h = max(0, min(ay2, by2) - max(ay1, by1))
        overlap = overlap_w * overlap_h

        return areaA + areaB - overlap

solution = Solution()
print(solution.computeArea(-3, 0, 3, 4, 0, -1, 9, 2))  # Output: 45
print(solution.computeArea(-2, -2, 2, 2, -2, -2, 2, 2))  # Output: 16
print(solution.computeArea(0, 0, 0, 0, -1, -1, 1, 1))  # Output: 1
