import tkinter
import tkinter.scrolledtext


class Page11:
    def __init__(self, screen, settings, data_package):
        self.screen = screen
        self.settings = settings
        self.data_package = data_package
        self.frame = tkinter.Frame(self.screen)

        self.screen.title(settings.page11_title)
        self.frame.pack(fill="both", expand=1)

        # 写缓存
        self.data_package.get_selected_book_info()

        # 所有的控件
        buttonConfirmChange = tkinter.Button(self.frame, text="确认修改", command=self.comfirm_change)
        buttonGoBack = tkinter.Button(self.frame, text="返回", command=self.go_back)
        labelTitle = tkinter.Label(self.frame, text="原书名: " + "《" + self.data_package.selected_book_info[0] + "》")
        labelNewTitle = tkinter.Label(self.frame, text="新书名: ")
        self.entryNewTitle = tkinter.Entry(self.frame, show=None)
        labelAuthor = tkinter.Label(self.frame, text="原作者: " + self.data_package.selected_book_info[1])
        labelNewAuthor = tkinter.Label(self.frame, text="新作者: ")
        self.entryNewAuthor = tkinter.Entry(self.frame, show=None)
        # labelBriefIntro = tkinter.Label(self.frame, text="原书本简介: ")
        scrolledtextBriefIntro = tkinter.scrolledtext.ScrolledText(self.frame)
        labelNewBriefIntro = tkinter.Label(self.frame, text="新书本简介: ")
        self.scrolledtextNewBriefIntro = tkinter.scrolledtext.ScrolledText(self.frame)

        # 控件子设定
        # # scrolledtextBriefIntro设定
        scrolledtextBriefIntro.insert(tkinter.END, self.data_package.selected_book_info[2])
        scrolledtextBriefIntro.config(state="disable")

        # 暂定放置
        buttonConfirmChange.place(width=282, height=48, x=230, y=30)
        buttonGoBack.place(width=282, height=48, x=688, y=30)
        labelTitle.place(width=282, height=48, x=230, y=108)
        labelNewTitle.place(width=282, height=48, x=230, y=392)
        self.entryNewTitle.place(width=458, height=48, x=512, y=392)
        labelAuthor.place(width=282, height=48, x=688, y=108)
        labelNewAuthor.place(width=282, height=48, x=230, y=470)
        self.entryNewAuthor.place(width=458, height=48, x=512, y=470)
        # labelBriefIntro.place(width=282, height=48, x=230, y=376)
        scrolledtextBriefIntro.place(width=740, height=176, x=230, y=186)
        labelNewBriefIntro.place(width=282, height=48, x=230, y=548)
        self.scrolledtextNewBriefIntro.place(width=740, height=176, x=230, y=596)

    def comfirm_change(self):
        self.data_package.generate_new_unique_code()
        self.data_package.new_book_info = (self.entryNewTitle.get(), self.entryNewAuthor.get(), self.scrolledtextNewBriefIntro.get(1.0, tkinter.END))
        self.frame.destroy()
        from page12 import Page12
        Page12(self.screen, self.settings, self.data_package)

    def go_back(self):
        self.data_package.new_one = ""
        self.data_package.new_book_info = ()
        self.frame.destroy()
        from page09 import Page09
        Page09(self.screen, self.settings, self.data_package)
