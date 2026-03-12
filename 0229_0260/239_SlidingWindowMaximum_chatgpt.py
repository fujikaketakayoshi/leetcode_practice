from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        dq = deque()  # indexを入れる
        result = []

        for i in range(len(nums)):
            
            # ① ウィンドウ外削除
            if dq and dq[0] <= i - k:
                dq.popleft()
            
            # ② 小さい値削除（単調減少を維持）
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            
            # ③ 追加
            dq.append(i)
            
            print(dq)
            # ④ 答え追加
            if i >= k - 1:
                result.append(nums[dq[0]])
        
        return result

solution = Solution()
print(solution.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))  # 出力: [3,3,5,5,6,7] 