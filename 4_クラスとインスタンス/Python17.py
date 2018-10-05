# 繰り返し処理で番号をつける

lessons = ['Python', 'Ruby', 'jaba']
index = 0
for lesson in lessons:
    print(str(index) + '.' + lesson)
    index += 1  # 1を足す

# 結果
# 0.Python
# 1.Ruby
# 2.jaba
