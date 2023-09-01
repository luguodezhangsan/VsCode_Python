# P183
# 变量作用域：变量生效的范围，主要分为 局部变量 和 全局变量
def testA():
    a = 100
    print(a)  # 函数内部访问，则可以访问变量 a

testA()  # 100
# print(a)

# NameError: name 'a' is not defined
# a 是一个局部变量不能全局生效，故显示a没有被定义

x = 10
def f():
    x = 5
    print('f内部: x=', x)
    return x * x

print('f()=', f())
# f内部: x= 5          # 局部变量和全局变量同名时，局部变量屏蔽全局变量，简称“局部优先”
# f()= 25              # 若 x = 5 不存在，则 x 可以访问外部变量此时 x = 10，局部变量可以访问全局变量，全局变量不可以访问局部变量
print('f外部: x=', x)  
# f外部: x= 10

# 如何在将局部变量变为全局变量？修改局部变量为全局变量
'''
语法： 
global 变量
变量 = 数值'''
a = 100
def testA():
    global a  # global 将 a 定义为了全局变量，位置位于 a = 100 下面，所以 a 的值新定义为了 200
    a = 200
    print(a)

print(a)
# 100 
testA()
# 200
print(a)
# 200

# 返回值作为参数传递
def test1():
    return 50

def test2(num):
    print(num)

result = test1()
test2(result)
# 50