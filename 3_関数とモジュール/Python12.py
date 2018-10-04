# import
# モジュール "python12utiles"を読み込む

import python12utils

print('じゃんけんを初めます')
player_name = input('名前を入力してください：')
print('何を出しますか？（0: グー, 1: チョキ, 2: パー）')
player_hand = int(input('数字で入力してください：'))

if python12utils.validate(player_hand): # モジュールの使い方
    computer_hand = 1

    if player_name == '':
        python12utils.print_hand(player_hand)
    else:
        python12utils.print_hand(player_hand, player_name)

    python12utils.print_hand(computer_hand, 'コンピュータ')

    result = python12utils.judge(player_hand, computer_hand)
    print('結果は' + result + 'でした')
else:
    print('正しい数値を入力してください')
