import os
import sys


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

        # 具体到一本书
        self.selected_one = ""  # 记录选中的书的UniqueCode(Key)
        self.selected_book_info = ()
        # (BookName, Author, BriefIntroduction)

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
        self.res = []  # 由于逻辑设计, 此处可以直接刷新
        if len(self.search_key_words) == 0:
            # 如果没有任何输入直接认为没有搜索结果
            pass
        else:
            # 此处的pass是临时的占位符
            pass
        self.search_key_words = []

        # 此函数不返回, 直接通过res来读取读取

    """
    def write_pic_2_temp(self):
        # 此函数在page07和page10里公用
        work_dir = os.getcwd()
        temp_dir = work_dir + "/temp"
        if not os.path.exists(temp_dir):
            os.mkdir(temp_dir)
        # 从服务器获取
        path = self.selected_one + ".bmp"
        contrnt = ...
        with open(path, 'wb', encoding='utf8') as (fp):
            fp.write(content)
        return path
        path = temp_dir + "/test"
        return path
    """

    def get_selected_book_info(self):
        # 从服务器取得
        self.selected_book_info = ("他改变了中国：江泽民传", "美罗伯特•劳伦斯•库恩",
                                   "《他改变了中国：江泽民传》，2005年中文版、英文版全球同步发行。该书是一部人物传记，作者为美国作家罗伯特·劳伦斯·库恩（Robert Lawrence Kuhn），中文翻译本署名“谈峥，于海江等”。作者长期关注中国，关注江泽民，并向江泽民的亲属、好友及有关工作人员进行了深入细致的采访，掌握了大量第一手资料，在此基础上写成本书。")

    def page08_get_all_from_db(self):
        self.res = []  # 由于逻辑设计, 此处可以直接刷新
        # 此函数不返回, 直接通过res来读取读取

