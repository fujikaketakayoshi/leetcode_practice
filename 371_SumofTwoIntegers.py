class Solution:
    def getSum(self, a: int, b: int) -> int:
        arr = [1] * 10000

        if a >= 0:
            for i in range(a):
                arr.append(i)
        else:
            for i in range(a, 0):
                arr.pop()
        if b >= 0:
            for i in range(b):
                arr.append(i)
        else:
            for i in range(b, 0):
                arr.pop()
        
        if len(arr) == 10000:
            return 0
        elif len(arr) < 10000:
            ans = []
            while len(arr) < 10000:
                ans.append(1)
                arr.append(1)
            return len(-ans)
        else:
            ans = []
            while len(arr) > 10000:
                ans.append(1)
                arr.pop()
            return len(ans)