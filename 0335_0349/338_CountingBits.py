class Solution:
    def countBits(self, n: int) -> list[int]:
        ans = []
        for i in range(n + 1):
            x = i
            cnt = 0
            while x > 0:
                if x % 2 == 1:
                    cnt += 1
                x //= 2
            ans.append(cnt)
        return ans