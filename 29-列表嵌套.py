# 列表嵌套：一个列表里包含了其他的子列表

namelist = [['小明', '小红', '小华'], ['Tom', 'Lily', 'Rose'], ['张三', '李四', '王五']]
print(namelist[0])   # 返回第一个子列表：['小明', '小红', '小华']

# 如何找到Lily？
print(namelist[1][1])