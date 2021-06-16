import tkinter


class Pagexx:
    def __init__(self, screen, settings, data_package):
        self.screen = screen
        self.settings = settings
        self.data_package = data_package
        self.frame = tkinter.Frame(self.screen)

        self.screen.title(settings.pagexx_title)
        self.frame.pack(fill="both", expand=1)

        # 所有的控件
        labelMessage = tkinter.Label(self.frame, text="这是一个测试用例")
        buttonTestButton = tkinter.Button(self.frame, text="测试按钮", command=self.test)
        buttonGoBack = tkinter.Button(self.frame, text="返回", command=self.go_back)

        # 暂定放置
        labelMessage.pack()
        buttonTestButton.pack()
        buttonGoBack.pack()

    def test(self):
        tkinter.messagebox.showinfo(title="TEST", message="这是一个测试按钮")

    def go_back(self):
        self.frame.destroy()
        from page08 import Page08
        Page08(self.screen, self.settings, self.data_package)