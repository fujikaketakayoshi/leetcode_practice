class Solution:
    def countDigitOne(self, n: int) -> int:
        count = 0
        m = 1
        
        while m <= n:
            high = n // (m * 10)
            cur = (n // m) % 10
            low = n % m
            print(f"m: {m}, high: {high}, cur: {cur}, low: {low}")

            if cur == 0:
                count += high * m
            elif cur == 1:
                count += high * m + low + 1
            else:
                count += (high + 1) * m
            
            m *= 10
        
        return count

solution = Solution()
print(solution.countDigitOne(13))  # 出力: 6
print(solution.countDigitOne(222))