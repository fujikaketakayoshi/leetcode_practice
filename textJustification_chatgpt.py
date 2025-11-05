class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        lines = []
        line = []
        width = 0
        
        # 行分割
        for word in words:
            if width + len(word) + len(line) > maxWidth:
                lines.append(line)
                line = [word]
                width = len(word)
            else:
                line.append(word)
                width += len(word)
        lines.append(line)
        
        results = []
        for i, line in enumerate(lines):
            # 最終行は左寄せ
            if i == len(lines) - 1:
                str_line = ' '.join(line)
                str_line += ' ' * (maxWidth - len(str_line))
                results.append(str_line)
                continue

            space_num = len(line) - 1
            space_total_len = maxWidth - sum(len(word) for word in line)
            
            if space_num == 0:
                # 単語1つの行
                str_line = line[0] + ' ' * (maxWidth - len(line[0]))
            else:
                shou, amari = divmod(space_total_len, space_num)
                spaces = [' ' * (shou + 1)] * amari + [' ' * shou] * (space_num - amari)
                str_line = ''.join(word + spaces[j] for j, word in enumerate(line[:-1])) + line[-1]
            
            results.append(str_line)
        
        return results
solution = Solution()
print(solution.fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16))
print(solution.fullJustify(["What","must","be","acknowledgment","shall","be"], 16))
print(solution.fullJustify(["Science","is","what","we","understand","well","enough","to","explain",
"to","a","computer.","Art","is","everything","else","we","do"], 20))
