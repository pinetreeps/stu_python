class Washer:
    """
    this is a Washer class
    """
    # 定义类名后三个双引号内是类的说明，可以通过 类名.__doc__ 访问

    company = "Hai1er Washer"
    # 类属性，一旦改变，所有对象访问该值都改变

    def __init__(self, water=10, scour=2):
        self._water = water
        # _water为非强制性私有属性，仅为标记，可以直接访问，如果想限制访问，可用装饰器加以限制
        self.scour = scour
        self.year = 2010
        # scour、year为实例属性，仅随实例改变，互不影响
        self.__c = 20
        # __c为私有属性，无法用直接访问

    @property
    # 用装饰器包装_d这个实例属性，使外界用方法water访问_water
    def water(self):
        return self._water

    @property
    def total_year(self):
        return 2017 - self.year

    @water.setter
    # 用可写装饰器控制属性_water的输入范围，如果没有这个可写装饰器，则属性_water就只能读取不能写
    def water(self, water):
        if 0 < water <= 500:
            self._water = water
        else:
            print("set water failure!")

    @staticmethod
    # 静态方法，相当于在类里的一个普通函数，这个函数是将洗涤剂的勺数转化为毫升
    def spins_ml(spins):
        print("Washer company is ", Washer.company)
        # 静态方法中只能用类名.类属性才能访问，不能访问实例属性（也就是self.实例属性名），因为实例属性在实例化之前是不存在的
        return spins * 0.4


    @classmethod
    # 类方法，提供另外一种新建类对象的方法，用于需要另外一种预处理方法的情况，不需要硬编码类名，虽然用Washer.也可以，但是一旦类名更改，就比较麻烦
    # 这里同样不能访问实例属性（也就是self.实例属性名），因为实例属性在实例化之前是不存在的
    # 这里定义的类方法意思是用洗涤剂的勺数来建立对象，而默认是用洗涤剂毫升升数建立对象
    def get_washer(cls, water, scour):
        return cls(water, cls.spins_ml(scour))

    def set_water(self, water):
        self.water = water

    def set_scour(self, scour):
        self.scour = scour

    def add_water(self):
        print("add water: ", self.water)

    def add_scour(self):
        print("add scour: ", self.scour)

    def start_wash(self):
        self.add_water()
        self.add_scour()

    def info_washer(self):
        print("water is: ", self.water, "scour is: ", self.scour, "__c:", self.__c)


class WasherDry(Washer):
    # 继承Washer洗衣机类
    def dry(self):
        print("Dry clothes...")

    def start_wash(self):
        self.add_scour()
        self.add_water()
        print("WasherDry start wash...")
        # 重载父类的开始洗涤start_wash方法，改变执行顺序
        super().start_wash()
        # 通过super().调用父类方法（
        # 实例对象调用方法的顺序：
        # 1、单继承情况：首先会先在该子类中寻找这个方法，没有的话继续向父类、祖父类搜索，以此类推
        # 2、多继承情况：按照广度优先进行搜索，也就是按照继承顺序搜索，父类都没有再向上级类搜索（新式类）

if __name__ == '__main__':
    print(Washer.__doc__)
    w1 = Washer()
    w1.start_wash()

    w2 = Washer()
    w2.__c = 3
    # 私有属性__c无法修改，输出__c值不变
    w2.info_washer()
    print(w2.__c)
    # 此次输出的__c虽然改为3，但实际程序为了保护私有属性不被外界修改，在运行时，已经将真的私有属性__c改为其他名称，
    # 这里输出的相当于是由赋值语句新建的__c，所以这里输出是__c=3

    setattr(w1, 'water', 15)
    temp1 = getattr(w1, 'scour')
    print(temp1)

    print(w1.water)
    w1.water = 500
    print(w1.water)
    print(w1.spins_ml(5))
    w3 = Washer(200, Washer.spins_ml(9))
    w3.start_wash()

    w4 = Washer.get_washer(100, 9)
    # 调用类方法，可以用 类名.静态方法 或者 对象.静态方法 访问，这里用第二个参数是洗涤剂勺数
    w4.start_wash()

    wd1 = WasherDry()
    wd1.start_wash()

