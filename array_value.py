arr = [1,2,3,1]

indexes = [i for i, v in enumerate(arr) if v == 1]
print(indexes)  # [0, 3]
