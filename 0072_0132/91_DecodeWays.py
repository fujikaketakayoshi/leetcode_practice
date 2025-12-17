class Solution:
    def numDecodings(self, s: str) -> int:
        digits = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15','16','17','18','19','20','21','22','23','24','25','26'}
        digits_invalid = {'01','02','03','04','05','06','07','08','09'}
        l = len(s)
        results = []
        def dfs(start, path):
            if start == l:
                results.append(path[:])
                return
            if start + 1 < l and s[start:start + 2] in {'10', '20'}:
                path.append(s[start:start + 2])
                dfs(start + 2, path)
                path.pop()
            else:
                path.append(s[start])
                dfs(start + 1, path)
                path.pop()
                if start + 1 < l:
                    path.append(s[start:start + 2])
                    dfs(start + 2, path)
                    path.pop()

        dfs(0, [])
        cnt = 0
        for rs in results:
            check = True
            for r in rs:
                if r in digits_invalid:
                    check = False
                    break
                if not r in digits:
                    check = False
                    break
            if check:
                cnt += 1
        
        return cnt
    
Solution = Solution()
print(Solution.numDecodings("12"))      # 2
print(Solution.numDecodings("226"))     # 3
print(Solution.numDecodings("06"))      # 0
print(Solution.numDecodings("11106"))   # 2
print(Solution.numDecodings("10"))      # 1
print(Solution.numDecodings("27"))      # 1
print(Solution.numDecodings("0"))       # 0
print(Solution.numDecodings("2101"))    # 1