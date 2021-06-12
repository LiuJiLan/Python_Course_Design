import tkinter


class Page01:
    def __init__(self, screen, settings):
        self.screen = screen
        self.frame = tkinter.Frame(self.screen)
        # 如果frame之后不加任何多余注释则为主frame, 方便于之后的销毁
        # 之后不再注释

        # 主屏设置, 之后不再注释
        self.screen.title(settings.page01_title)
        # self.screen.geometry("{}x{}".format(settings.page01_width, settings.page01_height))
        # screen.configure(bg=settings.page01_bg_color)
        self.frame.pack()

        # 所有的控件都建立在主frame之上
        buttonSignIn = tkinter.Button(self.frame, text="登录", command=self.handle_sign_in)
        buttonSignUp = tkinter.Button(self.frame, text="注册", command=self.handle_sign_up)
        buttonGetLicense = tkinter.Button(self.frame, text="Lince", command=self.get_license)

        # 将所有控件摆放至frame
        # 在组员具体设计前全部使用pack
        buttonSignIn.pack()
        buttonSignUp.pack()
        buttonGetLicense.pack()


    def handle_sign_in(self):
        pass

    def handle_sign_up(self):
        pass

    def get_license(self):
        pass
