from collections import defaultdict
class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        str_nums = list(map(str, nums))
        pre_digit = defaultdict(list)
        for char in str_nums:
            pre_digit[char[0]].append(char)

        def dfs(arr, path, max_num, used):
            if len(path) == len(arr):
                max_num = max(max_num, int(''.join(path)))
                return max_num
            for i in range(len(arr)):
                if used[i]:
                    continue
                path.append(arr[i])
                used[i] = True
                max_num = dfs(arr, path, max_num, used)
                used[i] = False
                path.pop()
            return max_num
        
        ans = ''
        for digit in reversed(sorted(pre_digit.keys())):
            if digit == '0':
                digit_max = '0' * len(pre_digit[digit])
            else:
                used = [False] * len(pre_digit[digit])
                digit_max = str(dfs(pre_digit[digit], [], 0, used))
            ans += digit_max
        if all(i == '0' for i in list(ans)):
            ans = '0'
        return ans

solution = Solution()
print(solution.largestNumber([3,30,34,5,9]))  # 出力: "9534330"
print(solution.largestNumber([10,2]))        # 出力: "210"
print(solution.largestNumber([0,0]))        # 出力: "0"