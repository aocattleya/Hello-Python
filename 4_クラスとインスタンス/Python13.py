# __init__メソッドでインスタンス変数を扱う

class MenuItem:
    def __init__(self):
        self.name = 'サンドイッチ'
        # インスタンス生成直後に"サンドイッチ"を
        # インスタンス変数nameに代入

menu_item1 = MenuItem()

print(menu_item1.name)

# 結果：サンドイッチ
