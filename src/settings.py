
class Settings:
    def __init__(self):
        # 主screen设置
        self.screen_title = "Screen"
        self.screen_width = 1200
        self.screen_height = 800
        self.screen_bg_color = "#808080"

        # page Title设置
        self.page01_title = "Page 1"
        self.page02_title = "Page 2"
        self.page03_title = "Page 3"
        self.page04_title = "Page 4"
        self.page05_title = "Page 5"
        self.page06_title = "Page 6"
        self.page07_title = "Page 7"
        self.page08_title = "Page 8"
        self.page09_title = "Page 9"
        self.page10_title = "Page 10"
        self.page11_title = "Page 11"
        self.page12_title = "Page 12"
        self.pagexx_title = "Page xx"

        # page01设置
        self.page01_license_url = "http://www.reinstall.cn/SomeAssets/ExampleLincense.txt"

        # page02设置
        self.page02_does_username_exist_message = "你的用户名不存在,\n请重新检查或先注册"
        self.page02_pwd_is_not_correct = "你的用户名或密码有误,请重试"

        # page03设置
        self.page03_combobox_not_selected = "请先选择身分"
        self.page03_does_id_exist_message = "未查询到你的学工号,请确认或联系管理员."
        self.page03_any_times_left_message = "输入的学工号已经达到创好上限,\n请使用登录功能.\n如仍需创号请联系管理员"
        self.page03_any_times_identity_left_message = "尽管输入的学工号没有达到创好上限,但您不能再已此身份继续创号\n请使用登录功能.\n如仍需创号请联系管理员"

        # page04设置
        self.page04_password_tip = "密码提示@@@未完成"
        self.page04_is_username_already_taken_message = "用户名已被占用,请换一个"
        self.page04_pwd_is_valid_message = "恭喜您注册成功"
        self.page04_pwd_is_not_valid_message = "您输入的密码不合规,请重新输入"
        self.page04_inconsistent_passwords = "两次密码不一致"

        # page05设置
        self.page05_get_0_res = "没有查找到相关信息.\n如有需要请咨询管理员"

        # page06设置
        self.page06_number_of_res_is_zero = "没有找到相关信息"
        self.page06_no_location_selected_message = "请先选择一条项目"

        # page07设置

        # page08设置
        # 输入 "True" "False"
        self.page08_allow_test_functions = "False"
        self.page08_do_not_allow_test_message = "测试功能未开启,\n请联系管理者或程序开发者"
