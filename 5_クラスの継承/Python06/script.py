# super()

from food import Food
from drink import Drink

food1 = Food('サンドイッチ', 500, 330)
print(food1.info())

drink1 = Drink('コーヒー', 300, 180)

# 以下の1行は削除
# drink1.amount = 180

print(drink1.info())

# オーバーライドしたメソッドの中で「super()」とすることで、
# 親クラスを呼び出すことが出来る。

# また、下の図のように「super().メソッド名()」とすることで、
# 親クラス内に定義されたインスタンスメソッドをそのまま利用することが可能。
