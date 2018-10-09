from menu_item import MenuItem

class Food(MenuItem):

    def calorie_info(self):     # 追加
        print(str(self.calorie) + 'kcalです')
