# _*_ coding:utf-8 _*_
# Filename: deal_word.py
# Author: pang song
# python 3.6
# Date: 2018/05/05

import os
import re
#导入word操作模块
import win32com

#准备打开word
from win32com.client import Dispatch,constants
w = win32com.client.Dispatch('Word.Application')

#  后台运行，不显示程序界面，不警告
w.Visible = 0
w.DisplayAlerts = 0

# file_path = "C:/PSuse/python_work/stu_python/test.doc"
file_path = "C:/PSuse/python_work/stu_python/test.docx"
doc = w.Documents.Open(FileName = file_path)
#文档最开始插入文字
#myRange = doc.Range(0,0)
#myRange.InsertBefore('哈哈哈哈哈哈')
#选中并修改全文字体
#par = doc.Range(doc.Content.Start,doc.Content.End)
#par.Font.Size = "14"

#1.修改全文字体、字号
w.ActiveDocument.Select()
w.Selection.Font.Name = "微软雅黑"
w.Selection.Font.Size = "14" #四号

try:
    # content = doc.Content
    # print(content)
    par1 = doc.Paragraphs(1).Range
    # par1.ParagraphFormat.Reset()#取消首行缩进
    # par1.Font.Name = "微软雅黑"
    par1.Font.Size = "28"  # 一号
    print(par1.GetParaFormat)

except Exception as e:
    # 打印详细内容
    print("error:",repr(e))

# 关闭文档
doc.Close()

# 退出word程序
w.Quit()
exit()


# --------------- 待测试代码 --------------------
#获取课文全路径
#..\1_一单元\1_《忆读书》\1_预习\1_音画课文
for root, dirnames, filenames in os.walk(r'C:\Users\jjw\Desktop\test\111_语文晋教版七年级上册'):
#字符串前面加r之后，正则里的\d等都不用变，'\'变成'\\'即可，开头末尾是'^$'，匹配全部是'.*'
#        if re.match(r'.*\\\d+_\w+\\\d+_.+\\1_预习\\1_音画课文$',dirpath):
#                print(dirpath)
#        else:
#                print('未找到')
    for filename in filenames:
        if re.match(r'课文.rtf',filename):
            classRTF = os.path.join(root,filename)
            doc = w.Documents.Open(FileName = classRTF)
            #文档最开始插入文字
            #myRange = doc.Range(0,0)
            #myRange.InsertBefore('哈哈哈哈哈哈')
            #选中并修改全文字体
            #par = doc.Range(doc.Content.Start,doc.Content.End)
            #par.Font.Size = "14"

            #1.修改全文字体、字号
            w.ActiveDocument.Select()
            w.Selection.Font.Name = "微软雅黑"
            w.Selection.Font.Size = "14"#四号

            #2.删除空格，替换字符串
            w.Selection.Find.ClearFormatting()
            w.Selection.Find.Replacement.ClearFormatting()
            w.Selection.Find.Execute(" ",False,False,False,False,False,True,1,True,"",2)#普通空格
            w.Selection.Find.Execute("　",False,False,False,False,False,True,1,True,"",2)#这里面是个“口”的符号，全角空格

            #3.删除空行，这里数量是1，因为回车占一个字符
            for each in w.ActiveDocument.Paragraphs:
                if each.Range.Words.Count == 1:
                    each.Range.Delete()

            #作者后面插入空行
            doc.Paragraphs(2).Range.InsertAfter('\n')

            #前两行清除格式，主要是首行缩进
            doc.Paragraphs(1).Range.Select()
            w.Selection.ClearFormatting()
            doc.Paragraphs(2).Range.Select()
            w.Selection.ClearFormatting()

            #前两行改字体、字号、居中
            par1 = doc.Paragraphs(1).Range
            #par1.ParagraphFormat.Reset()#取消首行缩进
            par1.Font.Name = "微软雅黑"
            par1.Font.Size = "28"#一号
            par1.ParagraphFormat.Alignment = 1
            par2 = doc.Paragraphs(2).Range
            par2.Font.Name = "微软雅黑"
            par2.Font.Size = "12"#小四
            par2.ParagraphFormat.Alignment = 1
            print("已处理：" + classRTF)
            doc.Close()
w.Quit
print("处理完毕！")