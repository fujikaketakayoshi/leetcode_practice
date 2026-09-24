class FenwickMax:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    # i以下の最大値
    def query(self, i):
        res = 0

        while i > 0:
            res = max(res, self.bit[i])
            i -= i & -i

        return res

    # iの位置にvalueを反映
    def update(self, i, value):
        while i <= self.n:
            self.bit[i] = max(self.bit[i], value)
            i += i & -i


class Solution:
    def maxEnvelopes(self, envelopes: list[list[int]]) -> int:
        # 幅の昇順
        envelopes.sort(key=lambda x: x[0])

        # 高さを座標圧縮
        heights = sorted(set(h for _, h in envelopes))
        rank = {h: i + 1 for i, h in enumerate(heights)}

        bit = FenwickMax(len(heights))
        ans = 0

        i = 0

        while i < len(envelopes):
            j = i
            w = envelopes[i][0]

            # 同じ幅の範囲を探す
            while j < len(envelopes) and envelopes[j][0] == w:
                j += 1

            updates = []

            # 同じ幅の封筒についてDPを計算
            for k in range(i, j):
                _, h = envelopes[k]
                r = rank[h]

                # 高さがh未満の封筒だけ
                best = bit.query(r - 1)
                dp = best + 1

                updates.append((r, dp))
                ans = max(ans, dp)

            # 同じ幅同士が影響しないように、
            # 全部計算し終わってからFenwick Treeを更新
            for r, dp in updates:
                bit.update(r, dp)

            i = j

        return ans

s = Solution()
envelopes = [[5,4],[6,4],[6,7],[2,3]]
print(s.maxEnvelopes(envelopes))  # Output: 3
