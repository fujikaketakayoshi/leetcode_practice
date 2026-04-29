from bisect import bisect_left

class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        tails = []

        for num in nums:
            idx = bisect_left(tails, num)

            if idx == len(tails):
                tails.append(num)
            else:
                tails[idx] = num

        print(tails)
        return len(tails)

s = Solution()
print(s.lengthOfLIS([10,9,2,5,3,7,1,4,101,18]))
