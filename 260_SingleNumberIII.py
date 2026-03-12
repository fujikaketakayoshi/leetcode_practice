class Solution:
    def singleNumber(self, nums: list[int]) -> list[int]:
        seen = set()
        for n in nums:
            if n in seen:
                seen.remove(n)
            else:
                seen.add(n)
        
        return list(seen)

solution = Solution()
print(solution.singleNumber([1,2,1,3,2,5]))  # Output: [3,5] (order may vary)
