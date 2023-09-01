# else 表示的如果没有异常要执行的代码

try:
    print(1)                   # 没问题需要执行
except Exception as result:
    print(result)              # 这里没有异常故跳过了 5, 6 行, 执行否则的第 7, 8 行
else:
    print('我是 else, 当没有异常时执行的代码')
'''
1
我是 else, 当没有异常时执行的代码'''