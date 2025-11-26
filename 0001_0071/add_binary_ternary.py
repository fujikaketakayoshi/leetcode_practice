def add_base(a: str, b: str, base: int) -> str:
    i, j = len(a) - 1, len(b) - 1
    carry = 0
    result = []

    while i >= 0 or j >= 0 or carry:
        da = int(a[i]) if i >= 0 else 0
        db = int(b[j]) if j >= 0 else 0
        s = da + db + carry
        result.append(str(s % base))
        carry = s // base
        i -= 1
        j -= 1

    return ''.join(reversed(result))

print(add_base("1010", "1011", 2))  # Output: "10101"
print(add_base("102", "21", 3))     # Output: "200"
print(add_base("0", "0", 2))        # Output: "0"
print(add_base("222", "111", 3))    # Output: "1110