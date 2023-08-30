# __str__()
# 使用 print 输出对象的时候，默认会打印对象的内存地址。如果类定义了 __str__() 方法，那么就会打印从在这个方法中 return 的数据

class Wahser():
    def __init__(self):
        self.width = 300

    def __str__(self):
        return '解释说明：类的说明或对象状态的说明'
        # 解释说明：类的说明或对象状态的说明
        # 加上这个 __str__() 会返回 return 后的内容，代替默认返回的地址

haier = Wahser()
print(haier)
# <__main__.Wahser object at 0x000001BD17CB2FD0>
# 输出的是内存地址