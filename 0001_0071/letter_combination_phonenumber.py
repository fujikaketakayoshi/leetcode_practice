class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        numLetters = {
            2: ['a', 'b', 'c'],
            3: ['d', 'e', 'f'],
            4: ['g', 'h', 'i'],
            5: ['j', 'k', 'l'],
            6: ['m', 'n', 'o'],
            7: ['p', 'q', 'r', 's'],
            8: ['t', 'u', 'v'],
            9: ['w', 'x', 'y', 'z'],
        }
        result = []
        combis = []
        i = 0
        while i < len(digits):
            now_letters = numLetters[int(digits[i])]
            if result == []:
                result = now_letters
            else:
                new_result = []
                for j in result:
                    for k in now_letters:
                        new_result.append(j + k)
                result = new_result
            i += 1
        return result

solution = Solution()
print(solution.letterCombinations("23"))
print(solution.letterCombinations("23539"))