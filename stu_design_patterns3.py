# python设计模式学习笔记3

# 通过组合来构建复杂对象
# 理解组合
# 类似用零件组装机器
# 零件：基础类， 机器：包含其他类的类
# 体现自下而上的面向对象编程方法

# 案例：在画布上组合一个雪人
# 案例步骤：
# 1、面向对象分析：分为三个部分，帽子，头，身体
# 2、抽象出基础类：圆形，半圆，三角形
# 3、实现基础类，Shape类，ShapeAngles类

# 没学完……

class Shape:
    def __init__(self, cvns, points):
        self.cvns = cvns
        self.points = points
        self.pid = None
        # cvns为画布

    def delete(self):
        if self.pid:
            self.cvns.delete(self.pid)


class ShapeAngles(Shape):
    def __init__(self, cvns, points, angles=(10, 170)):
        super().__init__(cvns, points)
        self.angles = {'start':angles[0], 'extent':angles[1]}


# 4、实现子类 Hat HatBottom Face 等
class HatTop(Shape):
    def draw(self):
        self.pid = self.cvns.creat_oval(*self.points)
        # creat_oval绘制圆形函数，返回id号


class HatBottom(Shape):
    def draw(self):
        self.pid = self.cvns.creat_polygon(*self.points)
        # creat_polygon绘制多边形函数，返回id号


# 5、组装子类，将帽子顶部和帽子底部组成帽子
class Hat:
    def __init__(self, cvns, start_point, w, h):
        self.cvns = cvns
        self.start_point = start_point
        self.w = w
        self.h = h
        self.ht = HatTop(self.cvns, self.ht_cacu())
        self.hb = HatBottom(self.cvns, self.hb_cacu())
        # ht_cacu为计算坐标方法

    def draw(self):
        self.ht.draw()
        self.hb.draw()

    def delete(self):
        self.ht.delete()
        self.hb.delete()

    def ht_cacu(self):
        r = self.h /3 /2
        x1 = self.start_point[0] + self.w /2 - r
        y1 = self.start_point[1]
        x2 = x1 + 2 * r
        y2 = y1 + 2 * r
        return x1, y1, x2, y2

    def hb_cacu(self):
        x1 = self.start_point[0] + self.w /2
        y1 = self.start_point[1] + self.h /3
        x2 = self.start_point[0] + self.w /3
        y2 = self.start_point[1] + self.h
        x3 = self.start_point[0] + self.w /3 * 2
        y3 = y2
        return x1, y1, x2, y2, x3, y3


    class Sense(ShapeAngles):
        # 绘制五官的类
        def draw(self):
            self.pid = self.cvns.creat_arc(*self.points, **self.angles)
            # creat_arc绘制弧线函数


    class Face(HatTop):
        pass




