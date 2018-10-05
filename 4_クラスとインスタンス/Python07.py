# クラスの中で定義したメソッドを呼び出す

class MenuItem:
    def hello(self):
        print('こんにちは！')

menu_item1 = MenuItem()

menu_item.hello()      # 結果：こんにちは！
