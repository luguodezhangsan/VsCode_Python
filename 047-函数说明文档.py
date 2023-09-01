# 如何在许多代码中找到某个函数的定义及注释？
# 函数说明文档写法
# 语法：help(函数名)
help(len)
'''
len(obj, /)
    Return the number of items in a container.'''

# help() 用来查看函数的说明文档
def sum_num(a, b):
    '''这里就是说明文档，必须放在第一行这个位置！'''
    c = a + b
    return c

help(sum_num)
'''
sum_num(a, b)
    这里就是说明文档，必须放在第一行这个位置！'''