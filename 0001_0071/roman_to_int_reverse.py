class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        
        total = 0
        
        # 文字列を末尾から走査
        for i in range(len(s) - 1, -1, -1):
            
            current_val = roman_map[s[i]]
            # ひとつ前の文字が存在し、現在の文字の値が前の文字の値より小さい場合
            # (例: IVのVを処理するときにIを考慮)
            if i < len(s) - 1 and current_val < roman_map[s[i+1]]:
                total -= current_val
            else:
                total += current_val
        return total

# Example usage:
solution = Solution()
# print(solution.romanToInt("III"))      # Output: 3
# print(solution.romanToInt("IV"))       # Output: 4
# print(solution.romanToInt("IX"))       # Output: 9
# print(solution.romanToInt("LVIII"))    # Output: 58
print(solution.romanToInt("MCMXCIV"))  # Output: 1994