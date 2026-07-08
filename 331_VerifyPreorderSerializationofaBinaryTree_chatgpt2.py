class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        pres = preorder.split(',')
        print(pres)
        i = 0
        while i < len(pres) - 2:
            if pres[i] != '#' and pres[i + 1] == '#' and pres[i + 2] == '#':
                tmp = pres[:i] + ['#'] + pres[i + 3:]
                pres = tmp.copy()
                # print(pres)
                i = 0
                continue
            i += 1
        return pres[0] == '#' and len(pres) == 1
