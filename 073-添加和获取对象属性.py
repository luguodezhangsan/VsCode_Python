# 属性即是特征，比如洗衣机的宽度、重量、高度.....
# 对象属性既可以在类外添加和获取，也能在类里面添加和获取

# 1. 类外面添加属性
'''
语法：
对象名.属性名 = 值'''
class Washer():
    def wash(self):
        print('洗衣服')

haier1 = Washer()
haier1.width = 400
haier1.height = 500

# 2. 类外面获取对象属性
'''
语法：
对象名.属性名'''
print(f'haier1的宽度为:{haier1.width}')
print(f'haier1的高度为:{haier1.height}')
'''
haier1的宽度为:400
haier1的高度为:500'''

# 3. 类里面获取对象属性
'''
语法：
self.属性名'''
class Washer():
    def print_info(self):
        print(f'haier1的宽度为:{haier1.width}')
        print(f'haier1的高度为:{haier1.height}')

haier1 = Washer()

# 添加属性
haier1.width = 300
haier1.height = 500

# 对象调用方法
haier1.print_info()
'''
haier1的宽度为:300
haier1的高度为:500'''

