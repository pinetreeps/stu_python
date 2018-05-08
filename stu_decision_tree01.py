# _*_ coding:utf-8 _*_
# Filename: stu_decision_tree01.py
# Author: pang song
# python 3.5
# Date: 2017/08/31

# 用pd中的DF数据类型简单实现决策树
# 采用的数据集为iris

from sklearn import tree
import pandas as pd
import numpy as np
from math import log2



class tree_point:
    def __init__(self, id=0, father_id=None, DF_col=None, class_now=None, DF_now=None, if_leaf=None):
        self.id = id #节点id
        self.father_id = father_id # 当前节点父节点的id
        self.DF_col = DF_col # 储存当前节点分类的类名（列号）
        self.class_now = class_now # 储存当前节的分类特征值
        self.DF_now = DF_now # 储存当前节点子集，DF类型
        self.if_leaf = if_leaf # 对应结果为True时，说明当前为叶节点，不再继续划分
        # self.class_num = DF_now[DF_now.columns[-1]].value_counts()


    def info_gain(self, DF_cut):
        # 决策树计算信息熵的差值，待完善
        info_gain = self.entropy(DF_cut.columns[-1])-self.conditional_entropy(DF_cut)
        return info_gain
    '''
    def split_data(self, DF_data, col):
        # 划分数据，col为划分特征所在的列序号，value为特征的具体值
        # 删除列
        DF_cut = DF_data
        for i in range(len(DF_data.columns) - 1):
            if i == col:
                pass
            else:
                DF_cut = DF_cut.drop(DF_data.columns[i], axis=1)
                # print(DF_cut)
        # 取数据中等于value值的行
        # DF_cut = DF_cut[DF_cut[DF_cut.columns[0]].isin([value])]
        return DF_cut
    '''

    def split_data(self, DF_data, col):
        # 删除列
        DF_cut = DF_data
        DF_cut = DF_cut.drop(DF_data.columns[col], axis=1)
                # print(DF_cut)
        return DF_cut

    def entropy(self, DF_cut_one_columns):
        # 计算信息熵，输入为单维度数据
        results = DF_cut_one_columns.value_counts()
        ent = 0.0
        # print("len(rows) is ",len(rows))
        for r in results.index:
            # print("r in rows is ", r)
            p = float(results[r])/len(DF_cut_one_columns)
            ent = ent - p*log2(p)
        return ent

    def conditional_entropy(self, DF_cut, col):
        # 计算条件信息熵，输入为DF类型数据，col列为需要计算条件熵的列，最后一列为特征
        # 取输入DF类型的第col列
        DF_cut_col = DF_cut[DF_cut.columns[col]]
        # 获得col列的序列表
        DF_cut_index = DF_cut_col.value_counts()
        # 初始化条件熵
        conditional_entropy = 0.0

        for value in DF_cut_index.index:
            # 取数据中等于value值的行
            DF_cut_value = DF_cut[DF_cut[DF_cut.columns[col]].isin([value])]
            ent = self.entropy(DF_cut_value.columns[-1])
            conditional_entropy = conditional_entropy + DF_cut_index[value]/len(DF_cut)*ent

        return conditional_entropy

    def build_tree(self, DF_cut):
        # 判断是否新节点是否为叶子节点
        if len(DF_cut.columns) == 2:
            self.if_leaf = True
            return self.id
        # 生成树
        # for i in self.__leaf_value_list:
        #     i.append(Node(self.__node_dict))
        pass


    def print_tree(self, tree):
        # 决策树的显示函数 待完善
        if tree.if_leaf == True:
            print(tree.DF_now)
        else:
            print(tree.DF_now, "-->")

'''
    # 递归方式构建决策树
    def build_tree(data):
        # 传入参数为DF类型
        # 判断数据是否只剩一个维度
        # tree_point = tree_point()
        if len(data.columns) == 1:
            return 0
        else:
            # 计算各维度的信息熵，保存最大值
            num = len(data.columns)-1
            for i in range(num):
                if

'''
# 分割数据集


def unique_counts(rows):
    # 计算各个取值（字符串）出现的次数，返回字典，为参考内容，本次实现不需要
    results = {}
    for row in rows:
        # 计数结果储存在最后一列
        r = row[len(row)-1]
        if r not in results:results[r] = 0
        results[r] += 1
    return results

