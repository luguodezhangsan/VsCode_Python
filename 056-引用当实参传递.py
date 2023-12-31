# 可变和不可变类型的引用都是可以当作实参的
def test1(a):
    print(a)
    print(id(a))

    a += a

    print(a)
    print(id(a))

b = 100
test1(b)
'''
100
2846438806992
200
2846438810256'''
# int: 计算后 id值 不同

c = [11, 22]
test1(c)
# 列表: 计算前后 id值 相同
'''
[11, 22]
2846440391104
[11, 22, 11, 22]
2846440391104'''