class SummaryRanges:

    def __init__(self):
        self.exists = [False] * 10001

    def addNum(self, value: int) -> None:
        self.exists[value] = True

    def getIntervals(self) -> List[List[int]]:
        intervals = []
        i = 0

        while i <= 10000:
            if not self.exists[i]:
                i += 1
                continue

            start = i

            while i <= 10000 and self.exists[i]:
                i += 1

            intervals.append([start, i - 1])

        return intervals