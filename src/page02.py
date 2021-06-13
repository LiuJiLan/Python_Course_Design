import tkinter


class Page02:
    def __init__(self, screen, settings):
        self.screen = screen
        self.settings = settings
        self.frame = tkinter.Frame(self.screen)

        self.screen.title(settings.page02_title)
        self.frame.pack()

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
        user_name = self.entryUserName.get()
        password = self.entryPassword.get()


    def go_back(self):
        pass
