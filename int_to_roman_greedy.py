def intToRoman(num: int) -> str:
    val_sym = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"),
        (1, "I")
    ]

    res = []
    for val, sym in val_sym:
        while num >= val:   # 引けるだけ引く
            num -= val
            res.append(sym)
            print(res)
    return "".join(res)

print(intToRoman(3))
print(intToRoman(496))
print(intToRoman(1994))
