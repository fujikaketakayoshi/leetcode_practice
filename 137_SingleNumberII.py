class Solution:
    def singleNumber(self, nums):
        ones = 0
        twos = 0

        for x in nums:
            ones = (ones ^ x) & ~twos
            twos = (twos ^ x) & ~ones
            bit_ones = bin(ones)
            bit_twos = bin(twos)
            print(f"After processing {x}: ones = {ones}, bit_ones = {bit_ones}, twos = {twos}, bit_twos = {bit_twos}")

        return ones

solution = Solution()
print(solution.singleNumber([2, 2, 3, 2]))  # Output: 3
print(solution.singleNumber([0, 1, 0, 1, 0, 1, 99]))  # Output: 99
print(solution.singleNumber([99, 3, 1, 3, 1, 3, 1]))