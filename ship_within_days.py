def can_ship(weights, days, capacity):
    # capacity で荷物を運んで days 日以内に終わるか判定
    day_count = 1
    current = 0
    for w in weights:
        if current + w > capacity:
            day_count += 1
            current = 0
        current += w
    return day_count <= days

def ship_within_days(weights, days):
    l, r = max(weights), sum(weights)  # 最小の積載量〜最大の積載量
    while l < r:
        mid = (l + r) // 2
        print(l, r, mid)
        if can_ship(weights, days, mid):
            r = mid  # 条件を満たす → もっと小さい容量があるかも
        else:
            l = mid + 1  # 条件を満たさない → もっと大きく
    return l

weights = [1,2,3,4,5,6,7,8,9,10]
days = 2
print(ship_within_days(weights, days))  # 15
