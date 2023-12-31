# P244
'''
1. 文件操作的作用：读写，备份
2. 文件的基本操作
    2.1 打开
    2.2 读写
    2.3 关闭
3. 文件备份
4. 文件和文件夹的操作'''

# 1. 打开
# open(name, mode) --> 可以打开一个已经存在的文件，或者创建一个新文件
'''
name: 是要打开的目标文件名的字符串（可以包含文件所在的具体路径）
mode: 设置打开文件的模式（访问模式）：只读、写入、追加等'''
f = open('test.txt', 'w')

# 2. 读写操作 read() write() 
f.write('aaa')

# 3. 关闭 close() --> 目的是为了节省内存
f.close()

