# 類別class、物件object

class Phone: #class 只是創建的模板
    def __init__(self,os,number,is_waterproof):
        self.os = os
        self.number = number
        self.is_waterproof = is_waterproof

    def is_ios(self):
        if self.os == "ios":
            return True
        else:
            return False

    def add(self,number1,number2):
        return number1 + number2   




phone1 = Phone("ios",123,True)
print(phone1.os)
print(phone1.number)
print(phone1.is_waterproof)
print(phone1.is_ios())
print(phone1.add(5,6))

# phone2 = Phone("android",456,False)
# print(phone2.os)
# print(phone2.number)
# print(phone2.is_waterproof)