'''
体验异常传递
需求:
1. 尝试只读方式打开 test2.txt 文件, 如果文件存在则读取文件内容, 文件不存在则提示用户即可
2. 读取内容要求: 尝试循环读取内容, 当无内容的时候退出循环, 读取过程中如果检测到用户意外终止程序, 则 except 捕获异常并提示用户
'''

# 注意一下代码若想实现其效果只能在命名提示符里面执行

import time
try:
    f = open('test2.txt')  # 没有文件类型, 默认输出为 r
    # 尝试读取循环内容
    try:
        while True:
            content = f. readline()  # 一行一行的读取
            # 如果读取完成退出循环
            if len(content) == 0:
                break
            time.sleep(2)  # 引入了时间函数, 每次读取的时间间隔为 2 秒
            print(content)
    except:
    # 如果在读取文件的过程中, 产生了异常, 那么就会捕获到
    # 在命名提示符里面如果按下了 ctrl + c，则会输出以下结果
    # 如何正确调用命令提示符？
    # 依据路径：E:\PythonProject
    # 然后在路径栏里面输入 cmd 弹出该文件夹的命令提示符，输入该文件名称：101-异常传递.py 即可正常进行输出，按 tab 可以自动补全文件名
        print('意外终止了读取数据')
    finally:
        f.close()
        print('关闭文件')
except:
    print('该文件不存在')

# 异常传递的流程为从外到内