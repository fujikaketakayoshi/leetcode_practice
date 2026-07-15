class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        first = float("inf")
        second = float("inf")

        for x in nums:
            if x <= first:
                first = x
            elif x <= second:
                second = x
            else:
                # return True
                return (first, second)

        return False

s = Solution()
print(s.increasingTriplet([2, 1, 5, 4, 6, 3, 7, 8, 9]))
