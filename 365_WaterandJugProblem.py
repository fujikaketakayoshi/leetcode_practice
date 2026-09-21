class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        if x + y < target:
            return False

        ans = set()
        ans.add(x)
        ans.add(y)
        ans.add(x + y)
        if target in ans:
            return True

        if x <= y:
            nowy = y
            amari = 0
            while nowy - x >= 0:
                nowy -= x
                ans.add(nowy)
                if nowy < x:
                    amari = nowy
                    ans.add(amari)
                    ans.add(amari + y)
            ans.add(y - (x - amari))
            ans.add(x + (x - amari))
            if target in ans:
                return True
            else:
                return False

        if x > y:
            nowx = x
            amari = 0
            while nowx - y >= 0:
                nowx -= y
                ans.add(nowx)
                if nowx < y:
                    amari = nowx
                    ans.add(amari)
                    ans.add(amari + x)
            ans.add(x - (y - amari))
            ans.add(y + (y - amari))
            if target in ans:
                return True
            else:
                return False

s = Solution()
print(s.canMeasureWater(3, 5, 4))
print(s.canMeasureWater(13, 11, 1)) # Trueだが、Falseが返ってしまう