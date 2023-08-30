# 坐公交车，如果有钱则可以上车，没有钱则不能上车；上车后有空座，则可以坐下，如果没有空座，就要站着。怎么书写程序？

'''
1. 将来要做判断的数据：钱和座位
2. 判断是否有钱
3. 判断是否能坐下
'''

# money = input('你带钱了吗？（填是或者否）') 
# if money == '是':
#     print('土豪请上车')
#     seat = input('你观察车上有位置吗？（填是或否）')        
#     if seat == '是':
#         print('有座位，请坐下')
#     else:
#         print('没座位，请站着')
# else:
#     print('朋友你没带钱，不能上车！')

'''
猜拳游戏：
'''
print('剪刀石头布游戏！和电脑来一场精彩的pk吧!')
from random import *  # import random
player = eval(input('请出拳：(0--石头、1--剪刀、2--布)'))
computer = randint(0, 2)  # random.randint(0， 2) 引入0-2之间的整数
print(computer)
if ((player == 0 and computer == 1)) or ((player == 1 and computer == 2)) or ((player == 2 and computer == 0)):  # and表示同时,or表示其中之一满足就行
    print('玩家获胜！')
elif player == computer:
    print('别走再来一局！')
else:
    print('电脑获胜！')