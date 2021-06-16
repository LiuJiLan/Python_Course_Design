import tkinter
import tkinter.scrolledtext
import tkinter.messagebox

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
        self.scrolledtextNewBriefIntro = tkinter.scrolledtext.ScrolledText(self.frame)

        # 暂定放置
        buttonConfirmAdd.place(width=282, height=48, x=230, y=64)
        buttonGoBack.place(width=282, height=48, x=688, y=64)
        labelNewTitle.place(width=282, height=48, x=230, y=152)
        self.entryNewTitle.place(width=458, height=48, x=512, y=152)
        labelNewAuthor.place(width=282, height=48, x=230, y=240)
        self.entryNewAuthor.place(width=458, height=48, x=512, y=240)
        labelNewBriefIntro.place(width=282, height=48, x=230, y=328)
        self.scrolledtextNewBriefIntro.place(width=740, height=360, x=230, y=376)

    def comfirm_add(self):
        self.data_package.generate_new_unique_code()
        self.data_package.new_book_info = (self.entryNewTitle.get(), self.entryNewAuthor.get(), self.scrolledtextNewBriefIntro.get(1.0, tkinter.END))
        self.data_package.create_new_one()
        self.data_package.flush_self_variable()
        tkinter.messagebox.showinfo(title="请注意", message=self.settings.page14_finish_add)
        self.frame.destroy()
        from page08 import Page08
        Page08(self.screen, self.settings, self.data_package)

    def go_back(self):
        self.data_package.new_one = ""
        self.data_package.new_book_info = ()
        self.frame.destroy()
        from page09 import Page09
        Page09(self.screen, self.settings, self.data_package)
