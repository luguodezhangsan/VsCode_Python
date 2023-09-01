# 将不满足程序逻辑的情况进行反馈
# 抛出自定义异常的语法为 raise 异常类对象
# 需求：密码长度不足，则报异常（用户输入密码，如果输入的长度不足 3 位，则报错，即抛出自定义异常，并捕获该异常）

# 1. 自定义异常类，继承 Exception，魔法方法有 init 和 str（设置异常描述信息）
class ShortInputError(Exception):
    def __init__(self, length, min_len):
        # 用户输入的密码长度
        self.length = length
        # 系统要求的最少长度
        self.min_len = min_len

    # 设置抛出异常的描述信息
    def __str__(self):
        return f'你输入的密码长度是{self.length}，不能少于{self.min_len}个字符'
    
def main():
    try:
        content = input('请输入密码：')
        if len(content) < 3:
            # 2. 抛出异常类创建的对象
            raise ShortInputError(len(content), 3)   # 如果密码长度大于 3 ，则不会执行该行，执行 25，26 行
    except Exception as result:   # 用 except 捕获异常，作为 result，然后再打印异常 ShortInputError
        print(result)
    else:
        print('密码已输入完成')

main()
# 3. 捕获该异常