class BIT:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def add(self, i, x):
        while i <= self.n:
            self.bit[i] += x
            i += i & -i

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s

class Solution:
    def countSmaller(self, nums):
        # 座標圧縮
        vals = sorted(set(nums))
        rank = {v:i+1 for i,v in enumerate(vals)}

        bit = BIT(len(vals))

        ans = []

        # 後ろから
        for x in reversed(nums):
            r = rank[x]

            # 自分未満
            ans.append(bit.sum(r - 1))

            # 自分を追加
            bit.add(r, 1)

        return ans[::-1]

s = Solution()
print(s.countSmaller([5,2,6,1]))  # [2,1,1,0]
