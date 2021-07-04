#https://github.com/materialsproject/mapidoc/blob/master/example_notebooks/Using%20the%20Materials%20API%20with%20Python.ipynb
'''
文件说明：
   该py文件通过是通过筛选条件从MP中获取数据
   criteria = '{"elements":{"$in":["Li", "Na", "K"], "$all": ["O"]}, "nelements":2}' #元素种类为2,前面三种金属的氧化物
   criteria={"elements": {"$all": ["Ti", "Ta"], "$nin": ["O", "C"]}}  # 所有含有Ti Ta 但是不含有O C的
supported_properties = (
        "energy",
        "energy_per_atom",
        "volume",
        "formation_energy_per_atom",
        "nsites",
        "unit_cell_formula",
        "pretty_formula",
        "is_hubbard",
        "elements",
        "nelements",
        "e_above_hull",
        "hubbards",
        "is_compatible",
        "spacegroup",
        "task_ids",
        "band_gap",
        "density",
        "icsd_id",
        "icsd_ids",
        "cif",
        "total_magnetization",
        "material_id",
        "oxide_type",
        "tags",
        "elasticity",这里
    )

输出：properties中的参数倒序输出

'''
import pandas as pd
import numpy as np
from pymatgen.ext.matproj import MPRester
import csv

def getInformation(keyMP, path,fileName):
    x=[]
    temp=[]
    cif1=[]
    cif2=[]
    print('开始注册MP！！！')
    with MPRester(keyMP) as m:
        print('注册成功，开始执行！')
        data = m.query(criteria={"elements": {"$all": ["Ti", "Nb"]}, "nelements":2}, #,
                       properties=[
                                    # "elasticity.G_Reuss",
                                    # "elasticity.G_VRH",
                                    # "elasticity.G_Voigt",
                                    # "elasticity.G_Voigt_Reuss_Hill",
                                    # "elasticity.K_Reuss",
                                    # "elasticity.K_VRH",
                                    # "elasticity.K_Voigt",
                                    # "elasticity.K_Voigt_Reuss_Hill",
                                   "material_id",
                                   "pretty_formula",
                                   "energy",
                                   "energy_per_atom",
                                   "volume",
                                   "formation_energy_per_atom",
                                   "nsites",
                                   "unit_cell_formula",
                                   "is_hubbard",
                                   "elements",
                                   "nelements",
                                   "e_above_hull",
                                   "hubbards",
                                   "is_compatible",
                                   "spacegroup",
                                   "task_ids",
                                   "band_gap",
                                   "density",
                                   "icsd_id",
                                   "icsd_ids",
                                   "cif",
                                   "total_magnetization",
                                   "oxide_type",
                                   "tags",
                           "elasticity.G_Reuss",
                           "elasticity.G_VRH",
                           "elasticity.G_Voigt",
                           "elasticity.G_Voigt_Reuss_Hill",
                           "elasticity.K_Reuss",
                           "elasticity.K_VRH",
                           "elasticity.K_Voigt",
                           "elasticity.K_Voigt_Reuss_Hill",
                           "elasticity.elastic_anisotropy",
                           "elasticity.elastic_tensor",
                           "elasticity.homogeneous_poisson",
                           "elasticity.poisson_ratio",
                           "elasticity.universal_anisotropy",
                           "elasticity.elastic_tensor_original",
                           "elasticity.compliance_tensor",
                           "elasticity.warnings",
                           "elasticity.nsites"
                                    ]
                       )
        # 获取上面所有的数据，保存在csv中
        hang = []  # 表头
        for key in data[0].keys():
            hang.insert(0,key)
        x.append(hang)  # 设置表头
        for i in range(0, len(data)):
            for key, value in data[i].items():
                #temp.insert(0, key)
                temp.insert(0, value)
            x.append(temp)
            temp = []
            # print(data)
        print('csv文件创建结束！')

        # 获取上面数据的一部分，用来构造cif文件
        for i in range(0, len(data)):
            for key, value in data[i].items():
                cif1.insert(0, key)
                cif1.insert(1, value)
            cif2.append(cif1)
            cif1 = []
        print('cif构造结束！')

    with open(path+fileName, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for row in x:
            # 所有数据逆序，因此写进文件之前需要逆序回来
            row.reverse()
            writer.writerow(row)

    for row in cif2:
        with open(path + row[row.index('material_id') + 1] + '.cif', 'w') as file:
            file.write(row[row.index('cif') + 1])


if __name__ == '__main__':
    path = r'D:\机器学习--孙老师\data\data\111/'
    keyMP = "K5JtfUOhunkvFWgT"
    fileName = 'try.csv'
    # 筛选条件以及信息太多，在主函数中添加
    getInformation(keyMP, path, fileName)


# x=[]
# temp=[]
# with MPRester("VNZxHJh7rSbOKaMl") as m:
#     print('注册成功，开始执行！')
#     data = m.query(criteria={"elements": {"$all": ["Ti", "Ta"], "$nin": ["O", "C"]}},
#                    properties=["cif", "pretty_formula", "formation_energy_per_atom", "elasticity","material_id"])
#     # 通过参数设置得到不同的需要
#     # data = m.query(criteria={"material_id": "mp-30882"},
#     #                properties=["pretty_formula", "spacegroup.symbol"])
#     for i in range(0, len(data)):
#         for key, value in data[i].items():
#             temp.insert(0, key)
#             temp.insert(1, value)
#         x.append(temp)
#         temp = []
#         # print(data)
#     print('任务结束！')
#
#
# with open('D:/机器学习--孙老师/data/Ti+Ta(oc).csv', 'w', newline='') as csvfile:
#     writer = csv.writer(csvfile)
#     for row in x:
#         writer.writerow(row)






