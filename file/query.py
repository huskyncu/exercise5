#查詢身份證字號
import os
def search(nid):
  if os.path.exists(nid+'.txt'):
    with open(nid+".txt", mode='r') as patient_file:
      name = patient_file.readline()
      nid = patient_file.readline()
      age = patient_file.readline()
      height = patient_file.readline()
      weight = patient_file.readline()
      print(nid + "電子健康檔案如下：")
      print("姓名：" + name.replace('\n',''))
      print("年紀：" + age.replace('\n',''))
      print("身高：" + height.replace('\n',''))
      print("體重：" + weight.replace('\n','')) 
  else: 
    print("找不到檔案!請重新輸入!")