import tkinter
import tkinter.messagebox
import db_functions as dbf


class Page02:
    def __init__(self, screen, settings, info):
        self.screen = screen
        self.settings = settings
        self.info = info
        self.frame = tkinter.Frame(self.screen)

        self.screen.title(settings.page02_title)
        self.frame.pack(fill="both")

        # 所有的控件
        labeUserName = tkinter.Label(self.frame, text="用户名:")
        self.entryUserName = tkinter.Entry(self.frame, show=None)
        labelPassword = tkinter.Label(self.frame, text="密码:")
        self.entryPassword = tkinter.Entry(self.frame, show="*")
        buttonSignIn = tkinter.Button(self.frame, text="登录", command=self.handle_sign_in)
        buttonGoBack = tkinter.Button(self.frame, text="返回", command=self.go_back)

        # 暂定放置
        labeUserName.pack()
        self.entryUserName.pack()
        labelPassword.pack()
        self.entryPassword.pack()
        buttonSignIn.pack()
        buttonGoBack.pack()

    def handle_sign_in(self):
        userName = self.entryUserName.get()
        password = self.entryPassword.get()
        if dbf.page02_does_username_exist(userName):
            if dbf.page02_is_pwd_correct(userName, password):
                if dbf.page02_is_administrator(userName, password):
                    self.frame.destroy()
                    from page08 import Page08
                    Page08(self.screen, self.settings)
                else:
                    self.frame.destroy()
                    from page05 import Page05
                    Page05(self.screen, self.settings)
            else:
                tkinter.messagebox.showinfo(title="对不起", message=self.settings.page02_pwd_is_not_correct)
        else:
            tkinter.messagebox.showinfo(title="对不起", message=self.settings.page02_does_username_exist_message)

    def go_back(self):
        self.frame.destroy()
        from page01 import Page01
        Page01(self.screen, self.settings)
