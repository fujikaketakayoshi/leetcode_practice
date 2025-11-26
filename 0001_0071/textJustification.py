class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        width = 0
        lines = []
        line = []
        for word in words:
            width += len(word)
            if width + len(line) > maxWidth:
                lines.append(line)
                line = [word]
                width = len(word)
            else:
                line.append(word)
        lines.append(line)
        
        results = []
        for i, line in enumerate(lines):
            str_line = ''
            space_num = len(line) - 1
            space_total_len = maxWidth - sum(len(word) for word in line)
            spaces = []
            if space_num == 0:
                spaces = [' ' * (maxWidth - len(line[0]))]
            elif i == len(lines) - 1:
                spaces = [' ' for _ in range(space_num)] + [' ' * (space_total_len - space_num)]
            else:
                shou, amari = divmod(space_total_len, space_num)
                if amari == 0:
                    spaces = [' ' * shou for _ in range(space_num)]
                else:
                    spaces = [' ' * (shou + 1)] * amari + [' ' * shou] * (space_num - amari)
            if len(line) - 1 == len(spaces):
                spaces.append('')
            # print(line, spaces)
            for j, word in enumerate(line):
                str_line += word + spaces[j]
            results.append(str_line)

        return results

solution = Solution()
print(solution.fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16))
print(solution.fullJustify(["What","must","be","acknowledgment","shall","be"], 16))
print(solution.fullJustify(["Science","is","what","we","understand","well","enough","to","explain",
"to","a","computer.","Art","is","everything","else","we","do"], 20))