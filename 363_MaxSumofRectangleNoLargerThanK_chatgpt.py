from bisect import bisect_left, insort


class Solution:
    def maxSumSubmatrix(self, matrix: list[list[int]], k: int) -> int:
        H = len(matrix)
        W = len(matrix[0])

        ans = float("-inf")

        # top, bottom を固定する
        for top in range(H):
            # top～bottom の各列の合計
            col_sum = [0] * W

            for bottom in range(top, H):
                for x in range(W):
                    col_sum[x] += matrix[bottom][x]

                # col_sum に対して
                # 「連続部分配列の和 <= k の最大値」を探す

                prefix = 0

                # 現在位置より前に登場したprefixを昇順で管理
                sorted_prefix = [0]

                for v in col_sum:
                    prefix += v

                    # prefix - old_prefix <= k
                    #
                    # old_prefix >= prefix - k
                    #
                    # なので prefix-k 以上で最小のold_prefixを探す
                    i = bisect_left(sorted_prefix, prefix - k)

                    if i < len(sorted_prefix):
                        candidate = prefix - sorted_prefix[i]
                        ans = max(ans, candidate)

                        # kを超えられないので、kなら理論上の最大値
                        if ans == k:
                            return k

                    # 今回のprefixは、次回以降left側として使える
                    insort(sorted_prefix, prefix)

        return ans