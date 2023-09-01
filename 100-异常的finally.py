# finally 表示的是无论是否异常都要执行的代码, 例如关闭文件

try:
    f = open('test2.txt', 'r')
except Exception as result:      # 感觉这里的 result 不要也没关系, 反正也不打印
    f = open('test2.txt', 'w')  # 5, 6 行没有被执行
else:
    print('没有异常真开心')
finally:
    f.close()
