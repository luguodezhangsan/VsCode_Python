# 异常类型: 异常信息
# 为什么要捕捉异常信息?
'''
try:
    print(num)
except (NameError, ZeroDivisionError) as result:  # 这里的 result 里存贮的就是异常的描述信息
    print(result)
'''
# name 'num' is not defined