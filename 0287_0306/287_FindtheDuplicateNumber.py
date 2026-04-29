class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        slow = nums[0]
        fast = nums[0]

        print(slow, fast)
        # cycle 内で出会う
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            print(slow, fast)
            if slow == fast:
                break

        # cycle の入口を探す
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
            print(slow, fast)

        return slow

s = Solution()
print(s.findDuplicate([1,3,4,2,3]))  # 2
print(s.findDuplicate([1,3,4,2,2]))  # 2
print(s.findDuplicate([3,1,3,4,2]))  # 3
print(s.findDuplicate([3,3,3,3,3]))  # 3