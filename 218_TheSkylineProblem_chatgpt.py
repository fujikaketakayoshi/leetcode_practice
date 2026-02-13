import heapq

class Solution:
    def getSkyline(self, buildings):
        events = []
        for l, r, h in buildings:
            events.append((l, -h, r))
            events.append((r, 0, 0))

        events.sort()

        result = []
        heap = [(0, float('inf'))]  # (height, right)
        prev_max = 0

        for x, neg_h, r in events:
            # remove ended buildings
            while heap[0][1] <= x:
                heapq.heappop(heap)

            if neg_h != 0:
                heapq.heappush(heap, (neg_h, r))

            curr_max = -heap[0][0]

            if curr_max != prev_max:
                result.append([x, curr_max])
                prev_max = curr_max

        return result

solution = Solution()
print(solution.getSkyline([[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]))

print(solution.getSkyline([[0,2,3],[2,5,3]]))