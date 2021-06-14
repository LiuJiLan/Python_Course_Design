import tkinter
import tkinter.messagebox
import db_functions as dbf


class Page04:
    def __init__(self, screen, settings, data_package):
        self.screen = screen
        self.settings = settings
        self.data_package = data_package
        self.frame = tkinter.Frame(self.screen)

        self.screen.title(settings.page04_title)
        self.frame.pack(fill="both")

        # 所有的控件
        labeUserName = tkinter.Label(self.frame, text="用户名:")
        self.entryUserName = tkinter.Entry(self.frame, show=None)
        labelPasswordTip = tkinter.Label(self.frame, text=self.settings.page04_password_tip)
        labelPassword = tkinter.Label(self.frame, text="密码:")
        self.entryPassword = tkinter.Entry(self.frame, show="*")
        labelPwdConfirm = tkinter.Label(self.frame, text="密码:")
        self.entryPwdConfirm = tkinter.Entry(self.frame, show="*")
        buttonSignUp = tkinter.Button(self.frame, text="注册", command=self.handle_sign_up)
        buttonGoBack = tkinter.Button(self.frame, text="返回", command=self.go_back)

        # 暂定放置
        labeUserName.pack()
        self.entryUserName.pack()
        labelPasswordTip.pack()
        labelPassword.pack()
        self.entryPassword.pack()
        labelPwdConfirm.pack()
        self.entryPwdConfirm.pack()
        buttonSignUp.pack()
        buttonGoBack.pack()

    def handle_sign_up(self):
        userName = self.entryUserName.get()
        password = self.entryPassword.get()
        pwdConfirm = self.entryPwdConfirm.get()
        if dbf.page04_is_username_already_taken(userName):
            tkinter.messagebox.showinfo(title="对不起", message=self.settings.page04_is_username_already_taken_message)
        else:
            if password == pwdConfirm:
                if dbf.page04_is_pwd_valid(password):
                    dbf.page04_complete_regist_action(userName, password, self.data_package.id,
                                                      self.data_package.identity)
                    # 由于注册和登录是分开的, 注册中的信息用完即可销毁
                    self.data_package.id = ""
                    self.data_package.identity = ""
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
