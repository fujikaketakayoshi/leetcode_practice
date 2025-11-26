def myAtoi(s: str) -> int:
    tmp = ''
    s = s.replace(' ', '')
    sign = 1
    if s == '':
        return 0
    if s[0] == '-':
        sign = -1
        s = s[1:]
    elif s[0] == '+':
        sign = 1
        s = s[1:]
    for ch in s:
        if ch == '0' and tmp == '':
            continue
        elif ch == '0':
            break
        elif ch.isdigit():
            tmp += ch
        else:
            break
    result = sign * int(tmp if tmp != '' else 0)
    if result < -2 ** 31:
        result = -2 ** 31
    elif result > 2 ** 31 -1:
        result = 2 ** 31 -1
    return result

print(myAtoi('-+12'))
