import tkinter

class Page14:
    def __init__(self, screen, settings, data_package):
        self.screen = screen
        self.settings = settings
        self.data_package = data_package
        self.frame = tkinter.Frame(self.screen)

        self.screen.title(settings.page14_title)
        self.frame.pack(fill="both", expand=1)

        # 写缓存
        self.data_package.get_selected_book_info()

        # 所有的控件
        buttonConfirmAdd = tkinter.Button(self.frame, text="确认增加", command=self.comfirm_add)
        buttonGoBack = tkinter.Button(self.frame, text="返回", command=self.go_back)
        labelNewTitle = tkinter.Label(self.frame, text="新书名: ")
        self.entryNewTitle = tkinter.Entry(self.frame, show=None)
        labelNewAuthor = tkinter.Label(self.frame, text="新作者: ")
        self.entryNewAuthor = tkinter.Entry(self.frame, show=None)
        labelNewBriefIntro = tkinter.Label(self.frame, text="新书本简介: ")
        self.entryNewBriefIntro = tkinter.Entry(self.frame, show=None)

        # 暂定放置
        buttonConfirmAdd.pack()
        buttonGoBack.pack()
        labelNewTitle.pack()
        self.entryNewTitle.pack()
        labelNewAuthor.pack()
        self.entryNewAuthor.pack()
        labelNewBriefIntro.pack()
        self.entryNewBriefIntro.pack()

    def comfirm_add(self):
        self.data_package.generate_new_unique_code()
        self.data_package.new_book_info = (self.entryTitle.get(), self.entryAuthor.get(), self.entryNewBriefIntro.get())
        self.data_package.create_new_one()
        self.data_package.flush_self_variable()
        from page12 import Page12
        Page12(self.screen, self.settings, self.data_package)

    def go_back(self):
        self.data_package.new_one = ""
        self.data_package.new_book_info = ()
        self.frame.destroy()
        from page09 import Page09
        Page09(self.screen, self.settings, self.data_package)
