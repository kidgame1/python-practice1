# for 迴圈

# for 變數 in 字串 or 列表
#     要重複執行的程式碼

# for letter in "小白你好":
#     print(letter)

# for num in [0,1,2,3,4]:
#     print(num)

# for num in range(100):
#     print(num)

# for num in range(2,7): #印出2,3,4,5,6
#     print(num)


def power(base_num,pow_num):
    result = base_num
    for index in range(pow_num - 1):
        result = result * base_num
    return result

print(power(2,10))