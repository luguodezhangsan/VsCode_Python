# “切片” 取字符串的某个部分
# 序列[开始位置下标: 结束位置下标： 步长]  步长的默认长度为1，不包括结束位置下标对应的数据，正负数都可以
# 结束位置下标更类似于取了多少个数
# 步长为选取间隔
# 步长的正负 和 选取方向 要保持一致
'''
从左到右： 0 ... n-1
从右到左： -n ... -1'''

str1 = '012345678'
print(str1[0: 5: 1])  # 其中1可以省略
print(str1[0: 5 :2])  # 选取的间隔为2
print(str1[:5])       # 开始不写，默认从0开始选取
print(str1[2:])       # 结束不写，默认选取到最后
print(str1[:])        # 开始和结束都不写，取所有

# 负数测试
print(str1[: : -1])     # 步长为负数，表示倒叙选取
print(str1[-4: -1])    # 下标-1表示最后一个数，依次向前类推
print(str1[-4: -1: -1]) # 不能选取出数据：从-4开始到-1结束，选取方向为从左到右，但是-1步长：从右往左选取
# 如果选取方向（下标开始到结束的方向）和 步长 的方向冲突，则无法选取数据
print(str1[-1: -4: -1])