# 当导入一个模块时，Python 解释器对模块位置的搜索顺序是：
# 遵循 由近及远 的原则
'''
1. 当前目录
2. 如果没在当前目录，Python 则搜索在 shell 变量 PYTHONPATH 下的每个目录
3. 如果都找不到，Python 会查看默认路径。UNIX 下默认路径一般为 /usr/local/lib/Python/'''

'''
注意：
1. 自己的文件名不要和已有模块名重复，否则导致模块功能无法使用，例如自己定义个 random 模块会引用自己定义的 random
2. 使用 from 模块名 import 功能的时候，如果功能名字重复，调用的是最后定义或导入成功的功能'''

import  random
num = random.randint(1, 5)
print(num)
# 随机打印 1 ~ 5 的数字

# 自己在该目录下定义一个 random.py 文件，再次运行本文件代码，则会报错（因为要报错，所以就不实验了）
from time import sleep
sleep(2)

def sleep():
    print('我是自定义的sleep')

# sleep(2) --> 这里会报错，被注释了
# TypeError: sleep() takes 0 positional arguments but 1 was given
# 调用了后面个 sleep()
# 就算把顺序提前，到 from time import sleep 之前，还是调用最后个 sleep



# 模块名重复的危害
import time
print(time)
# <module 'time' (built-in)> 
time = 1
print(time)
# 1
# 定义变量名与模块名重名，变量名在模块名后会被覆盖，造成后面 import time 照成混乱
# 问题：为了变量也能覆盖模块？ -- Python 语言中，数据是通过 引用 传递的