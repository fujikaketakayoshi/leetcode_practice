class Solution:
    def minPatches(self, nums: list[int], n: int) -> int:
        reach = 0      # 1～reachまで作れる
        i = 0
        ans = 0

        result = []
        while reach < n:
            if i < len(nums) and nums[i] <= reach + 1:
                # nums[i]を使うと作れる範囲が広がる
                reach += nums[i]
                result.append(nums[i])
                i += 1
            else:
                # reach+1 を追加する
                result.append(reach + 1)
                reach += reach + 1
                ans += 1
        print(result)
        return ans

s = Solution()
print(s.minPatches([1, 3], 6))  # Output: 1
print(s.minPatches([1, 5, 10], 20)) 
print(s.minPatches([5, 10], 20)) 
print(s.minPatches([], 20)) 
