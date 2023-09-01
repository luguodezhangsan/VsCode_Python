# 应用：学员管理系统
'''
需求：进入系统显示系统功能界面，功能如下：
1. 添加学员
2. 删除学员
3. 修改学员信息
4. 查询学员信息
5. 显示所有学员信息
6. 退出系统
系统共 6 个功能，用户根据自己需求选取'''

# 步骤分析：
# 定义功能界面函数：
def info_print():
    print('-' * 20,'请选择功能','-' * 20)
    print('1. 添加学员')
    print('2. 删除学员')
    print('3. 修改学员信息')
    print('4. 查询学员信息')
    print('5. 显示所有学员信息')
    print('6. 退出系统')

# 等待存储所有学员的信息
info = []

# 添加学员信息的函数
def add_info():
    '''添加学员函数'''  # 解释说明，用 help(add_info) 查询函数作用
    # pass    # 不知道函数中写什么时用 pass 占位，避免报错，运行时这个定义函数不会执行
    # 1. 用户输入：学号，姓名，手机号
    new_id = input('输入你的学号：')
    new_name = input('输入你的姓名：')
    new_tel = input('输入你的手机号：')

    # 2. 判断是否添加这个学员：存在则报错，不存在则添加到字典
    global info  # 这里设置为全局变量，但是局部变量里面好像可以执行全局变量嘛   验证是正确的，这步好像并不影响结果输出
    
    # 2.1 判断用户输入的姓名和列表中 name 所对应的值是否相同，是则给与相应提示
    for i in info:
        if new_name == i['name']:
            print('此用户已存在！')
            return  # 这里作用是退出当前函数，避免执行 2.2 内容来添加学员信息

    # 2.2 准备空字典，增添数据，列表追加字典
    info_dict = {}

    # 字典增加新数据，旧数据更换为新数据；没数据则添加数据
    info_dict['id'] = new_id
    info_dict['name'] = new_name
    info_dict['tel'] = new_tel
    # print(info_dict)    

    # 列表增加数据
    info.append(info_dict)
    print(info)

# 删除学员的函数
def del_info():
    '''删除学员的函数'''
    # 1. 用户输入要删除的学员姓名
    del_name = input('请输入要删除学员的姓名：')

    # 2. 判断学员是否存在：存在则删除，不存在则提示
    # 2.1 声明 info 为全局变量
    global info

    # 2.2 遍历列表
    # 2.3 判断学员是否存在：存在则执行删除（列表里的字典）.break：这个系统不允许重名，删除了一个后面的不需要遍历；不存在则提示
    for i in info:
        if del_name == i['name']:
            info.remove(i)
            break
    else:  # 如果遍历了所有的信息发现用户信息不存在，则选择 else，如果缩进到 if 那一个级别，则每遍历一个 i 就会输入一次：'这个学员不存在！'
        print('这个学员不存在！')
    print(info)

# 修改学员信息函数
def modify_info():
    '''修改学员信息函数'''
    # 1. 用户输入学员想要修改的姓名
    modify_name = input('请输入要修改的学员姓名：')
    # 2. 判断学员是否存在：存在则修改手机号；不存在则提示
    # 2.1 声明 info 是全局变量
    global info

    # 2.2 遍历列表，判断输入用户的姓名
    for i in info:
        if modify_name == i['name']:
            i['tel'] = input('请输入新的电话号码：')
            break
    else:
        print('这个学员不存在！')
    
    # 2.3 打印 info 判断信息是否修改成功
    print(info)

# 查询学员信息
def search_info():
    '''查询学员信息函数'''
    search_name = input('请你输入要查找的学员姓名：')
    global info
    for i in info:
        if search_name == i['name']:
            print('查询到的学员信息如下：','-' * 20)
            print(f"该学员的学号是{i['id']}，姓名是{i['name']}，手机号是{i['tel']}")  # 这里要用双引号，避免和里面的单引号发生冲突
            break
    else:
        print('这个学员不存在！')

# 打印所有学员信息的函数
def print_all():
    '''显示所有学员信息'''
    print('学号\t姓名\t电话')
    global info
    for i in info:
        print(f"{i['id']}\t{i['name']}\t{i['tel']}")


# 系统功能要循环使用，直到用户输入 6 结束系统（需要用 while True）
while True:
    # 1. 显示功能界面
    info_print()

    # 2. 用户输入功能序号
    user_num = int(input('请输入功能序号：'))

    # 3. 按照用户输入的功能序号，执行不同的功能
    # 如果用户输入：1. ...2. ....
    if user_num == 1:
        print('添加学员')
        add_info()

    elif user_num == 2:
        print('删除学员')
        del_info()

    elif user_num == 3:
        print('修改学员信息')
        modify_info()

    elif user_num == 4:
        print('查询学员信息')
        search_info()

    elif user_num == 5:
        print('显示所有学员信息')
        print_all()

    elif user_num == 6:
        print('退出系统')
        exit_flag = input('确定要退出吗？请输入 yes or no：')
        if exit_flag == 'yes':
            break  # 执行结束，结束 while True 循环

    else:
        print('输入有误，请重新输入：')

# 添加学员
'''
1. 接受用户输入学员信息，并保存
2. 判断是否添加学员信息
    2.1 如果学员姓名已经存在，则报错提示
    2.2 如果学员姓名不存在，则准备空字典，将用户输入的数据添加到字典当中，再将列表追加字典数据
3. 对应的 if 条件成立的位置调用该函数'''

# 删除学员
'''
1. 用户输入学员姓名
2. 检查这个学员是否存在
    2.1 如果存在，则从列表中删除这个数据
    2.2 如果不存在，则提示“该用户不存在”
3. 对应if条件成立的位置调用该函数'''

# 修改学员信息
'''
1. 用户输入目标学员姓名
2. 检查这个学员是否存在
    2.1 如果存在，则修改这学员的信息，例如手机号
    2.2 如果不存在，则报错
3. 对应if条件成立时调用该函数'''

# 查询学员信息
'''
1. 用户输入目标学员姓名
2. 检查这个学员是否存在
    2.1 如果存在，显示这个学员信息
    2.2 如果不存在，则报错
3. 对应if条件成立时调用该函数'''

# 显示所有学员信息
'''
1. print() 打印所有学员信息'''