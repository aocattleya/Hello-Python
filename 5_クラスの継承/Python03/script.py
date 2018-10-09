# 子クラスのインスタンスメソッド

from food import Food
from drink import Drink

food1 = Food('サンドイッチ', 500)

food1.calorie = 330

food1.calorie_info()

# Foodクラス内に「calorie_info」メソッドを追加
# 子クラスは「親クラス内に定義されているメソッド」と
#「独自に定義したメソッド」の両方が使える。

# また、親クラスでは子クラスのメソッドは使えない
