# 函式 function

def hello(name,age): #定義函數
    print("hello" + name + "你今年" + age + "歲")


hello("小赤","30")

print("----------------我是分隔線1----------------")

def add(num1,num2):
    print(num1 + num2)
    #如果沒定義 return，那麼python會自動定義為 None

value = add(3,6)
print(value)
