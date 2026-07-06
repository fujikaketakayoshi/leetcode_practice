class Solution:
    def minPatches(self, nums: list[int], n: int) -> int:
        reach = 0
        i = 0
        while reach < n:
            next_num = reach + 1
            if i < len(nums) and next_num >= nums[i]:
                reach += 1
                i += 1
                continue
            elif i < len(nums) and reach < nums[i]:
                reach += next_num
        print(reach)