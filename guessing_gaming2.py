# 猜數字遊戲 次數限定版

input_num = None
num = 100
guess_count = 0
guess_limit = 3
out_of_limit = False

while input_num != num and not(out_of_limit):
    guess_count += 1
    if guess_count <= guess_limit:
        input_num = int(input("請輸入數字 "))
        if input_num > num:
            print("輸入的數字太大囉, 請繼續努力")

        elif input_num < num:
            print("輸入的數字太小囉, 請繼續努力")

    else:
        out_of_limit = True

if out_of_limit:
    print("還差地遠呢")
else:
    print("恭喜你猜中了")

print("遊戲結束")


