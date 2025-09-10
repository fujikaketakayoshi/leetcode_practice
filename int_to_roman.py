def intToRoman(num: int) -> str:
    s = ''
    first = num % 10
    if 1 <= first <= 3:
        s += 'I' * first
    elif first == 4:
        s += 'IV'
    elif first == 5:
        s += 'V'
    elif 6 <= first <= 8:
        s += 'V' + 'I' * (first % 5)
    elif first == 9:
        s += 'IX' + s
    num = num // 10
    second = num % 10
    if 1 <= second <= 3:
        s = 'X' * second + s
    elif second == 4:
        s = 'XL' + s
    elif second == 5:
        s = 'L' + s
    elif 6 <= second <= 8:
        s = 'L' + 'X' * (second % 5) + s
    elif second == 9:
        s = 'XC' + s
    num = num // 10
    third = num % 10
    if 1 <= third <= 3:
        s = 'C' * third + s
    elif third == 4:
        s = 'CD' + s
    elif third == 5:
        s = 'D' + s
    elif 6 <= third <= 8:
        s = 'D' + 'C' * (third % 5) + s
    elif third == 9:
        s = 'CM' + s
    num = num // 10
    forth = num % 10
    if 1 <= forth <= 3:
        s = 'M' * forth + s
    return s

print(intToRoman(3))
print(intToRoman(496))
print(intToRoman(1994))

