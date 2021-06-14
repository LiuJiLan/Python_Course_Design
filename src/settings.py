

class Settings:
    def __init__(self):
        # 主screen设置
        self.screen_title = "Screen"
        self.screen_width = 1200
        self.screen_height = 800
        self.screen_bg_color = "#808080"

        # page的名称设置
        self.page01_title = "Page 1"
        self.page02_title = "Page 2"
        self.page03_title = "Page 3"

        # page01的部分设置
        self.page01_license_url = "http://www.reinstall.cn/SomeAssets/ExampleLincense.txt"

        # page02部分设置
        self.page02_does_username_exist_message = "你的用户名不存在,\n请重新检查或先注册"
        self.page02_pwd_is_not_correct = "你的用户名或密码有误,请重试"

        # page03部分设置
        self.page03_combobox_not_selected = "请先选择身分"
        self.page03_does_id_exist_message = "未查询到你的学工号,请确认或联系管理员."
        self.page03_any_times_left_message = "输入的学工号已经达到创好上限,\n请使用登录功能.\n如仍需创号请联系管理员"
        self.page03_any_times_identity_left_message = "尽管输入的学工号没有达到创好上限,但您不能再已此身份继续创号\n请使用登录功能.\n如仍需创号请联系管理员"