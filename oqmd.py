'''
composition: compostion of the materials or phase space, e.g. Al2O3, Fe-O
element_set: the set of elements that the compound must have, '-' for OR, ',' for AND, e.g. (Fe-Mn),O
icsd: whether the structure exists in ICSD, e.g. False, True, F, T
prototype: structure prototype of that compound, e.g. Cu, CsCl
generic: chemical formula abstract, e.g. AB, AB2
spacegroup: the space group of the structure, e.g. Fm-3m
natoms: number of atoms in the supercell, e.g. 2, >5
volume: volume of the supercell, e.g. >10
ntypes: number of elements types in the compound, e.g. 2, <3
stability: hull distance of the compound, e.g. 0, <-0.1,
delta_e: formation energy of that compound, e.g. <-0.5,
band_gap: band gap of the materials, e.g. 0, >2
fields: return subset of fields, e.g. 'name,id,delta_e', '!sites'
filter: customized filters, e.g. 'element_set=O AND ( stability<-0.1 OR delta_e<-0.5 )'
limit: number of data return at once
offset: the offset of data return

Github：https://github.com/mohanliu/qmpy_rester
官网：http://www.oqmd.org/static/docs/restful.html#kw-ref
'''
import qmpy_rester as qr
import csv
'''
判断是否是数字
'''
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False
'''
从数据库获取数据
返回一些的信息，网址等等信息，具体打印list_of_data获取，字典类型
'''
def get_data_OQMD():
    ## Return list of data
    with qr.QMPYRester() as q:
        # ","表示and,"-"表示or,"()"表示一种组合eg: S,(Mn-Fe),O
        kwargs = {
            "element_set": "(Zr-Nb),Ti"      # composition include (Fe OR Mn) AND O
            # "stability": "0",            # hull distance smaller than -0.1 eV
            # "natom": "<10",                  # number of atoms less than 10
            }
        list_of_data = q.get_oqmd_phases(**kwargs)
    return list_of_data
