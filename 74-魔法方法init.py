# 275
# __XX__() 的函数叫做魔法方法，指的是具有特殊功能的函数

# 1. __init__()
# 思考：洗衣机的宽度和高度是与生俱来的的属性，可不可以在生产过程中就赋予这些属性呢？

# __init__() 的作用 即是初始化对象
'''
1. __init__()方法，在创建一个对象时默认被调用，不需要手动调用
2. __init__(self)中 self 参数，不需要开发者传递，python解释器胡自动把当前对象引用过去'''

# 目标：定义 init 魔法方法设置初始化属性，并访问调用
'''
1. 定义类
    init 魔法方法：width 和 height
    添加实例方法：访问实例属性
2. 创建对象
3. 验证成果
    调用实例方法'''

class Washer():
    def __init__(self):
        # 添加实例属性
        self.width = 500
        self.height = 800
    
    def print_info(self):
        print(f'洗衣机的宽度是{self.width}')
        print(f'洗衣机的高度是{self.height}')

haier = Washer()
haier.print_info()
'''
洗衣机的宽度是500
洗衣机的高度是800'''

# 带参数的__init__()
# 1. 定义类：带参数的 init ：宽度和高度，实例方法：调用实例属性
class Washer():
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def print_info(self):
        print(f'洗衣机的宽度是{self.width}，高度是{self.height}')

# 2. 创建对象：创建多个对象且属性值不同：调用实例方法
haier1 = Washer(10, 20)
haier1.print_info()
'''
洗衣机的宽度是10，高度是20'''

haier2 = Washer()
haier2.print_info()
'''
TypeError: __init__() missing 2 required positional arguments: 'width' and 'height' '''
# 不传参数会直接报错缺少两个参数