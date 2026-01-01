from collections import defaultdict
from math import gcd

class Solution:
    def maxPoints(self, points):
        n = len(points)
        if n <= 2:
            return n

        ans = 0

        for i in range(n):
            slopes = defaultdict(int)
            x1, y1 = points[i]

            for j in range(i + 1, n):
                x2, y2 = points[j]
                dx = x2 - x1
                dy = y2 - y1

                if dx == 0:
                    dy = 1
                    dx = 0
                elif dy == 0:
                    dy = 0
                    dx = 1
                else:
                    g = gcd(dy, dx)
                    dy //= g
                    dx //= g
                    if dx < 0:
                        dx = -dx
                        dy = -dy

                slopes[(dy, dx)] += 1

            max_on_line = 0
            for cnt in slopes.values():
                max_on_line = max(max_on_line, cnt)

            ans = max(ans, max_on_line + 1)

        return ans

solution = Solution()
print(solution.maxPoints([[1,1],[2,2],[3,3]]))  # Output: 3
print(solution.maxPoints([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]))  # Output: 4
