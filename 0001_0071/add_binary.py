class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) < len(b):
            a, b = b, a
        b = (len(a) - len(b)) * '0' + b
        result = ''
        carry = '0'
        for i, ch in enumerate(reversed(b)):
            idx = -1 * i - 1
            # print(a[idx], ch, carry, result)
            if ch == '1' and a[idx] == '1' and carry == '1':
                result = '1' + result
                carry = '1'
            elif ch == '1' and a[idx] == '1':
                result = '0' + result
                carry = '1'
            elif ((ch == '1' and a[idx] == '0') or (ch == '0' and a[idx] == '1')) and carry == '1':
                result = '0' + result
                carry = '1'
            elif (ch == '1' and a[idx] == '0') or (ch == '0' and a[idx] == '1'):
                result = '1' + result
                carry = '0'
            elif ch == '0' and a[idx] == '0' and carry == '1':
                result = '1' + result
                carry = '0'
            else:
                result = '0' + result
                carry = '0'
        if carry == '1':
            result = '1' + result
        
        return result

solution = Solution()
print(solution.addBinary("1010", "1011"))
print(solution.addBinary("11", "1"))
print(solution.addBinary("0", "0"))
print(solution.addBinary("111", "101"))