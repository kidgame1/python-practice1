# 猜數字遊戲 基本版

input_num = None
num = 100

while input_num != num:
    input_num = int(input("請輸入數字 "))

    if input_num > num:
        print("輸入的數字太大囉, 請繼續努力")

    elif input_num < num:
        print("輸入的數字太小囉, 請繼續努力")

print("恭喜你猜中了")

print("遊戲結束")



