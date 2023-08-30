# P110
# 列表 list: 一次性存储多个数据（元素），可进行的操作有：增，删，改，查

name_list = ['Tom', 'Lily', 'Rose']
print(name_list)
print(name_list[0])  # 输出Tom

# 查找相关的函数：index(), count(), len() 用法与字符串中的一模一样
print(name_list.index('Lily'))  # 第二个元素，输出为1
print(name_list.count('Lily'))  # 返回1，Lily名字只出现了1次
print(len(name_list))   # 公共方法，不用在前面添加字符串序列，反映列表里有多少个元素

# 判断指定的数据是否存在，用in来判断(可用于判断是否存在列表之中)
print('Lily' in name_list)  # 返回True
print('Lilys' in name_list)  # 返回False
print('Lily' not in name_list)  # 返回False

# 案例：
name = input('请你输入您创建的用户名：')
if name in name_list:
    print(f'用户名{name}已被占用，不可以注册！')
else:
    print(f'用户名{name}创建成功！')