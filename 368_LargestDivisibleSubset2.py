class Solution:
    def largestDivisibleSubset(self, nums: list[int]) -> list[int]:
        nums.sort()
        n = len(nums)        
        divisors = [set() for _ in range(n)]

        for i in range(n):
            num = nums[i]
            for j in range(1, num + 1):
                if num % j == 0:
                    divisors[i].add(j)
        print(divisors)

        max_divs = []
        for i in range(n - 1, -1, -1):
            ans = [nums[i]]
            for j in range(i - 1, -1, -1):
                divand = divisors[i] & divisors[j]
                if divand == divisors[j]:
                    ans.append(nums[j])
            if len(ans) > len(max_divs):
                max_divs = ans[:]
        return max_divs

