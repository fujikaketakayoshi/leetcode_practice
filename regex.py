import re
str = 'abcdef'
regex = 'a.e'  # .は任意の1文字、*は0回以上の繰り返し

if re.search(regex, str):
    print("マッチしました")
else:
    print("マッチしませんでした")

