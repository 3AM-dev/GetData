'''
每行显示flag_num个数据
'''
import pandas as pd
import csv
import numpy as np

df = pd.read_csv(r"D:\机器学习--孙老师\data\3.22-1.csv")
data = df.values  # data是数组，直接从文件读出来的数据格式是数组
index1 = list(df.keys())  # 获取原有csv文件的标题，并形成列表
data = list(map(list, zip(*data)))  # map()可以单独列出列表，将数组转换成列表
#print('a',type(data))
data = pd.DataFrame(data, index=index1)  # 将data的行列转换
# print(type(data))
# print(data)
id_num=data.shape[1]#id个数
data=list(np.array(data).flatten())#转化为一维数组
print(data)
print(type(data))
flag_num=10  # 这是每行需要显示的数据个数
y=[]
a=0
b=a+flag_num
while data[a:b]!=[]:
    y.append(data[a:b])#放进二维数组，这样方便后面打进csv
    a=b;
    b=a+flag_num
#print(y)
#data.to_csv(r'D:\机器学习--孙老师\data\1.csv', header=0)
#y.to_csv(r'D:\机器学习--孙老师\data\1.csv', header=0)
with open('D:/机器学习--孙老师/data/3.22change.csv', 'w', newline='') as csvfile:
    writer  = csv.writer(csvfile)
    for row in y:
        writer.writerow(row)




