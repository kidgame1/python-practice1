# 列表list用法

from re import T


scores = [50, 70, 30, 40, 80]
friends = ["小赤","小綠","小藍"]
things = [90, "小黑", True]
print(scores)
print(friends)
print(things)
print(scores[-1]) # -1 代表倒數第一位，以此類推
print(scores[0:2]) #表示從第 0 位，取到第 2 位，但不含第 2 位
print(scores[1:4]) #表示從第 1 位，取到第 4 位，但不含第 4 位
print(scores[1:]) #表示從第 1 位，取到最後 1 位
print(scores[:4]) #表示從頭，取到第 4 位，但不含第 4 位

scores[0] = 20 #更改第 0 位的值
print(scores)

print("----------------我是分隔線1----------------")

scores.extend(friends) #將小括號裡的列表，接續在前面的列表，並同時更改前面列表的內容
print(scores)

scores.append(30) #將小括號裡的值，接續在前面的列表
print(scores)

scores.insert(3, 99) #在列表中插入值(也可以插入字串)，逗點前面為位置，逗點後面為值
print(scores)

scores.remove("小赤") #刪除列表中括號裡的值或是字串，且一次只能移除一個
scores.remove("小綠") #刪除列表中括號裡的值或是字串，且一次只能移除一個
scores.remove("小藍") #刪除列表中括號裡的值或是字串，且一次只能移除一個
print(scores)

print("----------------我是分隔線2----------------")

scores.pop() #移除列表中的最後一個值，或字串
print(scores)

scores.sort() #將列表做排列，但列表內容只能有值，不能有字串
print(scores)

scores.reverse() #將列表做反轉
print(scores)

print("----------------我是分隔線3----------------")

scores.insert(3, "小赤") #在列表中插入值(也可以插入字串)，逗點前面為位置，逗點後面為值
print(scores)
scores.insert(5, "小赤") #在列表中插入值(也可以插入字串)，逗點前面為位置，逗點後面為值
print(scores)

print(scores.index("小赤")) #找尋括號裡的值在第幾位，也可以用來找字串，但只會印出第一個找到的

print(scores.count("小赤")) #找尋括號裡的值，在列表中有幾個，也可以用來找字串

scores.clear() #清空列表
print(scores)
