# 檔案的讀取、寫入

# open("檔案路徑", mode = "開啟模式")
#絕對路徑 EX：D:/Python Practice/newworld/12321.txt
#相對路徑 以程式的位置做延伸 EX：12321.txt，等於是從程式在的位置出發，前面的部分程式會自己填寫

# mode = "r"   讀取
# mode = "w"   覆寫
# mode = "a"   在原先的資料後寫東西

# file = open("12321.txt", mode = "r")
# #print(file.read())  #read 是讀取全部的內容
# #print(file.readline())  #readline 是讀取一行的內容
# # print(file.readlines())  #readlines 是把內容放到列表裡

# # for line in file:   #利用 for 迴圈，讀取每一行
# #     print(line)

# file.close()        #close關閉檔案

# print("----------------我是分隔線1----------------")


# file = open("12321.txt", mode = "w")
# file.write("hello")
# file.close()

# print("----------------我是分隔線2----------------")

# file = open("12321.txt", mode = "a", encoding = "utf-8")    
# #一般的開啟芳是不支援中文輸入，需要新增參數，utf-8支援為中文
# file.write("\n你好")
# file.close()


with open("12321.txt", mode = "a", encoding = "utf-8") as file: #用with的寫法，不用加close，程式會自動關閉檔案
    file.write("\nhaha")
