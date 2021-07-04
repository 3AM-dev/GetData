import pandas as pd
import numpy as np
from pymatgen.ext.matproj import MPRester
import csv

path = r'D:\机器学习--孙老师\data\mp-ids-3402.csv'
data = pd.read_csv(path)
print(type(data))
data=data.values
data_num=data.shape[0]#id的个数
data=data.tolist()#二维数组转一维数组
data_id=[]
for i in range(0,data_num):#data.shape[0]
    data_id.append(data[i])
data_id=list(np.array(data_id).flatten())#转化为一维数组
#print(data_id)
x=[]
with MPRester("qgUvC7OLy8Pam1oT") as m:
    print('注册成功，开始执行！')
    for i in range(0,data_num):#ata_num
        result = m.get_data(data_id[i])
        result.insert(0,data_id[i])
        #print(result)
        x.append(result)
        if i%100==0:
            print('已经处理数据：',i)
    print('任务结束！')


with open('D:/机器学习--孙老师/data/result1.csv', 'w', newline='') as csvfile:
    writer  = csv.writer(csvfile)
    for row in x:
        writer.writerow(row)

# x_data.shape = -1, 1 # 将x_data调整为（任意行，1列）