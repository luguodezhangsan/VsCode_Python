# 如果一个函数有两个返回值 return，程序如何执行？
def return_num():
    return 1
    return 2
result = return_num()
print(result)
# 1
# 只返回第一个 return 不返回第二个 return

# 返回多个值时正确写法
def return_num2():
    # return 1, 2
    return [100, 200]
result2 = return_num2()
print(result2)
# (1, 2)
# return a, b 写法返回多个数据时，默认是元组类型
# return 后面可以连接列表、元组或者字典，以返回多个值
# [100, 200]