# 汐哥提供的思路-------------------------------------------------------
'''
# 汐哥提供的思路1，二叉树
class Node(object):
    def __init__(self, node_list):
        self.__value = node_list
        self.__left_list = []
        self.__right_list = []
        self.__sleft_leaf = None
        self.__right_leaf = None
        self.__split()
        self.__born()

    def __split(self):
        # todo handle self.__value
        left_list = []
        right_list = []

    def __born(self):
        self.__left_leaf = Node(self.__left_list)
        self.__right_leaf = Node(self.__right_list)


# 汐哥提供的思路2，id3算法
class Node(object):
    def __init__(self, node_dict):
        self.__node_dict = node_dict
        self.__leaf_value_list = []
        self.__leaf_node_dict = {}
        self.__split()
        self.__born()

    def __split(self):
        # todo handle self.__node_dict
        # self.__leaf_value_dict = [[left, right, sub_node_dict],...]
        pass

    def __born(self):
        for i in self.__leaf_value_list:
            i.append(Node(self.__node_dict))

class Node(object):
    def __init__(self, node_dict):
        self.__node_dict = node_dict
        self.__leaf_value_list = []
        self.__split()
        self.__born()

    def __split(self):
        # todo handle self.__node_dict
        # self.__leaf_value_dict = [[left, right, sub_node_dict],...]
        pass

    def __born(self):
        for i in self.__leaf_value_list:
            i.append(Node(self.__node_dict))

'''
# -------------------------------------------------


if __name__ == '__main__':
    data_iris = pd.read_table('C:\PSuse\python_work\data_analysis\iris_test0.txt', header=None, delim_whitespace=True, index_col=None)
    # print(data_iris)

    c_name = ['A', 'B', 'C', 'D', 'iris_class']
    data_iris.columns = c_name
    print(data_iris)

    # data_iris_A_index1 = data_iris['iris_class'].value_counts()
    # data_iris_A_index2 = data_iris[data_iris.columns[0]].value_counts()
    # data_iris_A_index3 = data_iris[data_iris.columns[-1]].value_counts()
    # print(data_iris['A'])

    # print(data_iris[data_iris.columns[0]])
    # print(data_iris_A_index2)

    # 储存树结构关系的字典，格式为 父节点：子节点
    # dec_tree = {}

    # print(entropy(data_iris[4]))
    # print(entropy(data_iris['C']))
    # print(entropy(data_iris['D']))
    # print(entropy(data_iris['iris_class']))
    # print(data_iris_A_index2)
    # print(data_iris_A_index2[6.6])
    # print(data_iris_A_index2.index)
    # print(type(data_iris_A_index2.index))
    # print(len(data_iris_A_index1))
    # print(len(data_iris_A_index2))
    # print(len(data_iris_A_index3))
    # print(len(data_iris.columns))

    blist = [exam for exam in data_iris['A']]
    print(blist)

'''
    # 测试5 DF类型删除特定行列
    # data_iris = data_iris.drop(0, axis=0) # 删除第1行
    # data_iris = data_iris.drop(data_iris.columns[1], axis=1) # 删除第2列
    # data_iris = data_iris.drop('A', axis=1) # 删除第A列
    # print(data_iris)
    
    # 测试4 DF类型条件切片
    num1 = 4
    tp_num = 1
    alist = [tp_num]
    tp = data_iris[data_iris[data_iris.columns[num1]].isin(alist)]
    tp2 = tp[tp.columns[num1]]
    # tp2 = data_iris.columns[num1]
    print(tp2)
    for i in tp2:
        print(i)

    # 测试3 
    # 取A列等于特定值的行isin()参数必须为list类型
    alist = [6.6]
    print("A 6.6 = ", data_iris[data_iris.A.isin(alist)])

    # 测试2 DF转numpy数组
    num = data_iris.as_matrix(columns=None)
    print(num)
    print(type(num))


    # 测试1，DF类型取值
    da = data_iris.iloc[0:1, 1]
    # iloc按位置取值，loc按照标签取值
    print(da*2)
'''
