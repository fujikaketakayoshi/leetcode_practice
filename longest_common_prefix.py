class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        
        # 最短の文字列長までしか共通prefixは存在しない
        min_len = min(len(s) for s in strs)

        prefix = ""
        for i in range(min_len):
            char = strs[0][i]
            # 全ての文字列で同じ位置の文字が一致するか
            if all(s[i] == char for s in strs):
                prefix += char
            else:
                break
        return prefix

solution = Solution()
print(solution.longestCommonPrefix(["flower","flow","flight"]))