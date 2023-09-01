# 需求：批量修改文件名，既可添加指定字符串，又可以指定删除指定字符串

# 添加字符串
# 1. 找到所有文件：获取文件夹的目录列表 -- listdir()
''' 
import os
file_list = os.listdir()
print(file_list)'''

# 2. 构造新名字
''' 
for i in file_list:
    new_name = 'Python' + i
'''

# 3. 重命名
'''
    os.rename(i, new_name)
'''
    # 千万不能执行哇，不然我好不容易设置的序号会被加个 Python 好丑啊

# 既能添加字符串又能删除字符串版本
# 1. 找到所有文件：获取文件夹的目录列表 -- listdir()
import os
file_list = os.listdir()
print(file_list)

# 2.构建条件函数
flag = 1  # 这里也可以设置为 0，布尔值等,通过修改这里的值实现文件名的添加或者删除

# 3.构建名字
for i in file_list:
    if flag == 1:
        new_name = 'Python_' + i
    elif flag == 2:
        num = len('Python_')   # 输出为7,以取长度的方式与下面的切片结合来实现删除字符串
        new_name = i[num:]     # 从第7个开始,取到最后一个值
    # 重命名
    os.rename(i, new_name)

# 这个案例完全可以用来实战修改文件夹里面文件的名称哇