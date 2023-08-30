# 循环的分类为：while 和 for 两种

# 需求：重复打印5次，媳妇2我错了

i = 0  # 红点表示debug运行测试开始点，可以用debug中的上下依次执行流程！
while i <= 4:  # while i < 5，最好！  
    print('媳妇我错了！')
    i += 1

# 工作中循环计数器开始一般取0，而不是1

print('原谅你了！')

# while的应用：
# 1-100的累加：
num = 1
result = 0
while num <= 100:
    result += num
    num += 1
print(result)

# 1-100之间的偶数做累加：
# 方法一：用余数来决定是否累加
num2 = 1
result2 = 0
while num2 <= 100:
    if num2 % 2 == 0:
        result2 += num2
        num2 += 1
    else:
        num2 += 1  # else 这部分可以去掉，把if中 num2 += 1 缩进提前
print(result2)
# 方法二：用计数器控制，这是人脑计算出的2进行累加，不是计算机计算的，不够好，应该全部交给程序来进行计算
num3 = 0
result3 = 0
while num3 <= 100:
    result3 += num3  # 如果num3 在这一行则result3开始值是2，而不是开始赋值的0了，会导致多一次运算（交换38和39行）
    num3 += 2  # 这个不能去掉，否则num3取值一直都是 < 2,会一直累加，会陷入死循环！要手动结束循环，否则会导致电脑cpu和内存增加，卡死计算机。
print(result3)

# break 和 continue 的运用
# break 吃5个苹果，吃到第3个苹果就吃饱了，后面的就不吃了（当条件成立时，后面条件不需要执行停止使用break）
# continue 吃5个苹果，吃到第3个苹果吃出条虫子，第三个就不吃了，接着吃第4.5个（当条件成立时，不执行该条件，继续执行下一个循环代码，使用continue）
# break 的运用：
i = 1
while i <= 5:
    if i == 4:
        print('吃饱了，不吃了！')
        break
    else:
        print(f'吃了第{i}个苹果。')
    i += 1
# continue 的运用：
j = 1
while j <= 5:
    if j == 3:
        print('吃出个大虫子，这个苹果不吃了！')
        # continue 之前一定要加入计数器，否则进入死循环
        j += 1
        continue  # 这里的 continue 使得 j += 1 一直没用执行，所以 j == 3，使得 print('吃出个大虫子，这个苹果不吃了！') 一直执行。
        #continue 使得后面几行程序不执行，直接回到 while 去了
    else:
        print(f'吃了{j}个苹果。')
    j += 1  # 这里缩进还是不缩进结果都是一样的



