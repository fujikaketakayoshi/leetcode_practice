class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        ok = [False] * n
        i = 0
        while i < n:
            j = 1
            while j < n - i + 1:
                first = num[i:i + j]
                if not first:
                    j += 1
                    continue
                l = 1
                while l < n - i + 1:
                    second = num[i + 1:i + 1 + l]
                    if not second:
                        l += 1
                        continue
                    rest = num[i + 1 + l:]
                    ans = int(first) + int(second)
                    lans = len(str(ans))
                    print(first, second, rest, ans, rest[:lans])
                    if len(rest) >= lans and str(ans) == rest[:lans]:
                        for fs in range(i, i + j + 1):
                            ok[fs] = True
                        ok[i + l + lans] = True

                    l += 1
                j += 1
            i += 1
        print(ok)
