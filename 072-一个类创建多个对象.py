# 1. 一个类创建多个对象：2. 多个对象都调用函数的时候，self地址是否相同
class Washer():
    def wash(self):
        print('洗衣服')
        print(self)

haier1 = Washer()
haier1.wash()
'''洗衣服
<__main__.Washer object at 0x000001E01A8A2FD0>'''

haier2 = Washer()
haier2.wash()
'''洗衣服
<__main__.Washer object at 0x000001E01A8A2F10>'''

# 一个类可以创建多个对象，多个对象在调用函数的时候，self 的地址不相同