import tkinter
import tkinter.messagebox
import db_functions as dbf

class Page03:
    def __init__(self, screen, settings):
        self.screen = screen
        self.settings = settings
        self.frame = tkinter.Frame(self.screen)

        self.screen.title(settings.page03_title)
        self.frame.pack(fill="both")

        # 所有的控件
        labelId = tkinter.Label(self.frame, text="学工号:")
        self.entryId = tkinter.Entry(self.frame, show=None)
        labelPassword = tkinter.Label(self.frame, text="密码:")
        self.entryPassword = tkinter.Entry(self.frame, show="*")
        buttonSignIn = tkinter.Button(self.frame, text="登录", command=self.handle_sign_in)
        buttonGoBack = tkinter.Button(self.frame, text="返回", command=self.go_back)

        # 暂定放置
        labelId.pack()
        self.entryId.pack()
        labelPassword.pack()
        self.entryPassword.pack()
        buttonSignIn.pack()
        buttonGoBack.pack()

    def handle_sign_in(self):
        id = self.entryId.get()
        password = self.entryPassword.get()
        if dbf.page03_does_id_exist(id):
            pass
        else:
            tkinter.messagebox.showinfo(title="对不起", message=self.settings.page03_does_id_exist_message)

    def go_back(self):
        pass