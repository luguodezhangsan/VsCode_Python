# test[备份].txt
'''
步骤：
1. 接受用户输入的文件名
2. 规划备份文件名
3. 备份文件写入数据
    3.1 打开文件
    3.2 写入数据
    3.3 关闭文件'''

# 1. 用户输入目标文件
old_name = input('请输入你要备份文件的名：')
print(old_name)  # 最后的 .xxx 才是真正的文件类型 
print(type(old_name))

# 2. 规划备份文件的名字
# 2.1 提取文件后缀点的下标，最右侧的点才是后缀的点 --> 字符串查找某个子串 rfind
index = old_name.rfind('.')
print(index)

if index > 0:                   # index = 0 的情况就是用户输入了 '.txt' 该格式不符合文件命名规则，不能使用
    postfix = old_name[index:]  # postfix 这个单词就是后缀的意思

# 2.2 组织新名字 = 原名字 + [备份] + 后缀
# 原名字就是字符串中的一部分子串 --> 切片就可以解决
print(old_name[:index])
print(old_name[index:])
new_name = old_name[:index] + '[备份]' + postfix
print(new_name)

# 3. 备份文件写入数据（数据与原文件一样）
# 3.1 打开原文件 和 备份文件
old_f = open(old_name, 'rb')  # 用二进制打开更符合计算机语言，不容易出错  旧文件已经存在了，故可以用 r，如果不存在原文件则会报错
new_f = open(new_name, 'wb')

# 3.2 原文件读取，将其写入备份文件
# 如果不确定目标文件大小，循环读取写入，当读取出来的数据没有了则终止
while True:
    con = old_f.read(1024)  # 避免全部读入，万一文件过大则会导致内存卡死，不足 1024 的个数据就读取应有的数据个数
    if len(con) == 0:
        # 表示读取完成了
        break

    new_f.write(con)


# 3.3 关闭两个文件
old_f.close()
new_f.close()


