# __del__()
class Wahser():
    def __init__(self):
        self.width = 300

    def __del__(self):            # 这里已经删除了所有对象
        print('对象已经被删除')    # 删除对象后输出

haier = Wahser()
# 对象已经被删除
# 会在执行这些对象后，自动删除这些对象来清理计算机内存