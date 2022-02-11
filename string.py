#如何使用字串、字串的用法
# \n 代表換行
print("Hello \n Fan")

# \" 就可以在字串中加入 "
print("Hello \" Fan")

phrase = "Hello Fan"
phrase_upper = "HELLO FAN"
phrase_lower = "hello fan"

# lower：將字串裡的字母變為小寫，用法 字串.lower()
print(phrase.lower())

# upper：將字串裡的字母變為大寫，用法 字串.upper()
print(phrase.upper())

# isupper：判斷串裡的字母是否大寫，用法 字串.isupper()
# islower：判斷串裡的字母是否大寫，用法 字串.islower()
print(phrase.isupper())
print(phrase_upper.isupper())
print(phrase.islower())
print(phrase_lower.islower())

# 函式可以疊加
print(phrase.lower().islower())
print(phrase.lower().isupper())


phrase_abc = "abcdefg"
# []中括號，裡面放數字，回傳值為數字對應的位置的值
print(phrase_abc[3]) #回傳值應為d，從0開始數

# index：用來尋找字串中的某個字的位址，只會找到最前面的那個字，用法 字串.index()
print(phrase_abc.index("f")) #回傳值應為5

#replace：替換字串裡面的字，替換會字串裡符合條件的全都替換掉，用法 字串.replace(,)
print(phrase_abc.replace("a","A"))