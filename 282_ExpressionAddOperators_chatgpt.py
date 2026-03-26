class Solution:
    def addOperators(self, num: str, target: int):
        res = []
        n = len(num)

        def dfs(pos, path, value, last):
            if pos == n:
                if value == target:
                    res.append(path)
                return

            for i in range(pos, n):
                # 先頭0はNG
                if i > pos and num[pos] == '0':
                    break

                cur_str = num[pos:i+1]
                cur = int(cur_str)

                if pos == 0:
                    # 最初はそのまま
                    dfs(i+1, cur_str, cur, cur)
                else:
                    dfs(i+1, path + "+" + cur_str, value + cur, cur)
                    dfs(i+1, path + "-" + cur_str, value - cur, -cur)
                    dfs(i+1, path + "*" + cur_str,
                        value - last + last * cur,
                        last * cur)

        dfs(0, "", 0, 0)
        return res