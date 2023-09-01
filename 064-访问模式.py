'''
主访问模式：
1. r  只读方式打开文件
2. w  只可写方式打开文件
3. a  表追加'''

'''
测试目标：
1. 访问模式对文件的影响
2. 访问模式对 write() 的影响
3. 访问模式是否可以省略'''

# 1. r  如果文件不存在则报错，不支持文件写入表示只读
# f = open('test1.txt', 'r')
# f.close()
# FileNotFoundError: [Errno 2] No such file or directory: 'test1.txt'
# 没有该文件则会报错该文件不存在

f = open('test.txt', 'r')
# D:/APP/python/python.exe e:/VsCodeProject/64-访问模式.py
# 会返回未见所在的位置并打开访问模式
f.close()

# f = open('test1.txt', 'r')
# 若文件不存在，用 r 格式打开则会报错
# f = open('test.txt', 'r')
# f.write('aa')
# f.close()
# io.UnsupportedOperation: not writable
# 因为该文件是不可以访问的，所以报错为 not writable

# 2. w  只写，如果文件不存在则新建文件，执行写入会覆盖原有内容
f2 = open('test2.txt', 'w')
f2.write('bb')
f2.close()

# 3. a  追加，如果文件不存在则新建文件，在原有基础上增加内容，不会覆盖原有内容
f3 = open('test3.txt', 'a')
f3.write('abc')
f3.close()

f3 = open('test3.txt', 'a')
f3.write('xyz')
f3.close()

# 4. 访问模式参数是否可以省略  可以省略，表示访问模式为 r
f4 = open('test.txt')
f4.close()

# .txt 可以省略，默认生成文本属性