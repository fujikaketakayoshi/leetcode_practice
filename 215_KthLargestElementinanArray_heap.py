import heapq

class Solution:
    def findKthLargest(self, nums, k):
        heap = []

        for x in nums:
            heapq.heappush(heap, x)

            # k 個より多くなったら一番小さいものを削除
            if len(heap) > k:
                heapq.heappop(heap)

        # heap の先頭が k 番目に大きい
        return heap[0]

solution = Solution()
print(solution.findKthLargest([3,2,1,5,6,4], 2))  # 出力: 5
print(solution.findKthLargest([3,2,3,1,2,4,5,5,6], 4))  # 出力: 4

