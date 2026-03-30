class Solution:
    def nthUglyNumber(self, n: int) -> int:
        def is_ugly_number(num):
            for p in [2, 3, 5]:
                while num % p == 0:
                    num //= p
            return num == 1
        
        cnt = 0
        num = 0
        while cnt < n:
            num += 1
            if is_ugly_number(num):
                cnt += 1
        return num

s = Solution()
print(s.nthUglyNumber(10)) # 12
