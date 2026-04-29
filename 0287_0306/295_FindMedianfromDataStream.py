from bisect import insort
class MedianFinder:

    def __init__(self):
        self.arr = []
        self.len = 0
    
    def addNum(self, num: int) -> None:
        insort(self.arr, num)
        self.len += 1

    def findMedian(self) -> float:
        idx = self.len // 2
        if self.len % 2 == 0:
            return (self.arr[idx - 1] + self.arr[idx]) / 2
        else:
            return float(self.arr[idx])


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()