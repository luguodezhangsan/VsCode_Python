# P286
# 需求：将小于房子剩余面积的家具摆放到房子中
'''
定义类（房子和家具）
房子类
    实例属性
        房子地理位置
        房子占地面积
        房子剩余面积
        房子内家具列表
    实例方法
        容纳家具
    显示房屋信息
    
家具类
    家具名称
    家具占地面积
    '''

class Furniture():
    def __init__(self, name, area):
        self.name = name
        self.area = area

class Home():
    def __init__(self, address, area):
        # 地理位置
        self.address = address
        # 房屋面积
        self.area = area
        # 剩余面积
        self.free_area = area
        # 家具列表
        self.furniture = []

    def __str__(self):
        return f'房屋的地理位置在{self.address}，房屋面积是{self.area}，剩余面积是{self.free_area}，家具有{self.furniture}'

    def add_furniture(self, item):
        '''容纳家具'''
        if self.free_area >= item.area:
            self.furniture.append(item.name)
            self.free_area -= item.area
        else:
            print('家具太大，剩余面积不足，无法容纳')

# 双人床：6
bed = Furniture('双人床', 6)
jia1 = Home('北京', 1000)
print(jia1)
# 房屋的地理位置在北京，房屋面积是1000，剩余面积是1000，家具有[]
# 自动调用了 init 和 str，add_furniture 未调用

jia1.add_furniture(bed)
print(jia1)
# 房屋的地理位置在北京，房屋面积是1000，剩余面积是994，家具有['双人床']
# 手动调用了 add_furniture 后再到 Home 中输出 jia1

ball = Furniture('篮球场', 2000)
jia1.add_furniture(ball)
print(jia1)
# 家具太大，剩余面积不足，无法容纳
# 房屋的地理位置在北京，房屋面积是1000，剩余面积是994，家具有['双人床']

# 魔法方法在调用该类时会自动使用，而其他函数需要手动调用