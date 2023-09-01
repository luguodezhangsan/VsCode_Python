# 当捕获多个异常时,可以把要捕获的异常类型的名字,放到except后,并使用元组的方式进行书写
try:
    print(1/0)
except (NameError, ZeroDivisionError):
    print('0 不能作为除数')
# 0 不能作为除数
# 执行代码出现的异常被捕获类型的其中之一出现一致,则可以成功捕获异常