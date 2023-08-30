'''
运算符的分类
1. 算数运算符
2. 赋值运算符
3. 复合赋值运算符
4. 比较运算符
5. 逻辑运算符'''

# 算数运算符的优先顺序：() > ** > * / // % > + -

# 赋值运算符 = ，将 = 右侧的结果赋值给左侧的变量
# 单变量赋值
num = 1
print(num)
# 多变量赋值
num1, float1, str1 = 1, 1.2 ,'hello world'  # 多变量依次赋值，左右个数相同
print(float1)
# 多变量赋相同值
a = b = 1
print(a,b)

# 复合赋值运算符（b = b + a == b += a)其余加减乘除的方式相同，执行的顺序是从左到右先加再等于
# 常用 += 和 -=
a = 100
a += 1
print(a)
c = 10
c += 1 + 2  # 运算的顺序是：c += 3 而不是：c + 1 + 2 即先算复合赋值运算符右侧的表达式，而非按顺序进行计算
print(c)

d = 10
d *= 1 + 2  # 运算的顺序是：d *= 3 即 d = 30
print(d)

# 比较运算符，返回布尔值True或False
'''
== 等于
!= 不等于
> 大于
< 小于
>= 大于等于
<= 小于等于'''

a = 0
b = 1
c = 2
# and意思为与：即都真即为真
print(a < b and a < c)
# or意思为：一真即真，都假才假
print(a < b or b > c)
print(a > b or b > c)
# not意思为：取反义的意思
print(not False)  # True
print(not c > b)  # False
print(not(a > b or b > c))  # True

print((a < b) and (a < c))  # True，为什么要加小括号？为了避免歧义，提高运算优先级，更直观

# 拓展：数字之间的逻辑运算
a = 0
b = 1
c = 2
d = 0
# and运算符，只要有一个值为0，则结果为0，否则结果为最后一个非0的数字
print(a and b)  # 0
print(b and c)  # 2
# or运算符，只有所有值为0，结果才为0，否则结果为第一个非0的数字,从左到右从非0开始的数
print(b or c)  # 1
print(a or d)  # 0
print(a or c)  # 2