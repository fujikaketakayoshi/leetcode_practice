class Solution:
    def palindromePairs(self, words: list[str]) -> list[list[int]]:
        def is_palindrome(s: str) -> bool:
            return s == s[::-1]

        # 単語 -> index
        mp = {word: i for i, word in enumerate(words)}

        ans = []

        for i, word in enumerate(words):
            m = len(word)

            # 全ての切れ目を試す
            for cut in range(m + 1):
                left = word[:cut]
                right = word[cut:]

                # left が回文なら reverse(right) を前に付けられる
                if is_palindrome(left):
                    rev = right[::-1]
                    if rev in mp and mp[rev] != i:
                        ans.append([mp[rev], i])

                # right が回文なら reverse(left) を後ろに付けられる
                # cut == m のときは空文字との重複を避ける
                if cut != m and is_palindrome(right):
                    rev = left[::-1]
                    if rev in mp and mp[rev] != i:
                        ans.append([i, mp[rev]])

        return ans