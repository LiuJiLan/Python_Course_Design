import tkinter
import tkinter.scrolledtext
import tkinter.messagebox



class Page12:
    def __init__(self, screen, settings, data_package):
        self.screen = screen
        self.settings = settings
        self.data_package = data_package
        self.frame = tkinter.Frame(self.screen)

        self.screen.title(settings.page12_title)
        self.frame.pack(fill="both", expand=1)

        # 所有的控件
        labelTitle = tkinter.Label(self.frame, text="原书名: " + "《" + self.data_package.selected_book_info[0] + "》")
        labelNewTitle = tkinter.Label(self.frame, text="新书名: " + "《" + self.data_package.new_book_info[0] + "》")
        labelAuthor = tkinter.Label(self.frame, text="原作者: " + self.data_package.selected_book_info[1])
        labelNewAuthor = tkinter.Label(self.frame, text="新作者: " + self.data_package.new_book_info[1])
        labelBriefIntro = tkinter.Label(self.frame, text="原书本简介: ")
        scrolledtextBriefIntro = tkinter.scrolledtext.ScrolledText(self.frame)
        labelNewBriefIntro = tkinter.Label(self.frame, text="新书本简介: ")
        scrolledtextNewBriefIntro = tkinter.scrolledtext.ScrolledText(self.frame)
        buttonConfirmChange = tkinter.Button(self.frame, text="确认修改", command=self.comfirm_change)
        buttonGoCancel = tkinter.Button(self.frame, text="返回", command=self.go_cancel)


        # 控件子设定
        # # scrolledtextBriefIntro设定
        scrolledtextBriefIntro.insert(tkinter.END, self.data_package.selected_book_info[2])
        scrolledtextBriefIntro.config(state="disable")
        scrolledtextNewBriefIntro.insert(tkinter.END, self.data_package.new_book_info[2])
        scrolledtextNewBriefIntro.config(state="disable")

        # 暂定放置
        labelTitle.pack()
        labelNewTitle.pack()
        labelAuthor.pack()
        labelNewAuthor.pack()
        labelBriefIntro.pack()
        scrolledtextBriefIntro.pack()
        labelNewBriefIntro.pack()
        scrolledtextNewBriefIntro.pack()
        buttonConfirmChange.pack()
        buttonGoCancel.pack()

    def comfirm_change(self):
        self.data_package.create_new_one()
        self.data_package.delete_old_one()
        self.data_package.flush_self_variable()
        tkinter.messagebox.showinfo(title="请注意", message=self.settings.page12_finish_change)
        self.frame.destroy()
        from page09 import Page09
        Page09(self.screen, self.settings, self.data_package)

    def go_cancel(self):
        self.data_package.new_one = ""
        self.data_package.new_book_info = ()
        self.frame.destroy()
        from page11 import Page11
        Page11(self.screen, self.settings, self.data_package)

