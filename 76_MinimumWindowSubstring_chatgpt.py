from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        need = Counter(t)            # t に必要な各文字の個数
        missing = len(t)             # まだ満たしていない文字の総数
        left = 0                     # 窓の左端
        min_len = float("inf")
        min_left = 0

        # 右端を1文字ずつ進める
        for right, ch in enumerate(s):
            # その文字が必要なら missing を減らす (need[ch] > 0 の場合のみ)
            if need[ch] > 0:
                missing -= 1
            need[ch] -= 1   # need は負にもなりうる（余分な文字の記録）

            # すべての文字が揃ったら、左を進めて最小化を試みる
            while missing == 0:
                # 更新
                window_len = right - left + 1
                if window_len < min_len:
                    min_len = window_len
                    min_left = left

                # 左を1つ動かして窓から外す準備
                left_ch = s[left]
                need[left_ch] += 1
                # もし need[left_ch] > 0 になれば、その文字が不足していることになる
                if need[left_ch] > 0:
                    missing += 1
                left += 1
                print(need, missing, s[min_left:min_left+min_len])

        return "" if min_len == float("inf") else s[min_left:min_left+min_len]

solution = Solution()
s = "ADOBECODEBANC"
t = "ABC"
print(solution.minWindow(s, t))  # 出力: "BANC"