# 1. 导入 managerSystem 模块
from managerSystem import *

# 2. 启动学员管理系统
# 保证是当前文件运行才启动管理系统：if --> 创建对象并调用 run 方法
if __name__ == '__main__':
    student_manager = StudentManager()
    student_manager.run()