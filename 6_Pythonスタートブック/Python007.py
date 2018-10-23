# coding: utf-8


# 空のsetを作る
test_set = set()
print(test_set)

# setに要素を追加する
test_set.add(1)
test_set.add(2)
test_set.add(3)
print(test_set)

# 同じテータは、最大で1つしか保持されない
test_set.add(3)
print(test_set)

# 値がsetに入っているかはinで確認
print(1 in test_set)
print(10 in test_set)