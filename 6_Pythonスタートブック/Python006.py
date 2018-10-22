# coding: utf-8


# その他の入れ物
# タプル（tuple）要素の追加や削除ができないリスト
tuple_test = (1,2,3,'100yen')
print(tuple_test)

# 追加や削除は出来ないが、添え字を使って中身にアクセスは出来る
print(tuple_test[3])

# 一部を切り出す操作も可能
tuple_test[0:3]
print(tuple_test)

# 長さが1のタプルを作る場合は、最後に「,」が必要
tuple_one = (1,)
print(tuple_one)

# タプルからリストを作る
# 追加や削除が出来ない為、必要になった場合は必要になる
print(list(tuple_test))