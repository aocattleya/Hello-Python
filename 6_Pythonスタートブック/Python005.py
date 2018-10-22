# coding: utf-8


# 辞書型
country_code = {1:'America',39:'Italia',86:'China'}
print(country_code[39])

# inで存在するかを調べる
print(81 in country_code)   # False
print(39 in country_code)   # True

# 要素の追加
country_code[81] = 'Japan'
print(country_code)

# 要素の変更
country_code[81] = 'Nippon'
print(country_code)

# 指定されたキーとそれに関連付けられた値を削除
country_code.pop(1)   # popメソッド
print(country_code)