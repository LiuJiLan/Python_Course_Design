class Package:
    def __init__(self):
        # 注册用信息
        self.id = ""  # 学工号
        self.authority = ""  # 选择的身份, 原为identity, 为放置与id弄混而重命名
        self.sign_up_pwd = ""  # 注册时的密码, 与登录时的密码进行区分

        # 用户信息
        self.user_name = ""
        self.sign_in_pwd = ""
        # 以后可以改进的地方, 操作时要调取用户信息看有没有权限

        # 用于搜索与结果在列表中展示
        self.search_key_words = []
        """
        res中的项为一个元组, 元组中包含了书本的信息
        注意只包含三个信息:(UniqueCode(Key), BookName, Author)
        内容的详见SQL设计
        """
        self.res = [("1", "2", "3")]
        self.last_visited_location = -1  # 用于记录上次访问的位置, 如为-1就不设置

        self.selected_one = ""  # 记录选中的书的UniqueCode(Key)






    def page02_does_username_exist(self):
        """
        :param userName:
        :return:
        """
        return True

    def page02_is_pwd_correct(self):
        """
        :param userName:
        :param password:
        :return:
        """
        return True

    def page02_is_administrator(self):
        """
        :param userName:
        :param password:
        :return:
        """
        return True

    def page03_does_id_exist(self):
        """
        :param id:
        :return:
        """
        return True

    def page03_any_times_left(self):
        """
        :param id:
        :return:
        """
        return True

    def page03_any_times_identity_left(self):
        """
        :param id:
        :param identity:
        :return:
        """
        # identity为"管理员"或"学生"
        return True

    def page04_is_username_already_taken(self, userName):
        """
        :param userName:
        :return:
        """
        return False

    """
    def page04_is_pwd_valid(self, password):
        # 这个函数只用处理来自外部的数据,
        # 其实可以考虑搬出去
        return True
    # 已移动到Page04
    """

    def page04_complete_regist_action(self):
        pass
        # 由于注册和登录是分开的, 注册中的信息用完即可销毁
        self.id = ""
        self.authority = ""
        self.sign_up_pwd = ""
        self.user_name = ""

    def search_from_db(self):
        """
        :param key_words:
        :return:
        """
        # 此函数在page05和page08里公用
        self.res = []
        if len(self.search_key_words) == 0:
            # 如果没有任何输入直接认为没有搜索结果
            pass
        else:
            # 此处的pass是临时的占位符
            pass
        self.search_key_words = []
        # 此函数不返回, 直接通过res来读取读取
