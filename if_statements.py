# if判斷句

score = 59
if score == 100:
    print("獲得1000元")
elif score >= 80:
    print("獲得500元")
elif score >=60:
    print("獲得100元")
else:
    print("損失300元")

print("----------------我是分隔線1----------------")

score2 = 100
rainy = True
if score2 == 100 and rainy:
    print("獲得1000元")
else:
    print("損失500元")

print("----------------我是分隔線2----------------")

score3 = 99
rainy2 = True
if score3 == 100 or rainy2:
    print("獲得1000元")
else:
    print("損失500元")

print("----------------我是分隔線3----------------")

score4 = 99
rainy3 = False
if score4 == 100 or not rainy3:
    print("獲得1000元")
else:
    print("損失500元")

# !=，為不等於

print("----------------我是分隔線4----------------")

def max_num(num1,num2,num3):
    if num1>=num2 and num1 >= num3:
        return num1
    elif num2>=num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(26,87,14))




