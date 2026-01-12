class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        ans_keta = 0
        ans = ''
        tmp = 0
        while numerator > 0:
            if numerator < denominator:
                ans_keta -= 1
                numerator *= 10
            while numerator >= denominator:
                numerator -= denominator
                tmp += 1
                print(numerator, ans)
            ans += str(tmp)
        print(tmp)

