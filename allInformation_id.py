'''
作用：通过id获取所有的数据信息
版本：21/5/14修改了原来的部分,行头整理完毕
'''
import pandas as pd
import numpy as np
from pymatgen.ext.matproj import MPRester
import csv

# path = r'D:\机器学习--孙老师\data\5.12\Ti+Cr\12.csv'
# data = pd.read_csv(path)
# print(type(data))
# data=data.values
# data_num=data.shape[0]#id的个数
# data=data.tolist()#二维数组转一维数组
# data_id=[]
# for i in range(0,data_num):#data.shape[0]
#     data_id.append(data[i])
# data_id=list(np.array(data_id).flatten())#转化为一维数组
# #print(data_id)
# x=[]
# print("开始注册！")
# with MPRester("K5JtfUOhunkvFWgT") as m:
#     print('注册成功，开始执行！')
#     for i in range(0,data_num):#ata_num
#         result = m.get_data(data_id[i])
#         result.insert(0,data_id[i])
#         #print(result)
#         x.append(result)
#         if i%100==0:
#             print('已经处理数据：',i)
#     print('任务结束！')
#
#
# with open('D:/机器学习--孙老师/data/5.12/Ti+Cr/cr.csv', 'w', newline='') as csvfile:
#     writer  = csv.writer(csvfile)
#     for row in x:
#         writer.writerow(row)



path = r'D:\机器学习--孙老师\data\5.12\Ti+Cr\Ti+Mo.csv'
data = pd.read_csv(path)
# print(type(data))
data = data.values
data_num = data.shape[0]#id的个数
data = data.tolist()#二维数组转一维数组
data_id = []
for i in range(0, data_num):#data.shape[0]
    data_id.append(data[i])
data_id = list(np.array(data_id).flatten())#转化为一维数组
#print(data_id)
x = []
print("开始注册！")
with MPRester("K5JtfUOhunkvFWgT") as m:
    print('注册成功，开始执行！')
    num_count = 0  # 数据条目个数
    for i in range(0, data_num):#ata_num
        result = m.get_data(data_id[i])
        result.insert(0, data_id[i])

        # 设置表头,此时result[0]里面的从文件中读的id,result[1]才是dict
        if i == 0:
            hang = []
            for key in result[1].keys():
                hang.insert(0, key)
            x.append(hang)  # 设置表头

        # 只要数据,此时result[0]里面的从文件中读的id,result[1]才是dict
        temp = []
        for key, value in result[1].items():
            # temp.insert(0, key)
            temp.insert(0, value)
        x.append(temp)
        temp = []

        if i% 100 == 0:
            print('已经处理数据：', i)
        num_count = i
    print("该任务总共打印数据:", num_count)
    print('任务结束！')


with open('D:/机器学习--孙老师/data/5.12/Ti+Cr/try2.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for row in x:
        writer.writerow(row)