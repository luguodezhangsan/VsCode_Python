# 方法一
'''
import 包名. 模块名
包名. 模块名. 目标'''

import mypackage. my_module3
mypackage. my_module3. info_print1()
'''
3
my_module3
'''

# 方法二
# 注意：必须在 __init__.py 文件中添加 __all__ = []，添加允许导入的模块列表
'''
from 包名 import *
模块名. 目标
'''

from mypackage import *
my_module3. info_print1()
'''
3
my_module3
'''