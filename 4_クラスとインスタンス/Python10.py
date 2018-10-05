# インスタンスメソッド（戻り値）

class MenuItem:
    def info(self):
        return self.name + ': ¥' + str(self.price)  # return

menu_item1 = MenuItem()
menu_item1.name = 'サンドイッチ'
menu_item1.price = 500

print(menu_item1.info())    # 出力する

menu_item2 = MenuItem()
menu_item2.name = 'チョコケーキ'
menu_item2.price = 400

print(menu_item2.info())    # 出力する

# 結果
# サンドイッチ: ¥500
# チョコケーキ: ¥400
