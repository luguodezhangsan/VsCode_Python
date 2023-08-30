# 案例一：烤地瓜
'''
需求主线：
1. 被烤的时间和对应的地瓜状态：
    0-3分钟：生的
    3-5分钟：半生不熟
    5-8分钟：熟的
    超过8分钟：烤糊了
    
2. 添加调料
    用户可以按照自己的意愿来添加调料'''

'''
需求涉及一个事物：地瓜，故案例涉及一个类：地瓜类
'''

'''
定义类：
1. 地瓜的属性
    被烤的时间
    地瓜的状态
    添加的调料
2. 地瓜的方法
    被烤：
        用户根据意愿设定每次烤地瓜的时间
        判断地瓜备考的总时间在哪个区间，修改地瓜的状态
    添加调料
        用户根据意愿设定添加的调料
        将用户添加的调料存储
3. 显示对象信息'''

# 1. 定义类：初始化属性，被烤和添加调料的方法，显示对象信息的 str
class SweetPotato():
    def __init__(self):
        # 被烤的时间
        self.cook_time = 0
        # 被烤的状态
        self.cook_state = '生的'
        # 调料列表
        self.condiments = []

    def cook(self, time):
        '''烤地瓜的方法'''
        # 计算地瓜烤过的时间
        self.cook_time += time
        # 用整体烤过的时间再判断地瓜的状态
        if 0 <= self.cook_time < 3:
            # 生的
            self.cook_state = '生的'
        elif 3 <= self.cook_time < 5:
            # 半生不熟的
            self.cook_state = '半生不熟的'
        elif 5 <= self.cook_time < 8:
            # 烤熟了
            self.cook_state = '烤熟了'
        elif self.cook_time >= 8:
            # 烤糊了
            self.cook_state = '烤糊了'

    def add_condiments(self, condiment):
        # 用户意愿的调料添加到调料列表
        '''添加调料'''
        self.condiments.append(condiment)

    def __str__(self):   # 返回值有字符串，否则返回的是地址
        return f'这个地瓜烤了{self.cook_time}分钟，状态是{self.cook_state}，调料有{self.condiments}'

    
# 2. 创建对象并调用对应的实例方法
digua1 = SweetPotato()
print(digua1)
digua1.cook(4)
print(digua1)
'''
这个地瓜烤了0分钟，状态是生的
这个地瓜烤了4分钟，状态是半生不熟的'''

digua1.cook(2)
print(digua1)
'这个地瓜烤了6分钟，状态是烤熟了'

digua1.add_condiments('辣椒面')
print(digua1)
digua1.add_condiments('蜂蜜')
print(digua1)
'''
这个地瓜烤了6分钟，状态是烤熟了，调料有['辣椒面']
这个地瓜烤了6分钟，状态是烤熟了，调料有['辣椒面', '蜂蜜']'''