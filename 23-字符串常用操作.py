# 字符串的常用操作的方法有查找、修改和判断三大类

# 查找：查找某个子串出现的位置或次数
# 字符串序列. find(子串, 开始位置下标， 结束位置下标)
# 检测某个子串是否在字符串中，如果在则返回位置，不在则返回 -1

# 1.find()
mystr = 'hello world and itcast and itheima and python'
print(mystr.find('and'))  # 返回12，空格也算字符，从 0-->11,12为a所在位置
print(mystr.find('and', 15, 30))  # 返回23，15到30这个区间之间找and开始的位置
print(mystr.find('ands'))  # 返回-1

# 2.index()
print(mystr.index('and'))  # 返回12
print(mystr.index('and', 15, 30))  # 返回23，15到30这个区间之间找and开始的位置
# print(mystr.index('ands'))  # 直接报错，唯一不一样的地方

# 3.count()
print(mystr.count('and'))  # 返回3
print(mystr.count('and', 15, 30))  # 返回1
print(mystr.count('ands'))  # 返回0

# 4.rfind() 和 rindex() 从右往左开始查找
print(mystr.rfind('and'))  # 返回35，仍然是从左往右

# 修改：指的是通过函数的形式修改字符串中的数据
# replace，split，join

# 1. 字符串序列.replace(旧子串, 新子串， 替换次数)  替换次数省略不写则全部替换
# replace函数有返回值，返回是修改后的字符串，原有字符串不变，说明该字符串为不可变数据类型，数据类型可以分为可变数据类型（列表、元组、字典）和不可变数据类型（'')所带的文字型字符串
new_mystr = mystr.replace('and', 'or')
print(mystr)
print(new_mystr)

new_mystr = mystr.replace('and', 'or', 1)  # 只替换从左到右的第一个
new_mystr = mystr.replace('and', 'or', 10)  # 替换次数超过子串出现的次数，则全部替换

# 2. split(): 按照指定字符串分割字符串
# 语法：字符串序列.split(分割字符, num)  # num表示分割字符出现的次数，即将来返回数据的个数为 num + 1
list1 = mystr.split('and')  # 分割，返回一个列表，丢失分割字符
print(list1)
# 输出['hello world ', ' itcast ', ' itheima ', ' python']

list2 = mystr.split('and', 2) 
print(list2)
# 输出['hello world ', ' itcast ', ' itheima and python']，只分割两次

# 3. join()：合并列表里的字符串数据为一个大的字符串
mylist = ['aa', 'bb', 'cc']
new_str = '...'.join(mylist)
print(new_str)
# 输出：aa...bb...cc

# captialize()：将字符串中第一个字符转换为大写
print(mystr.capitalize())

# title()：将字符串每个字母都转换为大写
print(mystr.title())

# 字符串序列.lower()：将字符串中大写转小写
# 字符串序列.upper()：将字符串中小写转大写
# 字符串序列.swapcase()：将字符串中大小写互换

# 该节需要注意的是是否需要新赋值

# 字符串序列.lstrip()：删除字符串左侧空白字符
# 字符串序列.rstrip()：删除字符串右侧空白字符
# 字符串序列.strip()：删除字符串两侧空白字符

# 字符串序列.ljust(长度， 填充字符)
b = 'hello'
s = b.ljust(10, '*')
print(s)
# 字符串居左对齐，输出宽度为10，不足部分以 * 补齐

# 字符串序列.rjust(长度， 填充字符)
# 字符串序列.center(长度， 填充字符)  
b = 'hello'
s = b.center(11, '*')
print(s)
# 字符串居中对齐，输出宽度为11，不足部分以 * 补齐

# 判断：是否以某子串开始或者结尾，输出 True 或 False
# 字符串序列.starwith(子串, 开始位置下标, 结束位置小标)
# 字符串序列.endrwith(子串, 开始位置下标, 结束位置小标)
print(mystr.startswith('hello'))  # 返回 True
print(mystr.startswith('hel'))    # 返回 True

# 字符串序列.isalpha()    字符串至少有一个字符并且所有字符都是字母则返回True，否则返回False
# 字符串序列.isdigital()  字符串只要包含数字返回True，否则返回False
# 字符串序列.isalnum()    字符串至少有一个字符并且所有字符都是字母或或数字则返回True，否则返回False
# 字符串序列.isspace()    字符串只要包含空白返回True，否则返回False