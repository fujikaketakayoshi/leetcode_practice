class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []
        
        mapping = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }
        result = []  # ★ ← これは Enclosing スコープ
        
        def backtrack(index: int, path: str):
            if index == len(digits):
                result.append(path)  # ★ ここで参照できる
                return
            for char in mapping[digits[index]]:
                backtrack(index + 1, path + char)
        
        backtrack(0, "")
        return result

solution = Solution()
print(solution.letterCombinations("23"))
print(solution.letterCombinations("23539"))