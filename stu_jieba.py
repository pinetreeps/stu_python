# 采用jieba包进行分词，载入用户字典，去除停用词，计算词频

import re
import jieba
import jieba.posseg as pseg
import snownlp

# 读取抓取的文件
file_obj = open('temp.txt')
data_text = file_obj.read()
file_obj.close()

# 使用正则表达式，选择所有中文字符，得到列表
chinese_pattern = re.compile("[\u4e00-\u9fa5]+", re.S)
data_text = chinese_pattern.findall(data_text)
print(type(data_text))
print(len(data_text))

# 将正则后的列表合并
data_text ="".join(data_text)
print(data_text)

# 使用jieba分词包分割
seg1 = jieba.lcut(data_text)
# seg2 = jieba.cut(data_text)
print(seg1)
# print("/".join(seg2))

# 导入自己的字典，字典文档必须为utf-8编码
my_dict = jieba.load_userdict("my_dict.txt")
# 重新分词
seg1 = jieba.lcut(data_text)
print(seg1)
print(len(seg1))



# 读取停用词到列表
f = open("stop_word.txt")
stop_word = []
for line in f.readlines():
    # 逐行读取数据
    line = line.strip("\n")
    # if not len(line) or line.startswith('#'):
    # 判断是否是空行或注释行
    stop_word.append(line)
print(stop_word)
f.close()

# 删除停用词
for s in seg1:
    if s in stop_word:
        seg1.remove(s)

print(seg1)
print(len(seg1))

''''''
# 生成字典记录词频
word_freq_dict = dict()
for word in seg1:
    freq = seg1.count(word)
    word_freq_dict[word] = freq
print(word_freq_dict)

# 用set函数转为集合去重
seg1 = set(seg1)
print(seg1)
print(len(seg1))