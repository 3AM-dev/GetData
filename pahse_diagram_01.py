# %matplotlib inline # %matplotlib inline这一句是IPython的魔法函数，可以在IPython编译器里直接使用，作用是内嵌画图，省略掉plt.show()这一步，直接显示图像。
# 如果不加这一句的话，我们在画图结束之后需要加上plt.show()才可以显示图像。
'''
https://matgenb.materialsvirtuallab.org/2013/01/01/Plotting-and-Analyzing-a-Phase-Diagram-using-the-Materials-API.html
https://gist.github.com/shyuep/3570304
https://gist.github.com/computron/c0323115e92b48d0019d
这是最详细的一个：https://workshop.materialsproject.org/lessons/06_new_systems/06%20-%20New%20Systems%20-%20filled/
PDPlotter Examples：https://python.hotexamples.com/examples/pymatgen.phasediagram.plotter/PDPlotter/-/python-pdplotter-class-examples.html
pymagen开发者笔记：http://matgenb.materialsvirtuallab.org/
pymatgen学习：https://wenhaosun.github.io/docs/MSE593/
'''

from pymatgen.core import Composition
from pymatgen.ext.matproj import MPRester
from pymatgen.analysis.phase_diagram import PhaseDiagram, PDPlotter, CompoundPhaseDiagram
from pymatgen.core import Element
import collections

print('开始注册MP！！！')
a = MPRester("K5JtfUOhunkvFWgT")
print('MP注册成功！！！')

'''
get_entries_in_chemsys()
For example, elements = [“Li”, “Fe”, “O”] will return a list of all entries in the Li-Fe-O chemical system, i.e., all LixOy, FexOy, LixFey, LixFeyOz
'''
# create phase diagram!
entries = a.get_entries_in_chemsys(['Cu'])  # MPRester---print(type(entries))-------<class 'list'>
print("Get entries success!")
pd = PhaseDiagram(entries)  # PhaseDiagram is the standard constructor for phase diagram.
print("Get phasediagrom!")

# plot!
# plotter = PDPlotter(pd, show_unstable=0.2, backend="matplotlib")
# plotter = PDPlotter(pd,  show_unstable=0.2, markerfacecolor=(0.2157, 0.4941, 0.7216), markersize=10, linewidth= 2)
print("--------开始画图--------------")
# plotter = PDPlotter(pd, backend="matplotlib")
plotter = PDPlotter(pd, show_unstable=True, markersize=10, backend="matplotlib")


plotter.show()  # 显示图片

print("---------结束画图-------------")
# plotter.write_image("{}.png".format('-'.join(system)), "png")  # save figure
# plotter.write_image("Cu.png", "png")  # save figure image=str(ff)+str("_DFT")+str(".jpg")  plotter.write_image(image)


# 轮廓相图Contour phase diagram

# 二元相图Binary phase diagram
# fig = plotter.get_contour_pd_plot()
# fig.show()




# cpd = CompoundPhaseDiagram(entries, [Composition("ZnS"), Composition("CuS")], normalize_terminal_compositions=False)
# compound_plotter = PDPlotter(cpd, show_unstable=100, markersize=20)
# compound_plotter = PDPlotter(cpd, show_unstable=100, markersize=20)
# compound_plotter.show()

# plotter.get_chempot_range_map_plot([Element("Cu"), Element("Zn")])
# print('执行成功')

# analyze phase diagram!

# data = collections.defaultdict(list)
# for e in entries:
#     decomp, ehull = pd.get_decomp_and_e_above_hull(e)
#     data["Materials ID"].append(e.entry_id)
#     data["Composition"].append(e.composition.reduced_formula)
#     data["Ehull"].append(ehull)
#     data["Decomposition"].append(" + ".join(["%.2f %s" % (v, k.composition.formula) for k, v in decomp.items()]))
#
# from pandas import DataFrame
# df = DataFrame(data, columns=["Materials ID", "Composition", "Ehull", "Decomposition"])
#
# print(df.head(30))




# from pymatgen.electronic_structure.plotter import BSPlotter
# # ZnS_bs =a.get_bandstructure_by_material_id("mp-10695")
# ZnS_bsp = BSPlotter(ZnS_bs)
# ZnS_bsp.show() # takes a second






