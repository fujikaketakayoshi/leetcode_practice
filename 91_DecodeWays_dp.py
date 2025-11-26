class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        
        dp[n] = 1  # 終端の空文字は 1 通り
        
        for i in range(n - 1, -1, -1):
            if s[i] == '0':
                dp[i] = 0
            else:
                # 1文字デコード
                dp[i] = dp[i + 1]
                
                # 2文字デコード可能？
                if i + 1 < n and 10 <= int(s[i:i+2]) <= 26:
                    dp[i] += dp[i + 2]
        
        return dp[0]

Solution = Solution()
print(Solution.numDecodings("12"))      # 2
print(Solution.numDecodings("226"))     # 3
print(Solution.numDecodings("06"))      # 0
print(Solution.numDecodings("11106"))   # 2
print(Solution.numDecodings("10"))      # 1
print(Solution.numDecodings("27"))      # 1
print(Solution.numDecodings("0"))       # 0
print(Solution.numDecodings("2101"))    # 1