import datetime
import random
# import cryptography
import pymysql  # 缺少cryptography包, 如有异常报错需要添加这个这个包



class Package:
    def __init__(self):
        self.connect = None
        try:
            self.connect = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='Wxxsh314', db='pycd_sc')
            # 此处如果链接失败会直接退出
        except Exception as e:
            import tkinter.messagebox
            error_message = "与数据库链接出现以下错误: \n"
            tkinter.messagebox.showerror(title="致命错误", message=error_message + str(e))
            quit()
        finally:
            pass

        """
        if self.connect is None:
            import tkinter
            import tkinter.messagebox
            temp_screen = tkinter.Tk()
            error_message = "与数据库链接出现错误"
            tkinter.messagebox.showerror(title="致命错误", message=error_message)
            temp_screen.quit()
            quit()  # 这里需要改进, quit会不给任何提示的掐掉程序
        else:
            pass
            """

        # 注册用信息
        self.id = ""  # 学工号
        self.authority = ""  # 选择的身份, 原为identity, 为放置与id弄混而重命名
        self.sign_up_pwd = ""  # 注册时的密码, 与登录时的密码进行区分

        # 用户信息
        # user_name是登录与注册公用的
        self.user_name = ""
        self.sign_in_pwd = ""
        self.sign_in_authority = 1
        # 以后可以改进的地方, 操作时要调取用户信息看有没有权限

        # 用于搜索与结果在列表中展示
        self.search_key_words = []
        """
        res中的项为一个元组, 元组中包含了书本的信息
        注意只包含三个信息:(UniqueCode(Key), BookName, Author)
        内容的详见SQL设计
        """
        self.res = []
        self.last_visited_location = -1  # 用于记录上次访问的位置, 如为-1就不设置

        # 具体到一本书
        self.selected_one = ""  # 记录
        self.selected_book_info = ("NULL", "NULL", "NULL")
        # (BookName, Author, BriefIntroduction)

        # 新信息
        self.new_one = ""  # 记录选中的书的UniqueCode(Key)
        self.new_book_info = ("NULL", "NULL", "NULL")

        # (BookName, Author, BriefIntroduction)

    def generate_new_unique_code(self):
        self.new_one = datetime.datetime.now().strftime('%Y%m%d%H%M%S%f') + str(random.randint(0, 9)) + str(
            random.randint(0, 9))

    def create_new_one(self):
        sql = "INSERT INTO books_info (uni_code, book_name, author, brief_intro) VALUES ('{0}','{1}', '{2}', '{3}')".format(self.new_one, self.new_book_info[0], self.new_book_info[1], self.new_book_info[2])
        try:
            with self.connect.cursor() as cursor:
                cursor.execute(sql)
            self.connect.commit()
        except Exception as e:
            self.connect.rollback()
        finally:
            pass

    def delete_old_one(self):
        sql = "DELETE FROM books_info WHERE uni_code = '{0}'".format(self.selected_one)
        try:
            with self.connect.cursor() as cursor:
                cursor.execute(sql)
            self.connect.commit()
        except Exception as e:
            self.connect.rollback()
        finally:
            pass

    def flush_self_variable(self):
        self.id = ""
        self.authority = ""
        self.sign_up_pwd = ""
        self.user_name = ""
        self.sign_in_pwd = ""
        self.sign_in_authority = 1
        self.search_key_words = []
        self.res = []
        self.last_visited_location = -1
        self.selected_one = ""
        self.selected_book_info = ("NULL", "NULL", "NULL")
        self.new_one = ""
        self.new_book_info = ("NULL", "NULL", "NULL")

    def page02_does_username_exist(self):
        sql = "SELECT * FROM user_info WHERE user_name = '{0}'".format(self.user_name)
        result = None
        try:
            with self.connect.cursor() as cursor:
                cursor.execute(sql)
                result = cursor.fetchone()
        finally:
            pass
        ret = False
        if result is None:
            pass
        else:
            ret = True
        return ret

    def page02_is_pwd_correct(self):
        sql = "SELECT * FROM user_info WHERE user_name = '{0}'".format(self.user_name)
        result = None
        try:
            with self.connect.cursor() as cursor:
                cursor.execute(sql)
                result = cursor.fetchone()
        finally:
            pass
        ret = False
        if result is None:
            pass
        else:
            if self.sign_in_pwd == result[1]:
                ret = True
                self.sign_in_authority = result[2]  # 密码正确就设置权限
        return ret

    def page02_is_administrator(self):
        if self.sign_in_authority == 0:
            return True
        else:
            return False

    def page03_does_id_exist(self):
        sql = "SELECT * FROM school_info WHERE user_id = '{0}'".format(self.id)
        result = None
        try:
            with self.connect.cursor() as cursor:
                cursor.execute(sql)
                result = cursor.fetchone()
        finally:
            pass
        ret = False
        if result is None:
            pass
        else:
            ret = True
        return ret

    def page03_any_times_left(self):
        sql = "SELECT * FROM school_info WHERE user_id = '{0}'".format(self.id)
        result = None
        try:
            with self.connect.cursor() as cursor:
                cursor.execute(sql)
                result = cursor.fetchone()
        finally:
            pass
        ret = False
        if result is None:
            pass
        else:
            if (result[1] + result[2]) > 0:
                ret = True
        return ret

    def page03_any_times_identity_left(self):
        sql = "SELECT * FROM school_info WHERE user_id = '{0}'".format(self.id)
        result = None
        try:
            with self.connect.cursor() as cursor:
                cursor.execute(sql)
                result = cursor.fetchone()
        finally:
            pass
        ret = False
        if result is None:
            pass
        else:
            if self.authority == "管理员":
                if result[1] > 0:
                    ret = True
            elif self.authority == "学生":
                if result[2] > 0:
                    ret = True
        return ret

    def page04_is_username_already_taken(self):
        sql = "SELECT * FROM user_info WHERE user_name = '{0}'".format(self.user_name)
        result = None
        try:
            with self.connect.cursor() as cursor:
                cursor.execute(sql)
                result = cursor.fetchone()
        finally:
            pass
        ret = True
        if result is None:
            ret = False
        return ret

    def page04_complete_regist_action(self):
        auth = 1
        if self.authority == "管理员":
            auth = 0
        elif self.authority == "学生":
            auth = 1
        sql = "INSERT INTO user_info (user_name, pwd, authority, user_id) VALUES ('{0}','{1}', '{2}', '{3}')".format(self.user_name, self.sign_up_pwd, auth, self.id)
        try:
            with self.connect.cursor() as cursor:
                cursor.execute(sql)
            self.connect.commit()
        except Exception as e:
            self.connect.rollback()
        finally:
            pass

    def page04_flush_times(self):
        sql = "SELECT * FROM school_info WHERE user_id = '{0}'".format(self.id)
        result = None
        try:
            with self.connect.cursor() as cursor:
                cursor.execute(sql)
                result = cursor.fetchone()
        finally:
            pass
        if self.authority == "管理员":
            identy = "admin_times"
            times = result[1] - 1
        elif self.authority == "学生":
            identy = "guest_times"
            times = result[2] - 1
        sql = "UPDATE school_info SET {0} = {1}  WHERE user_id = {2}".format(identy, times, self.id)
        try:
            with self.connect.cursor() as cursor:
                cursor.execute(sql)
            self.connect.commit()
        except Exception as e:
            self.connect.rollback()
        finally:
            pass

    def search_from_db(self):
        # 此处是将所有关键词放进去搜索, 真正的情况是分开搜索
        # 未来可以改进
        result_set = set()
        self.res = []
        if len(self.search_key_words) == 0:
            pass
        else:
            for item in self.search_key_words:
                sql = "SELECT * from books_info  WHERE book_name  LIKE '%{}%';".format(item)
                try:
                    with self.connect.cursor() as cursor:
                        cursor.execute(sql)
                        select_result = cursor.fetchall()
                        for result_one in select_result:
                            result_set.add(result_one)
                except Exception as e:
                    pass
                finally:
                    pass

                sql = "SELECT * from books_info  WHERE author  LIKE '%{}%';".format(item)
                try:
                    with self.connect.cursor() as cursor:
                        cursor.execute(sql)
                        select_result = cursor.fetchall()
                        for result_one in select_result:
                            result_set.add(result_one)
                except Exception as e:
                    pass
                finally:
                    pass

                sql = "SELECT * from books_info  WHERE brief_intro  LIKE '%{}%';".format(item)
                try:
                    with self.connect.cursor() as cursor:
                        cursor.execute(sql)
                        select_result = cursor.fetchall()
                        for result_one in select_result:
                            result_set.add(result_one)
                except Exception as e:
                    pass
                finally:
                    pass

        self.search_key_words = []
        for item in result_set:
            self.res.append((item[0], item[1], item[2]))

    def get_selected_book_info(self):
        sql = "SELECT * FROM books_info WHERE uni_code = '{0}'".format(self.selected_one)
        result = None
        try:
            with self.connect.cursor() as cursor:
                cursor.execute(sql)
                result = cursor.fetchone()
        finally:
            pass
        self.selected_book_info = ("NULL", "NULL", "NULL")
        if result is None:
            pass
        else:
            self.selected_book_info = (result[1], result[2], result[3])

    def page08_get_all_from_db(self):
        sql = "SELECT * from books_info"
        try:
            with self.connect.cursor() as cursor:
                cursor.execute(sql)
                select_result = cursor.fetchall()
                for item in select_result:
                    self.res.append((item[0], item[1], item[2]))
        except Exception as e:
            pass
        finally:
            pass
