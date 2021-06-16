import tkinter
from urllib.request import urlopen
from tkinter import filedialog
import os


class Page01:
    def __init__(self, screen, settings, data_package):
        self.screen = screen
        self.settings = settings
        self.data_package = data_package
        self.frame = tkinter.Frame(self.screen)
        # 如果frame之后不加任何多余注释则为主frame, 方便于之后的销毁
        # 之后不再注释

        # 主屏设置, 之后不再注释
        self.screen.title(self.settings.page01_title)
        # self.screen.geometry("{}x{}".format(settings.page01_width, settings.page01_height))
        # screen.configure(bg=settings.page01_bg_color)
        self.frame.pack(fill="both", expand=1)

        # 所有的控件都建立在主frame之上
        buttonSignIn = tkinter.Button(self.frame, text="登录", command=self.handle_sign_in)
        buttonSignUp = tkinter.Button(self.frame, text="注册", command=self.handle_sign_up)
        buttonGetLicense = tkinter.Button(self.frame, text="Lincense", command=self.get_license)

        # 将所有控件摆放至frame
        # 在组员具体设计前全部使用pack
        buttonSignIn.pack()
        buttonSignUp.pack()
        buttonGetLicense.pack()

    def handle_sign_in(self):
        self.frame.destroy()
        from page02 import Page02
        Page02(self.screen, self.settings, self.data_package)

    def handle_sign_up(self):
        self.frame.destroy()
        from page03 import Page03
        Page03(self.screen, self.settings, self.data_package)

    def get_license(self):
        try:
            url = self.settings.page01_license_url
            with urlopen(url) as (fp):
                content = fp.read().decode()
            target_dir = filedialog.askdirectory()
            os.chdir(target_dir)
            with open("lincense.txt", 'w', encoding='utf8') as (fp):
                fp.write(content)
        finally:
            pass
