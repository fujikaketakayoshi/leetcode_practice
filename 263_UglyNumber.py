class Solution:
    def isUgly(self, n: int) -> bool:
        def prime_factor_list(n):
            res = []
            d = 2
            while d * d <= n:
                while n % d == 0:
                    res.append(d)
                    n //= d
                d += 1
            if n > 1:
                res.append(n)
            return res
        
        pfl = prime_factor_list(n)
        print(pfl)
        if n <=  0:
            return False
        ok = True
        for pf in pfl:
            if pf == 2 or pf == 3 or pf == 5:
                continue
            else:
                ok = False
                break
        return ok

s = Solution()
print(s.isUgly(6))  # True
print(s.isUgly(8))  # True
print(s.isUgly(14)) # False