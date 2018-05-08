# python设计模式学习笔记1

# 单例模式

# 工厂模式

# 策略模式
# 让一个对象的某个方法可以随时改变，而不用更改对象的代码
# 对于动态类型的python语言，不需要定义接口
# 基本实现方法：用类作为参数传递
# 最简实现方法：用函数作为参数来传递


class Moveable:
    def move(self):
        print("Move...")


class MoveOnFeet(Moveable):
    def move(self):
        print("Move on Feet...")


class MoveOnWheel(Moveable):
    def move(self):
        print("Move on Wheels...")


class MoveObj:
    def set_move(self, moveable):
        self.moveable = moveable()
        # 实例化传入的moveable类

    def move(self):
        self.moveable.move()


class Test:
    def move(self):
        print("This is a test")


if __name__ == '__main__':
    m = MoveObj()
    # 随时改变MoveObj实例对象调用的Move方法
    m.set_move(Moveable)
    m.move()
    m.set_move(MoveOnFeet)
    m.move()
    m.set_move(MoveOnWheel)
    m.move()

    # 对于python来说，没有继承统一父类Moveable也可以调用
    m.set_move(Test)
    m.move()