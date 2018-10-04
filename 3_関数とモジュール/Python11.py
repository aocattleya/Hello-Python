# 複数のreturn

def hello(name = 'ゲスト'):
    if name == 'ゲスト':
        return '名前を教えてください'
    return name + 'さん、ようこそ'

print(hello())

# 結果：名前を教えてください
