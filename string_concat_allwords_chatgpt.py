from collections import Counter
from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        
        word_len = len(words[0])
        words_len = len(words)
        total_len = word_len * words_len
        n = len(s)

        words_counter = Counter(words)
        results = []

        for i in range(word_len):  # ← スライド開始位置をずらす（重要）
            left = i
            right = i
            window_counter = Counter()
            count = 0  # 現在windowに含まれる単語数

            while right + word_len <= n:
                word = s[right:right + word_len]
                right += word_len
                if word in words_counter:
                    window_counter[word] += 1
                    count += 1
                    # 出現回数が多すぎたら左を動かして調整
                    while window_counter[word] > words_counter[word]:
                        left_word = s[left:left + word_len]
                        window_counter[left_word] -= 1
                        left += word_len
                        count -= 1
                    if count == words_len:
                        results.append(left)
                else:
                    # 不要な単語が出てきたらリセット
                    window_counter.clear()
                    count = 0
                    left = right

        return results
Solution = Solution()
print(Solution.findSubstring("barfoothefoobarman", ["foo","bar"]))
print(Solution.findSubstring("wordgoodgoodgoodbestword", ["word","good","best","word"]))
print(Solution.findSubstring("barfoofoobarthefoobarman", ["bar","foo","the"]))
