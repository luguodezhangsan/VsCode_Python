# 两个函数 testA 和 testB --> 在 A 里嵌套调用 B
def testB():
    print('B函数开始......')
    print('这是B函数')
    print('B函数结束......')

def testA():
    print('A函数开始......')
    testB()
    print('A函数结束......')

testA()
'''
A函数开始......
B函数开始......
这是B函数
B函数结束......
A函数结束......'''
# 目标是为了减少步骤与函数的复杂程度