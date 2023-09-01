# 控制模块导入的导入行为
# 如果一个模块文件中有 __all__ 变量，当使用 from xxx import * 导入时，只能导入这个列表中的元素
from my_module2 import *
testA()
# testA
# testB()
# NameError: name 'testB' is not defined
# testB() 不能被调用，因为不在 __all__ 列表之中