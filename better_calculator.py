# 建立一個計算機

num1 = float(input("請輸入第一個數： "))  #因為 input 的輸入預設為字串，所以要進行轉換
op   = input("請輸入運算符號： ")
num2 = float(input("請輸入第二個數： "))


if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
else:
    print("輸入錯誤")