'''
数据处理1
将数据库中的所有信息保存
'''
def data_analysis_1(list_of_data):
    # dict里面的数据，还有标准资源定位符等，不重要
    # 获取所有的数据直接打印 list_of_data
    di = list_of_data['data']
    # 数据缓存列表
    x = []
    # 临时数据缓存
    temp = []
    # 表头
    hang = []
    # 读取第一行数据的key值，作为表头
    # 注意，当符合要求的数据为null时，报error
    for key in di[0].keys():
        hang.insert(0, key)
    # 添加一列数据,这里设置表头
    hang.insert(0, 'delta_e/natoms')
    # 设置表头
    x.append(hang)
    # 第二行开始存储数据
    for i in range(0, len(di)):
        # print(di[i])
        for key, value in di[i].items():
            # 由于表头已设置，只需要读取dict的value
            temp.insert(0, value)
        # 添加手动修改的数据
        temp.insert(0, float(di[i]['delta_e']) / float(di[i]['natoms']))
        # 单行数据添加
        x.append(temp)
        # 单行添加完成，清空，等待下一次添加
        temp = []

    # 文件路径，注意是左斜线
    with open(path + file_name + '.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for row in x:
            # 所有数据逆序，因此写进文件之前需要逆序回来
            row.reverse()
            # 按行读取
            writer.writerow(row)

'''
获取指定类型的数据,POSTCAR???
根据指定格式修改
'''
def postcar(path, list_of_data):
    data=list_of_data['data']
    # 用来存组合name
    file_name=[]
    # 所有数据存储地
    x=[]
    # 每一次遍历数据存储地
    cur_Data = ''
    for i in range(0,len(data)):
        #print(data[i])
        # file_name.append(data[i]['name'])
        # print(data[i]['name'])
        unit_cell = data[i]['unit_cell']
        sites = data[i]['sites']
        # 行
        row = len(unit_cell)
        # 列
        col = len(unit_cell[0])
        # 每一个数据

        # 每个组合的name
        file_name.append(data[i]['name'])
        # 加上名字
        # 第一部分数据unit_cell
        # 首先取name
        cur_Data = cur_Data + data[i]['name'] + '\n' + '1.0' + '\n'
        for i in range(row):
            for j in range(col):
                # print(unit_cell[i][j])
                # 没有无关数据，直接加
                cur_Data = cur_Data + str(unit_cell[i][j]) + ' '
            cur_Data = cur_Data + '\n'
        cur_Data = cur_Data + 'D' + '\n'
        # print(cur_Data)
        # 去除无关项
        sites = str(sites).replace("[", "").replace(",", "").replace("]", "").replace("@", "").replace("'", "")
        # 统计元素出现的个数，这种方法是每个数字都会统计
        result = {word: sites.split().count(word) for word in set(sites.split())}
        # print(result)
        # 统计元素出现次数，也就是非数字
        for key, value in result.items():
            if is_number(key):
                continue
            else:
                cur_Data = cur_Data + str(value) + " "
        cur_Data = cur_Data + "\n"
        # site数据，具有无关项，小心处理
        count = 0
        for word in (sites.split()):
            # 只要数字
            if is_number(word):
                cur_Data = cur_Data + word + " "
                count = count + 1
                # 按列输出
                if count == col:
                    cur_Data = cur_Data + '\n'
                    count = 0
        # print(cur_Data)
        x.append(cur_Data)
        # 清空当前，也就是每一个数据
        cur_Data = ''

    for i in range(0,len(x)):
        # print(file_name[i]) #str
        with open(path + str(i) + '-' + file_name[i]+'.txt', 'w') as file:
            file. write(x[i])

if __name__ == '__main__':
    path = r'D:\机器学习--孙老师\data\611/'
    file_name = 'li4'
    data=get_data_OQMD()
    data_analysis_1(data)
    # postcar(path, data)
    print('this is main')

#list_of_data = q.get_optimade_structures(**kwargs)
# xxx=q.get_calculation_by_id(852599)
# print(xxx)










#
# ## Return list of data
# with qr.QMPYRester() as q:
#     # ","表示and,"-"表示or,"()"表示一种组合eg: S,(Mn-Fe),O
#     kwargs = {
#
#         "element_set": "(Zr-Nb),Ti"      # composition include (Fe OR Mn) AND O
#         # "stability": "0",            # hull distance smaller than -0.1 eV
#         # "natom": "<10",                  # number of atoms less than 10
#         }
#     list_of_data = q.get_oqmd_phases(**kwargs)
#     # dict里面的数据，还有标准资源定位符等，不重要
#     # 获取所有的数据直接打印 list_of_data
#     di = list_of_data['data']
# print(di)
#
# # 数据缓存列表
# x=[]
# # 临时数据缓存
# temp=[]
# # 表头
# hang = []
# # 读取第一行数据的key值，作为表头
# # 注意，当符合要求的数据为null时，报error
# for key in di[0].keys():
#     hang.insert(0,key)
# # 设置表头
# x.append(hang)
# # 第二行开始存储数据
# for i in range(0,len(di)):
#     # print(di[i])
#     for key, value in di[i].items():
#         # 由于表头已设置，只需要读取dict的value
#         temp.insert(0, value)
#     # 单行数据添加
#     x.append(temp)
#     # 单行添加完成，清空，等待下一次添加
#     temp = []
#
#
# # 文件路径，注意是左斜线
# with open('C:/Users/Administrator/Desktop/libo9.csv', 'w', newline='') as csvfile:
#     writer = csv.writer(csvfile)
#     for row in x:
#         # 所有数据逆序，因此写进文件之前需要逆序回来
#         row.reverse()
#         # 按行读取
#         writer.writerow(row)
#
#
#
# #list_of_data = q.get_optimade_structures(**kwargs)
# # xxx=q.get_calculation_by_id(852599)
# # print(xxx)