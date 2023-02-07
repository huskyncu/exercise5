import insert
import query
import os
while True:
    choice =int(input("(1)新增病患資料(2)查詢病患資料(3)結束程式："))
    if choice ==1:
        name = input("請輸入病患的姓名：") 
        nid = input("請輸入病患的身分證字號：") 
        age = input("請輸入病患的年紀：")
        height = input("請輸入病患的身高(cm)：")
        weight = input("請輸入病患的體重(kg)：")
        insert.add(name,nid,age,height,weight)
    elif choice==2:
        nid = input("請輸入病患的身分證字號：")
        query.search(nid)
    elif choice==3:
        print("結束程式！")
        break
    else:
        print("無效指令！")
os.system("pause")