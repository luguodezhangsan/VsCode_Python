# P221
# 递归：再遍历一个文件夹里所有文件通常会使用递归实现，再快速排序中也需要，爬虫里面也需要
'''
特点：
1. 函数内部自己调用自己
2. 必须有出口（否则会出现死循环）'''

# 应用：3以内数字累加（3+2+1）
sum = 0
i = 1
while i <= 3:
    sum += i
    i += 1
print(sum)
# 6

# 递归的方法：
def sum_numbers(num):
    # 2. 出口，如果删掉这步，则会报错，接近死循环，该电脑最大递归深度为 996 次
    if num == 1:
        return 1
    # 1. 当前数字 + (当前数字 - 1) 的累加和
    return num + sum_numbers(num - 1)

result = sum_numbers(3)  # = 3 + sum_numbers(2) = 3 + 2 +sum_number(1) = 3 + 2 + 1
print(result)
# 6