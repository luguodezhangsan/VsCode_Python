# Exception 是所有程序异常类的父类

'''
try:
    print(num)
except Exception as result:
    print(result)
'''
# name 'num' is not defined
# 不用管 异常类型 是什么, Exception 包括所有异常类型

try:
    print(1/0)
except Exception:   # 后面的 as result 可以省略, 其本来的目的就是为了来看 异常信息的, 最后如果没有输出异常信息则可以省略
    print(1)
# 1