class Solution:
    def singleNumber(self, nums: list[int]) -> list[int]:
        xor_all = 0
        for n in nums:
            xor_all ^= n
        
        diff = xor_all & -xor_all
        print(diff)

        a = 0
        b = 0
        
        for n in nums:
            if n & diff:
                a ^= n
            else:
                b ^= n
        
        return [a, b]

solution = Solution()
print(solution.singleNumber([1,2,1,3,2,5]))  # Output: [3,5] (order may vary)
