class Solution:
    def getSkyline(self, buildings: list[list[int]]) -> list[list[int]]:
        pre_r = -1
        craster = []
        tmp_b = []
        for b in buildings:
            l, r, h = b
            if pre_r < l:
                if len(tmp_b) > 0:
                    craster.append(tmp_b[:])
                pre_r = r
                tmp_b.clear()
                tmp_b.append(b)
            else:
                tmp_b.append(b)
                pre_r = max(pre_r, r)
        if len(tmp_b) > 0:
            craster.append(tmp_b[:])
        
        print(craster)

solution = Solution()
print(solution.getSkyline([[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]))

print(solution.getSkyline([[0,2,3],[2,5,3]]))