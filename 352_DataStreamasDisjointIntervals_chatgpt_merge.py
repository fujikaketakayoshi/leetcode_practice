class SummaryRanges:

    def __init__(self):
        self.intervals = []

    def addNum(self, value: int) -> None:
        new_intervals = []
        start = end = value
        inserted = False

        for s, e in self.intervals:

            # 今回の区間より完全に左
            if e + 1 < start:
                new_intervals.append([s, e])

            # 今回の区間より完全に右
            elif end + 1 < s:
                if not inserted:
                    new_intervals.append([start, end])
                    inserted = True

                new_intervals.append([s, e])

            # 重なる or 隣接する
            else:
                start = min(start, s)
                end = max(end, e)

        if not inserted:
            new_intervals.append([start, end])

        self.intervals = new_intervals

    def getIntervals(self) -> List[List[int]]:
        return self.intervals