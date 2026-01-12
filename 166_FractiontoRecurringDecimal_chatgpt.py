class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        # 0 の場合
        if numerator == 0:
            return "0"

        res = []

        # 符号処理
        if (numerator < 0) ^ (denominator < 0):
            res.append('-')

        numerator = abs(numerator)
        denominator = abs(denominator)

        # 整数部分
        integer_part = numerator // denominator
        res.append(str(integer_part))

        remainder = numerator % denominator
        if remainder == 0:
            return ''.join(res)

        res.append('.')

        # 余り → その余りが出たときの index
        seen = {}

        while remainder != 0:
            if remainder in seen:
                idx = seen[remainder]
                res.insert(idx, '(')
                res.append(')')
                break

            seen[remainder] = len(res)

            remainder *= 10
            res.append(str(remainder // denominator))
            remainder %= denominator

        return ''.join(res)
    
solution = Solution()
print(solution.fractionToDecimal(1, 2))        # Output: "0.5"
print(solution.fractionToDecimal(2, 1))        # Output: "2"
print(solution.fractionToDecimal(2, 3))        # Output: "0.(6)"
print(solution.fractionToDecimal(4, 333))      # Output: "0.(012)"
print(solution.fractionToDecimal(1, 6))        # Output: "0.1(6)"
print(solution.fractionToDecimal(-50, 8))      # Output: "-6.25"
print(solution.fractionToDecimal(7, -12))      # Output: "-0.58(3)"
print(solution.fractionToDecimal(-1, -2147483648))  # Output: "0.0000000004656612873077392578125"

print(-1 / -2147483648)  # Output: 0.0000000004656612873077392578125