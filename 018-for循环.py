''' 
for 临时变量 in 序列：
    重复执行的代码1
    重复执行的代码2'''

str = 'itheima'
for i in str:
    print(i)

for j in str:
    if j == 'e':
        print('遇到e了不打印了')
        break  # 当某些条件成立时，break使其退出循环
    print(j)

for n in str:
    if n == 'i':
        print('遇到i了不打印了')
        continue  # 当 n == 'i' 时候，n不打印了，即不打印 'i'，则继续输出剩下字符
    print(n)

