"""
这份文件专门存放一些函数
这些函数用于处理整个程序转跳中的较为复杂的逻辑
同时在服务器搭建前充当了调试的任务
逻辑函数,相当于一个抽象的接口,屏蔽与SQL联系的细节
"""


def page02_does_username_exist(userName):
    return True


def page02_is_pwd_correct(userName, password):
    return True


def page02_is_administrator(userName, password):
    return True


def page03_does_id_exist(id):
    return True

def page03_any_times_left(id):
    return True

def page03_any_times_identity_left(id, identity):
    # identity为"管理员"或"学生"
    return True