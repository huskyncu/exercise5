#輸入個人資料
def add(name,nid,age,height,weight):
    #開啟檔案，寫入內容
    with open(nid+".txt", mode='w') as patient_file:
        patient_file.write(name + "\n"+nid + "\n"+age + "\n"+height + "\n"+weight + "\n")
        print("成功新增"+name+"的檔案！")

#改良：你也可以將檔案集中在一個資料夾下
#你可以在本資料夾開一個Patients的子資料夾，用來存放個人檔案
#檔名可以寫 "Patients\\身分證字號.txt"（Windows）或 "Patients/身分證字號.txt"(Mac)