# coding: UTF-8
# 条件分岐

apple_price = 200

money = 1000

input_count = input('購入するリンゴの個数を入力してください')
count = int(input_count)
total_price = apple_price * input_count
print('購入するリンゴの個数は' + str(count) + '個です')
print('支払い金額は' + str(total_price) + '円です')

if money > total_price:
    print('リンゴを' + str(count) + '個買いました')
    print('残高は' + str(money - total_price) + '円です')
elif money == total_price:
    print('リンゴ' + str(count) + '個買いました')
    print('財布が空になりました')
else:
    print('お金が足りません')
    print('リンゴを買えませんでした')
