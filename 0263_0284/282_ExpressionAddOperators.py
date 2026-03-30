from itertools import permutations

class Solution:
    def addOperators(self, num: str, target: int) -> list[str]:
        nums = list(num)
        n = len(nums)
        
        execs = []
        def dfs(es, l):
            if len(es) == l:
                execs.append(es.copy())
                return
            for e in ['+', '-', '*']:
                es.append(e)
                dfs(es, l)
                es.pop()
        
        dfs([], n - 1)

        ans = []
        for exe in execs:
            i = 0
            exp = ''
            while i < n:
                if i == n - 1:
                    exp += nums[i]
                else:
                    exp += nums[i] + exe[i]
                i += 1
            if eval(exp) == target:
                ans.append(exp)
        return ans
s = Solution()
print(s.addOperators("123", 6)) # ["1+2+3", "1*2*3"]
print(s.addOperators("232", 8)) # ["2*3+2", "2+3*2"]
print(s.addOperators("105", 5)) # ["1*0+5","10-5"]
print(s.addOperators("00", 0)) # ["0+0", "0-0", "0*0"]
print(s.addOperators("3456237490", 9191)) # []