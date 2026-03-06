class Solution:
    def diffWaysToCompute(self, expression: str) -> list[int]:
        i = 0
        nums = []
        signs = []
        num = 0
        while i < len(expression):
            c = expression[i]
            if c.isdigit():
                num = num * 10 + int(c)
            elif c in ('+', '-', '*'):
                signs.append(c)
                nums.append(num)
                num = 0
            i += 1
        nums.append(num)

        # print(nums, signs)

        results = []
        def dfs(nums, signs):
            if len(nums) == 1:
                results.append(nums[0])
                return
            i = 0
            while i < len(nums) - 1:
                # print(i)
                n1 = nums[i]
                n2 = nums[i+1]
                sign = signs[i]
                if sign == '+':
                    next_val = n1 + n2
                elif sign == '-':
                    next_val = n1 - n2
                elif sign == '*':
                    next_val = n1 * n2
                next_nums = nums[:]
                # print(i, next_nums)
                next_nums.pop(i)
                next_nums.pop(i)
                next_nums.insert(i, next_val)
                next_signs = signs[:]
                next_signs.pop(i)
                dfs(next_nums, next_signs)
                i += 1
        
        dfs(nums, signs)
        return results

solution = Solution()
print(solution.diffWaysToCompute("2-1-1"))  
print(solution.diffWaysToCompute("2*3-4*5"))    