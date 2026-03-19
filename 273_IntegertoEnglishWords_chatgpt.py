class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        
        below_20 = [
            "", "One", "Two", "Three", "Four", "Five", "Six", "Seven",
            "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen",
            "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"
        ]

        tens = [
            "", "", "Twenty", "Thirty", "Forty",
            "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"
        ]

        def helper(n):
            if n == 0:
                return ""
            elif n < 20:
                return below_20[n] + " "
            elif n < 100:
                return tens[n // 10] + " " + helper(n % 10)
            else:
                return below_20[n // 100] + " Hundred " + helper(n % 100)

        thousands = ["", "Thousand", "Million", "Billion"]
        i = 0
        res = ""

        while num > 0:
            if num % 1000 != 0:
                res = helper(num % 1000) + thousands[i] + " " + res
            num //= 1000
            i += 1

        return res.strip()

s = Solution()
print(s.numberToWords(1234567891))
print(s.numberToWords(123))
print(s.numberToWords(12345))
print(s.numberToWords(10101010))