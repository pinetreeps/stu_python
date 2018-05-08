# python设计模式学习笔记2

# 装饰模式

# 示例1
# 定义一个被装饰的类
class BeDeco:
    def be_edit_fun(self):
        print("Source fun.")

    def be_keep_fun(self):
        print("Keep fun.")


# 定义一个装饰类
class Decorater:
    def __init__(self, dec):
        self._dec = dec()

    def be_edit_fun(self):
        print("Start...edit...")
        self._dec.be_edit_fun()

    def be_keep_fun(self):
        # print("Start...keep...")
        self._dec.be_keep_fun()

# 示例2
# 定义一个装饰器，也就是一个装饰函数

def deco(a_class):
    class NewClass:
        def __init__(self, age, color):
            self.wrapped = a_class(age)
            # 将传入的类实例化
            self.color = color
            # 增加一个属性 颜色

        def display(self):
            print(self.color)
            print(self.wrapped.age)
    return NewClass


# 被包装的类
@deco
class Cat:
    def __init__(self, age):
        self.age = age

    def display(self):
        print(self.age)

    # 通过装饰器来为类Cat增加属性color


if __name__ == '__main__':
    # 示例1测试代码
    bd = BeDeco()
    bd.be_edit_fun()
    bd.be_keep_fun()

    dr = Decorater(BeDeco)
    dr.be_edit_fun()
    dr.be_keep_fun()

    # 示例2测试代码
    c = Cat(12, "black")
    c.display()
    # 经过装饰器装饰后，使Cat类增加了一个颜色属性