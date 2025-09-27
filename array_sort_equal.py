lst = ['foo', 'bar', 'baz', 'foo']
lst2 = ['foo', 'bar', 'foo', 'baz']
lst3 = ['foo', 'bar', 'baz', 'foo', 'foo']
print(lst == lst2)
print(sorted(lst) == sorted(lst2))
print(sorted(lst) == sorted(lst3))
