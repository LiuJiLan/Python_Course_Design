import tkinter
import tkinter.messagebox


class Page02:
    def __init__(self, screen, settings, data_package):
        self.screen = screen
        self.settings = settings
        self.data_package = data_package
        self.frame = tkinter.Frame(self.screen)

        self.screen.title(settings.page02_title)
        self.frame.pack(fill="both")

        # 所有的控件
        labelUserName = tkinter.Label(self.frame, text="用户名:")
        self.entryUserName = tkinter.Entry(self.frame, show=None)
        labelPassword = tkinter.Label(self.frame, text="密码:")
        self.entryPassword = tkinter.Entry(self.frame, show="*")
        buttonSignIn = tkinter.Button(self.frame, text="登录", command=self.handle_sign_in)
        buttonGoBack = tkinter.Button(self.frame, text="返回", command=self.go_back)

        # 暂定放置
        labelUserName.pack()
        self.entryUserName.pack()
        labelPassword.pack()
        self.entryPassword.pack()
        buttonSignIn.pack()
        buttonGoBack.pack()

    def handle_sign_in(self):
        self.data_package.user_name = self.entryUserName.get()
        self.data_package.sign_in_pwd = self.entryPassword.get()

        if self.data_package.page02_does_username_exist():
            if self.data_package.page02_is_pwd_correct():
                if self.data_package.page02_is_administrator():
                    self.frame.destroy()
                    from page08 import Page08
                    Page08(self.screen, self.settings, self.data_package)
                else:
                    self.frame.destroy()
                    from page05 import Page05
                    Page05(self.screen, self.settings, self.data_package)
            else:
                tkinter.messagebox.showinfo(title="对不起", message=self.settings.page02_pwd_is_not_correct)
        else:
            tkinter.messagebox.showinfo(title="对不起", message=self.settings.page02_does_username_exist_message)

    def go_back(self):
        self.frame.destroy()
        from page01 import Page01
        Page01(self.screen, self.settings, self.data_package)
