def intToRoman(num: int) -> str:
    thousands = ["", "M", "MM", "MMM"]
    hundreds  = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    tens      = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    ones      = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

    return (
        thousands[num // 1000] +
        hundreds[(num % 1000) // 100] +
        tens[(num % 100) // 10] +
        ones[num % 10]
    )

print(intToRoman(3))
print(intToRoman(496))
print(intToRoman(1994))

