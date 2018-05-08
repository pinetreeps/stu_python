# _*_ coding:utf-8 _*_
# Filename: hello.py
# Author: pang song
# python 3.5
# Date: 2017/09/24


# ----------------------------格式化输入输出------------------------------------
# name = input('please input your name:')
#
# print(name)
# print(type(name))
# print("personal information of {n}: \n \t name: {n} ".format(n=name))



# ----------------------------操作mysql的技巧------------------------------------
'''
# pymysql方式逐条查询数据
# 然后我们调用了 fetchone() 方法，这个方法可以获取结果的第一条数据，返回结果是元组形式，元组的元素顺序跟字段一一对应，也就是第一个元素就是第一个字段 id，第二个元素就是第二个字段 name，以此类推。随后我们又调用了fetchall() 方法，它可以得到结果的所有数据，然后将其结果和类型打印出来，它是二重元组，每个元素都是一条记录。我们将其遍历输出，将其逐个输出出来。
# 但是这里注意到一个问题，显示的是4条数据，fetall() 方法不是获取所有数据吗？为什么只有3条？这是因为它的内部实现是有一个偏移指针来指向查询结果的，最开始偏移指针指向第一条数据，取一次之后，指针偏移到下一条数据，这样再取的话就会取到下一条数据了。所以我们最初调用了一次 fetchone() 方法，这样结果的偏移指针就指向了下一条数据，fetchall() 方法返回的是偏移指针指向的数据一直到结束的所有数据，所以 fetchall() 方法获取的结果就只剩 3 个了，所以在这里要理解偏移指针的概念。
# 所以我们还可以用 while 循环加 fetchone() 的方法来获取所有数据，而不是用 fetchall() 全部一起获取出来，fetchall() 会将结果以元组形式全部返回，如果数据量很大，那么占用的开销会非常高。所以推荐使用如下的方法来逐条取数据：
sql = 'SELECT * FROM students WHERE age >= 20'
try:
    cursor.execute(sql)
    print('Count:', cursor.rowcount)
    row = cursor.fetchone()
    while row:
        print('Row:', row)
        row = cursor.fetchone()
except:
    print('Error')
# 这样每循环一次，指针就会偏移一条数据，随用随取，简单高效。
'''