class SummaryRanges:

    def __init__(self):
        self.n = 10 ** 4 + 2
        self.range = [0] * self.n
        self.intervals = []
        return None

    def addNum(self, value: int) -> None:
        if self.range[value] != 1:
            self.range[value] = 1
                
        # print(self.range[9990:])
        prev = 0
        self.intervals = []
        s = None
        e = None
        for i in range(self.n):
            if prev == 0 and self.range[i] == 1:
                s = i
                prev = 1
            # elif prev == 1 and self.range[i] == 1:
            #     prev = 1
            elif prev == 1 and self.range[i] == 0:
                e = i - 1
                self.intervals.append([s, e])
                s = None
                e = None
                prev = 0
        return None
    def getIntervals(self) -> list[list[int]]:
        return self.intervals


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()

s = SummaryRanges()
s.addNum(1)
s.addNum(3)
s.addNum(7)
print(s.getIntervals())
s.addNum(2)
print(s.getIntervals())