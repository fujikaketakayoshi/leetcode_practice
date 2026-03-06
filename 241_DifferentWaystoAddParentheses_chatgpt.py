class Solution:
    def diffWaysToCompute(self, expression: str) -> list[int]:

        res = []

        for i, c in enumerate(expression):

            if c in "+-*":

                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i+1:])
                print(i, c, left, right, res)

                for l in left:
                    for r in right:

                        if c == "+":
                            res.append(l + r)
                        elif c == "-":
                            res.append(l - r)
                        else:
                            res.append(l * r)

        if not res:
            res.append(int(expression))

        return res

solution = Solution()
# print(solution.diffWaysToCompute("2-1-1"))
print(solution.diffWaysToCompute("2*3-4*5"))