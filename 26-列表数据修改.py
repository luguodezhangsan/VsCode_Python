num_list = [1, 2, 3, 4, 5, 6]

# 修改指定下标的数据
num_list[0] = 0
print(num_list)
# 返回：[0, 2, 3, 4, 5, 6]

# 逆序 reverse()
num_list.reverse()
print(num_list)
# 返回：[6, 5, 4, 3, 2, 0]

# sort() 排序：升序 和 降序
# 语法：sort(key = None, reverse = False)    key 用于字典中按某个值来进行排序
# 默认 sort()中被赋予 reverse = False 做升序排序
num = [3, 1, 4, 2, 6]
num.sort()
print(num)  # 升序排序
num.sort(reverse = True)
print(num)  # 降序排序