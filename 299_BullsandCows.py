class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        s_ex_cnt = [0] * 10
        g_ex_cnt = [0] * 10
        a = 0
        b = 0
        for s, g in zip(secret, guess):
            if s == g:
                a += 1
            else:
                s_ex_cnt[int(s)] += 1
                g_ex_cnt[int(g)] += 1
        print(s_ex_cnt, g_ex_cnt)
        for i in range(10):
            # if s_ex_cnt[i] > 0 and g_ex_cnt[i] > 0:
            b += min(s_ex_cnt[i], g_ex_cnt[i])
        return str(a) + 'A' + str(b) + 'B'

s = Solution()
print(s.getHint("1807", "7810"))
print(s.getHint("1121", "1311"))