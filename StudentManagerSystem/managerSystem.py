'''
需求：
1. 存储数据位置：文件(student.data)
    加载文件数据
    （系统功能循环使用）
    显示菜单功能
    用户输入功能序号
    根据用户输入的功能序号执行不同的功能
    修改数据后保存到文件
2. 存储数据的形式：列表存储学员对象
3. 系统功能
    添加学员
    删除学员
    修改学员
    查询学员信息
    保存学员信息'''

from student import *
class StudentManager(object):
    def __init__(self):
        # 存储数据所用的列表
        self.student_list = []

    # 一. 程序入口，启动程序后执行的函数
    def run(self):
        # 1. 加载学员信息
        self.load_student()

        while True:
            # 2. 显示功能菜单
            self.show_menu()

            # 3. 用户输入功能序号
            menu_num = int(input('请输入你需要的功能序号：'))

            # 4. 根据用户输入的功能序号不同执行不同的功能
            if menu_num == 1:
                # 添加学员
                self.add_student()

            elif menu_num == 2:
                # 删除学员
                self.del_student()

            elif menu_num == 3:
                # 修改学员信息
                self.modify_student()

            elif menu_num == 4:
                # 查询学员信息
                self.search_student()

            elif menu_num == 5:
                # 显示所有学员信息
                self.show_student()

            elif menu_num == 6:
                # 保存学员信息
                self.save_student()

            elif menu_num == 7:
                # 退出系统
                break
            
            else:
                print('输入有误，请重新输入！')

    # 二. 系统功能函数
    # 2.1 显示功能菜单  -- 打印序号的功能对应关系 --
    @staticmethod
    def show_menu():
        print('请选择如下功能：')
        print('1. 添加学员')
        print('2. 删除学员')
        print('3. 修改学员信息')
        print('4. 查询学员信息')
        print('5. 显示所有学员信息')
        print('6. 保存学员信息')
        print('7. 退出系统')
    
    # 2.2 添加学员
    def add_student(self):
        # 1. 用户输入姓名、性别、手机号
        name = input('请输入你的姓名：')
        gender = input('请输入你的性别：')
        tel = input('请输入你的手机号：')

        # 2. 创建学员对象 --> 类在 student 内， 在最顶部导入 student 对象，再创建对象
        student = Student(name, gender, tel)

        # 3. 将该对象添加到学员列表
        self.student_list.append(student)

        # 4. 验证代码
        print(self.student_list)
        print(student)

    # 2.3 删除学员
    def del_student(self):
        # 1. 删除学员：删除指定姓名的学员
        del_name = input('请输入要删除的学员的姓名：')

        # 2. 如果用户输入的目标学员存在则删除，否则提示学员不存在
        for i in self.student_list:
            if i.name == del_name:
                self.student_list.remove(i)
                print('删除成功！')
                break
        else:
            print('查无此人！')

        # 3. 验证代码
        print(self.student_list)

    # 2.4 修改学员信息
    def modify_student(self):
        # 1. 用户输入目标学员姓名
        modify_name = input('请输入你要修改的学员姓名：')
        # 2. 如果用户输入的目标学员存在则修改姓名、性别、手机号等数据，否则提示学员不存在
        for i in self.student_list:
            if i.name == modify_name:
                i.name = input('请输入学员的姓名：')
                i.gender = input('请输入学员的性别：')
                i.tel = input('请输入学员手机号：')
                print(f'修改该学员信息成功，姓名{i.name}, 性别{i.gender}, 手机号{i.tel}。')
                break
        else:
            print('查无此人！')


    # 2.5 查询学员信息
    def search_student(self):
        # 1. 用户输入目标学员姓名
        search_name = input('请输入要查询的学员的姓名：')

        # 2. 如果用户输入的目标学员存在，则打印学员信息，否则提示学员不存在
        for i in self.student_list:
            if i.name == search_name:
                print(f'你所查询的学员信息为：姓名: {i.name}, 性别: {i.gender}, 手机号: {i.tel}')
                break
        else:
            print('查无此人！')


    # 2.6 显示所有学员信息
    def show_student(self):
        print('姓名 \t 性别 \t 手机号')
        for i in self.student_list:
            print(f'{i.name} \t {i.gender} \t {i.tel}')
    
    # 2.7 保存学员信息
    def save_student(self):
        # 需求：将修改后的学员数据保存到存储数据的文件中
        # 步骤：
        # 1. 打开文件
        f = open('student.data', 'w')

        # 2. 文件写入学员数据
        # 注意1：文件写入的数据不能是学员对象的内存地址，需要把学员数据转化为列表的字典数据再做存储
        new_list = [i.__dict__ for i in self.student_list]
        # [{'name': 'aa', 'gender': 'nv', 'tel': '123'}]

        # 注意2：文件内数据要求为字符串类型，故需要先转换数据类型为字符串才能文件写入数据
        f.write(str(new_list))

        # 3. 关闭文件
        f.close()

        print('学员信息已成功储蓄到 student.data')

    # 2.8 加载学员信息
    # 需求：每次进入系统后，修改的数据是文件里面的数据
    def load_student(self):
        # 尝试以 “r” 模式打开数据文件，文件不存在则提示用户；文件存在（没有异常）则读取数据
        # 1. 打开文件：尝试 r 打开，如果有异常 w
        try:
            f = open('student.data', 'r')  # 有则打开
        except:
            f = open('student.data', 'w')  # 没有则创建
        else:
        # 2. 读取数据：文件读取出的数据是字符串，还原为列表类型：[{}] 转换为 []
            data = f.read()
            new_list = eval(data)  # 将字符串转换为原本类型，转换为列表加字典类型[{}] 
            self.student_list = [Student(i['name'], i['gender'], i['tel']) for i in new_list]  # [{}] 转换为 []
        finally:
        # 3. 关闭文件
            f.close()
