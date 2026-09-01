class SummaryRanges:

    def __init__(self):
        # self.arr = []
        self.intervals = []
        return None

    def addNum(self, value: int) -> None:
        n = len(self.intervals)
        if n == 0:
            self.intervals = [[value, value]]
        elif n == 1:
            s, e = self.intervals[0]
            if s == value + 1:
                self.intervals[0][0] = value
            elif e == value - 1:
                self.intervals[0][1] = value
            elif value < s:
                self.intervals.insert(0, [value, value])
            elif e < value:
                self.intervals.append([value, value])
        else:
            print(value)
            if value + 1 < self.intervals[0][0]:
                self.intervals.insert(0, [value, value])
            elif self.intervals[-1][1] < value - 1:
                self.intervals.append([value, value])
            else:
                for i in range(n - 1):
                    # print(n, i + 1, self.intervals)
                    s0, e0 = self.intervals[i]
                    s1, e1 = self.intervals[i + 1]
                    if s0 == value + 1:
                        print('1!')
                        self.intervals[i][0] = value
                        break
                    elif e1 == value - 1:
                        print('2!')
                        self.intervals[i + 1][1] = value
                        break
                    elif e0 == value - 1 and s1 == value + 1:
                        print('3!')
                        self.intervals.pop(i + 1)
                        self.intervals[i][1] = e1
                        break
                    elif e0 == value - 1:
                        print('4!')
                        self.intervals[i][1] = value
                        break
                    elif s1 == value + 1:
                        print('5!')
                        self.intervals[i + 1][0] = value
                        break
                    elif e0 < value < s1:
                        print('6!')
                        self.intervals.insert(i + 1, [value, value])
                        break
                    else:
                        print('7!')
        # print(self.intervals)
        return None
    def getIntervals(self) -> list[list[int]]:
        return self.intervals


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()