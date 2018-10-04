# 引数の初期値

def hello(name, message = 'こんにちは'):

    print(name + 'さん、' + message)

hello('John', 'こんばんは')
hello('Kate')

# 結果
# Johnさん、こんばんは
# Kateさん、こんにちは

# 1だけの場合は、"こんにちは"が入る
