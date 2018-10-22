# coding: utf-8


list_int = [0,1,2,3]
print(list_int)

list_mix = [2,1.732,'test']
print(list_mix)

print(list_mix[0])
print(len(list_int))
print(len(list_mix))

# 要素の変更
list_int[0] = -1
print(list_int)

# リストに新しい要素を追加する
list_int.append(4)
print(list_int)

# 要素の削除
list_int.pop(1)
print(list_int)

# リストの連結と拡張
print(list_int + list_mix)

# リストの連結と拡張（extend）
list_int.extend(list_mix)
print(list_int)