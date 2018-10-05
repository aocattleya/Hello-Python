# インスタンスのリスト

from Python16item import MenuItem

menu_item1 = MenuItem('サンドイッチ', 500)
menu_item2 = MenuItem('チョコケーキ', 400)
menu_item3 = MenuItem('コーヒー', 300)
menu_item4 = MenuItem('オレンジジュース', 200)

menu_items = [menu_item1, menu_item2, menu_item3, menu_item4]

# for文を用いて1つづつメニューを出力
for Python16item in menu_items:
    print(Python16item.info())

# サンドイッチ: ¥500
# チョコケーキ: ¥400
# コーヒー: ¥300
# オレンジジュース: ¥200
