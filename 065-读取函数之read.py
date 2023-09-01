# P247
# read()
# 文件对象.read(num)
# num表示要从文件中读取的数据的长度（单位是字节），如果没有传入num，那么就表示读取文件中所有数据

# readlines()
# 可以按照行的方式把整个文件中的内容进行一次性读取，并且返回的是一个列表，其中每一行的数据作为一个元素

'''
而且文件之中不允许执行多次读取操作，只能使用一次'''

f = open('test.txt', 'r')
print(f.read())  # read() 不写参数表示读取全部内容
'''
aaaaaa
bbbbbb
cccccc
dddddd
eeeeee'''
print(f.read(10))  
'''
aaaaaa
bbb'''
# 不是输出 10 个字符吗？这么只有 9 个？
# 因为换行符也算一个字符，所以一共是10个
f.close()

f1 = open('test.txt', 'r')
a = f1.readlines()
print(a)

f.close()
# ['aaaaaa\n', 'bbbbbb\n', 'cccccc\n', 'dddddd\n', 'eeeeee']

f2 = open('test.txt', 'r')
b = f2.readline()
print(b)
# aaaaaa
c = f2.readline()
print(c)
# bbbbbb
f2.close()
# readline() 一次读取一行内容，多次读取就读取下行