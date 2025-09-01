num = 100
mod = num % 3
if mod == 0:
    print(f"{num}は3の倍数です")
elif mod == 1:
    print(f"{num}を3で割った余りは1です")
else:
    print(f"{num}を3で割った余りは2です")