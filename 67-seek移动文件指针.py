# seek()
# 作用：用来移动文件指针
# 语法：文件对象.seek(偏移量, 起始位置)
'''
起始位置：
0 开头位置
1 当前位置
2 文件结尾'''

'''
目标：
1. r 改变文件指针位置：改变读取数据开始位置或把文件指针放在结尾（无法读取数据）
2. a 改变文件指针位置：做到可以读取数据'''

f = open('test.txt', 'r+')

# 将指针的位置向后移动两个，导致前面 'aa' 没有被读取
f.seek(2, 0)

# 将指针的位置改到最后，读取不了数据，输出为空
# f.seek(0, 2)

con = f.read()
print(con)
'''
aaaa
bbbbbb
cccccc
dddddd
eeeeee'''

f.close()

# 本来 a+ 的位置在文本的最后，但是用 seek() 将指针的位置移动到了开始的地方，则可以读取全部内容
f2 = open('test.txt', 'a+')

f2.seek(0, 0) # == f.seek(0) 此处省略的是偏移量，保留了起始位置

con = f2.read()
print(con)
'''
aaaaaa
bbbbbb
cccccc
dddddd
eeeeee'''

f2.close()
