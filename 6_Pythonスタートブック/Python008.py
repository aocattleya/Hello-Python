# coding: utf-8


# for文でリストの中身を一括表示
list_tohoku = [5349, 5478, 5344, 4644, 4968, 6259]
list_shikoku = [3148, 2991, 2966, 2457]

for val in list_tohoku:     # valは変数なので何でも良い
    print(val)

avg_tohoku = 0

for val in list_tohoku:
    avg_tohoku += val

avg_tohoku /= len(list_tohoku)
print(avg_tohoku)