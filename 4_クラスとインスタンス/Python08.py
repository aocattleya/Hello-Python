# インスタンスメソッドのself

class MenuItem:
    def info(self):
        print(self.name)    # menu_item1が代入されている

menu_item1 = MenuItem()
menu_item1.name = 'サンドイッチ'

menu_item1.info()

# 結果：サンドイッチ
