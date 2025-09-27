class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        words_len = len(words)
        word_len = len(words[0])
        words_count = [0] * words_len
        i = 0
        concats = []
        results = []
        while i < len(s):
            if s[i:i + word_len] in words:
                concats.append(s[i:i + word_len])
            if len(concats) == words_len:
                print(concats)
                tmp_concats = concats.copy()
                tmp_words = words.copy()
                tmp_concats.sort()
                tmp_words.sort()
                if tmp_concats == tmp_words:
                    results.append(i - word_len * (words_len - 1))
                    concats = []
            i += word_len
        return results

Solution = Solution()
print(Solution.findSubstring("barfoothefoobarman", ["foo","bar"]))
print(Solution.findSubstring("wordgoodgoodgoodbestword", ["word","good","best","word"]))
print(Solution.findSubstring("barfoofoobarthefoobarman", ["bar","foo","the"])) #正しく出力されない

