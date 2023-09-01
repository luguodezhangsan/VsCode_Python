# 需求：一个函数完成任意两个数字加法运算
def testA(a, b):
    print(a + b)

testA(1, 1)
# 2
# 模块编写者通常会在该文件下编写测试信息，来验证该模块是否能满足需求

# 只有在当前文件中调用该函数，其他导入的文件内不符合该条件，则不执行 testA 函数调用
print(__name__)
# __main__
'''
__name__ 在当前文件中调用，输出的是 __main__
__name__ 在别的文件中被调用，输出的是 本文件的名称，即 my_module1
'''

# __name__ 是一个系统变量，是模块的标识符，值是：如果是自身模块是 __main__，否则是当前的模块的名字
if __name__ == '__main__':
    testA(1, 1)
# 2
# 故要测试模块需要使用以上代码