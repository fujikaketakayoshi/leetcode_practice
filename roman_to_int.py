class Solution:
    def romanToInt(self, s: str) -> int:
        romans = {
            "M": 1000, "CM": 900, "D": 500, "CD": 400,
            "C": 100, "XC": 90, "L": 50, "XL": 40,
            "X": 10, "IX": 9, "V": 5, "IV": 4, "I": 1
        }
        
        i = 0
        num = 0
        while i < len(s):
            if i + 1 < len(s) and s[i:i+2] in romans:
                num += romans[s[i:i+2]]
                i += 2
            else:
                num += romans[s[i]]
                i += 1
        return num

# Example usage:
solution = Solution()
# print(solution.romanToInt("III"))      # Output: 3
# print(solution.romanToInt("IV"))       # Output: 4
# print(solution.romanToInt("IX"))       # Output: 9
# print(solution.romanToInt("LVIII"))    # Output: 58
print(solution.romanToInt("MCMXCIV"))  # Output: 1994