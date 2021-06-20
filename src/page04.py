import tkinter
import tkinter.messagebox


class Page04:
    def __init__(self, screen, settings, data_package):
        self.screen = screen
        self.settings = settings
        self.data_package = data_package
        self.frame = tkinter.Frame(self.screen)

        self.screen.title(settings.page04_title)
        self.frame.pack(fill="both", expand=1)

        # 所有的控件
        labelUserName = tkinter.Label(self.frame, text="用户名:")
        self.entryUserName = tkinter.Entry(self.frame, show=None)
        labelPasswordTip = tkinter.Label(self.frame, text=self.settings.page04_password_tip)
        labelPassword = tkinter.Label(self.frame, text="密码:")
        self.entryPassword = tkinter.Entry(self.frame, show="*")
        labelPwdConfirm = tkinter.Label(self.frame, text="密码:")
        self.entryPwdConfirm = tkinter.Entry(self.frame, show="*")
        buttonSignUp = tkinter.Button(self.frame, text="注册", command=self.handle_sign_up)
        buttonGoBack = tkinter.Button(self.frame, text="返回", command=self.go_back)

        # 暂定放置
        self.screen.geometry("480x320")
        labelUserName.place(x=92, y=24, width=113, height=38)
        self.entryUserName.place(x=205, y=24, width=183, height=38)
        labelPasswordTip.place(x=92, y=86, width=296, height=24)
        labelPassword.place(x=92, y=134, width=113, height=38)
        self.entryPassword.place(x=205, y=134, width=183, height=38)
        labelPwdConfirm.place(x=92, y=196, width=113, height=38)
        self.entryPwdConfirm.place(x=205, y=196, width=183, height=38)
        buttonSignUp.place(x=92, y=258, width=113, height=38)
        buttonGoBack.place(x=275, y=258, width=113, height=38)

    def handle_sign_up(self):
        self.data_package.user_name = self.entryUserName.get()
        password = self.entryPassword.get()
        pwdConfirm = self.entryPwdConfirm.get()
        if self.data_package.page04_is_username_already_taken():
            tkinter.messagebox.showinfo(title="对不起", message=self.settings.page04_is_username_already_taken_message)
        else:
            if password == pwdConfirm:
                if self.is_pwd_valid():
                    self.data_package.sign_up_pwd = password
                    self.data_package.page04_complete_regist_action()
                    self.data_package.page04_flush_times()
                    self.data_package.flush_self_variable()
                    # 由于注册和登录是分开的, 注册中的信息用完即可销毁
                    # 此步骤已被移入self.data_package.page04_complete_regist_action()函数中
                    # 移到单独的flush函数中
                    tkinter.messagebox.showinfo(title="谢谢", message=self.settings.page04_pwd_is_valid_message)
                    self.frame.destroy()
                    from page01 import Page01
                    Page01(self.screen, self.settings, self.data_package)
                else:
                    tkinter.messagebox.showinfo(title="对不起", message=self.settings.page04_pwd_is_not_valid_message)
            else:
                tkinter.messagebox.showinfo(title="对不起", message=self.settings.page04_inconsistent_passwords)

    def go_back(self):
        self.frame.destroy()
        from page03 import Page03
        Page03(self.screen, self.settings, self.data_package)

    def is_pwd_valid(self):
        pwd = self.entryPassword.get()
        if (len(pwd) >= 8) and (len(pwd) <= 16):
            return True
        else:
            return False
