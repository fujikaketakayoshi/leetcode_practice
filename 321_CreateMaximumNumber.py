from collections import deque
class Solution:
    def maxNumber(self, nums1: list[int], nums2: list[int], k: int) -> list[int]:
        def getCand(arr):
            n = len(arr)
            cands = [[] for _ in range(n + 1)]
            for c in range(1, min(n, k) + 1):
                sute = n - c
                stack = [arr[0]]
                for i in range(1, n):
                    while sute > 0 and stack and stack[-1] < arr[i]:
                        stack.pop()
                        sute -= 1
                    stack.append(arr[i])
                cands[c] = stack[:c]
            return cands
        cand1 = getCand(nums1)
        cand2 = getCand(nums2)

        m = len(nums1)
        n = len(nums2)
        max_num = 0
        for i in range(0, k + 1):
            if i >= m + 1 or k - i >= n + 1:
                continue
            # print(cand1[i], cand2[k - i])
            q1 = deque()
            q1.extend(cand1[i])
            q2 = deque()
            q2.extend(cand2[k - i])

            result = []
            while q1 or q2:
                if q1 > q2:
                    result.append(q1.popleft())
                else:
                    result.append(q2.popleft())
            max_num = max(max_num, int(''.join(map(str,result))))
        ans = list(map(int, list(str(max_num))))
        return ans
