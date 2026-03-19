class Solution:
    def numberToWords(self, num: int) -> str:
        keta = ['', 'Thousand', 'Million', 'Billion']
        keta_i = -1
        result = []
        while num > 0:
            keta_i += 1
            three = num % 1000
            num //= 1000
            result.append(str(three) + keta[keta_i])
        
        print(result)