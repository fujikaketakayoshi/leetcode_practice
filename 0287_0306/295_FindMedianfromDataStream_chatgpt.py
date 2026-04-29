import heapq

class MedianFinder:

    def __init__(self):
        self.small = []  # max heap (負の値)
        self.large = []  # min heap

    def addNum(self, num: int) -> None:
        # まず small に入れる
        heapq.heappush(self.small, -num)

        # small の最大値を large に移す
        heapq.heappush(self.large, -heapq.heappop(self.small))

        # large の方が多すぎたら戻す
        if len(self.large) > len(self.small) + 1:
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self) -> float:
        if len(self.large) > len(self.small):
            return float(self.large[0])

        return (self.large[0] - self.small[0]) / 2

# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
obj.addNum(10)
print(obj.findMedian())
obj.addNum(2)
print(obj.findMedian())
obj.addNum(3)
print(obj.findMedian())
obj.addNum(2)
print(obj.findMedian())