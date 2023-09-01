# 共有 4 参数
# 1. 位置参数
def user_info(name, age ,gender):
    print(f'你的名字是{name},年龄是{age},性别是{gender}')
user_info('Tom', 20, '男')
# 你的名字是Tom,年龄是20,性别是男
# 顺序和个数必须和传递的函数一致，否则会导致传递的函数没有意义

# 2. 关键字参数
# 通过 “键 = 值” 的形式加以指定，可以使函数更加清晰，更容易理解
user_info('小明', gender = '男', age = 16)
# 你的名字是小明,年龄是16,性别是男
user_info(gender= '男', age= 20, name= 'Jack')
# 你的名字是Jack,年龄是20,性别是男
# user_info(gender = '男', '小明', age = 16)
# 位置参数和关键字参数并存的情况下，位置参数要放在最前面不然会报错

# 3. 缺省参数（默认参数）
def user_info1(name, age ,gender= '男'):
    print(f'你的名字是{name},年龄是{age},性别是{gender}')
user_info1('Tom', 20)
# 你的名字是Tom,年龄是20,性别是男
user_info1('Rose', 18, '女')  # 这个可以修改默认参数
# 你的名字是Rose,年龄是18,性别是女

# 4. 不定长参数（可变参数）
# 用于不确定多少个参数的场景，此时可以用包裹（packing）位置参数，或者包裹关键字参数，来进行参数传递
# 4.1 包裹位置传递
def user_info2(*args):  # python 底层解释器中接受不定长参数时都是用的 *arg
    print(args)  # print(*arg) 返回的是字符串
user_info2('Tom')
user_info2('Jack', 20)
# ('Tom',)
# ('Jack', 20)
# 返回的都是元组

# 4.2 包裹关键字传递
def user_info3(**kwargs):
    print(kwargs)
user_info3()
# {}
user_info3(name = 'Mary', age = 12, id = 114514)
# {'name': 'Mary', 'age': 12, 'id': 114514}
# 返回的是字典

# 综上，无论是包裹位置传递还是包裹关键字传递，都是一个组包的过程，收集零散数据返回一个整体