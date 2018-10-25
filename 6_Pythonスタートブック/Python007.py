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

# セット内の要素を削除したい時はremove
test_set.remove(3)
print(test_set)

# リストを元にセットを作る
from_list = set([1, 2, 3])
# ファイル実行だとなんか上手く行かない