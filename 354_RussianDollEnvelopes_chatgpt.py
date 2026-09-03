from bisect import bisect_left
class Solution:
    def maxEnvelopes(self, envelopes: list[list[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        print(envelopes)
        heights = [h for w, h in envelopes]
        lis = []
        for x in heights:
            i = bisect_left(lis, x)

            if i == len(lis):
                lis.append(x)
            else:
                lis[i] = x
        return len(lis)