#直接批量获取cif文件
import csv
import os
import pandas as pd
import numpy as np
from pymatgen.ext.matproj import MPRester
path = r'D:\机器学习--孙老师\data\my_try\Ti+Nb/'
x=[]
temp=[]
with MPRester("qgUvC7OLy8Pam1oT") as m:
    print('注册成功，开始执行！')
    data = m.query(criteria={"elements": {"$all": ["Ti", "Nb"]}},
                   properties=["cif", "pretty_formula", "formation_energy_per_atom", "elasticity", "material_id"])

    # 通过参数设置得到不同的需要
    # data = m.query(criteria={"material_id": "mp-30882"},
    #                properties=["pretty_formula", "spacegroup.symbol"])
    for i in range(0, len(data)):
        for key, value in data[i].items():
            temp.insert(0, key)
            temp.insert(1, value)
        x.append(temp)
        temp = []
        # print(data)
    print('数据获取结束！')


for row in x:
    with open(path+row[row.index('material_id')+1]+'.cif', 'w') as file:
         file. write(row[row.index('cif')+1])


with open('D:/机器学习--孙老师/data/my_try/Ti+Nb/Ti+Nb.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for row in x:
        writer.writerow(row)











#row=['material_id', 'mp-1217914', 'elasticity', None, 'formation_energy_per_atom', -1.5128505145233344, 'pretty_formula', 'TaTiN2', 'cif', "# generated using pymatgen\ndata_TaTiN2\n_symmetry_space_group_name_H-M   'P 1'\n_cell_length_a   3.07713800\n_cell_length_b   3.07713800\n_cell_length_c   4.33434200\n_cell_angle_alpha   90.00000000\n_cell_angle_beta   90.00000000\n_cell_angle_gamma   90.00000000\n_symmetry_Int_Tables_number   1\n_chemical_formula_structural   TaTiN2\n_chemical_formula_sum   'Ta1 Ti1 N2'\n_cell_volume   41.04092335\n_cell_formula_units_Z   1\nloop_\n _symmetry_equiv_pos_site_id\n _symmetry_equiv_pos_as_xyz\n  1  'x, y, z'\nloop_\n _atom_site_type_symbol\n _atom_site_label\n _atom_site_symmetry_multiplicity\n _atom_site_fract_x\n _atom_site_fract_y\n _atom_site_fract_z\n _atom_site_occupancy\n  Ta  Ta0  1  0.00000000  0.00000000  0.00000000  1\n  Ti  Ti1  1  0.50000000  0.50000000  0.50000000  1\n  N  N2  1  0.00000000  0.00000000  0.50000000  1\n  N  N3  1  0.50000000  0.50000000  0.00000000  1\n"]
# print(x.index('material_id'),':',x[x.index('material_id')+1])
# print(type(x[x.index('material_id')+1]))
# print(x.index('cif'),':',x[x.index('cif')+1])


# import os
# path = r'D:\机器学习--孙老师\data\my_try/'
# f = os.listdir(path)
# h=0
# for i in f:
#     oldname = path+i
#     newname = path+str(h)+'.cif'
#     os.rename(oldname,newname)
#     h=h+1
#     #print(i)

# h=0
# for i in range(0,5):
#     with open(path+'test'+str(h)+'.txt','w') as file:
#         file.write(str(i))
#         h=h+1





