# 基本資料型態 & 變數

#字串：單引號或雙引號都 ok，直接引號裡面放字就好了
"安安你好"
'發大財'


#數字：不用引號，直接寫數字就好
70
-87
149.555555


#布林值：用來存放 True or False
True 
False 


#變數
# 1. 變數名稱只能是英文 or 數字 or _ 的組合
# 2. 變數的開頭不可以是數字

name = "Fan"
age = 30
is_male = True
tall = 177

# 字串只能跟字串相加，代表相連；數字跟數字相加，是做運算；字串無法跟數字相加
print("有一個人叫" + name)
print(name + "今年" + age + "歲") #所以這行是錯誤的
print(name + "身高" + tall + "公分") #所以這行是錯誤的
print(name + "想不到已經" + age + "歲了") #所以這行是錯誤的
print(name + age) #所以這行是錯誤的



#在下方輸入 CLS 可以清空結果 for Windows，如果是MAC，用CLEAR