import tkinter
import tkinter.scrolledtext
import tkinter.messagebox


class Page13:
    def __init__(self, screen, settings, data_package):
        self.screen = screen
        self.settings = settings
        self.data_package = data_package
        self.frame = tkinter.Frame(self.screen)

        self.screen.title(settings.page13_title)
        self.frame.pack(fill="both", expand=1)

        # 写缓存
        self.data_package.get_selected_book_info()

        # 所有的控件
        labelTitle = tkinter.Label(self.frame, text="书名: " + "《" + self.data_package.selected_book_info[0] + "》")
        labelAuthor = tkinter.Label(self.frame, text="作者: " + self.data_package.selected_book_info[1])
        labelBriefIntro = tkinter.Label(self.frame, text="书本简介: ")
        scrolledtextBriefIntro = tkinter.scrolledtext.ScrolledText(self.frame)
        buttonConfirmDelete = tkinter.Button(self.frame, text="确认删除", command=self.comfirm_delete)
        buttonGoCancel = tkinter.Button(self.frame, text="取消", command=self.go_cancel)

        # 控件子设定
        # # scrolledtextBriefIntro设定
        scrolledtextBriefIntro.insert(tkinter.END, self.data_package.selected_book_info[2])
        scrolledtextBriefIntro.config(state="disable")

        # 暂定放置
        screen.geometry("1200x800")
        labelTitle.place(width=282, height=48, x=230, y=152)
        labelAuthor.place(width=282, height=48, x=688, y=152)
        labelBriefIntro.place(width=282, height=48, x=230, y=240)
        scrolledtextBriefIntro.place(width=740, height=448, x=230, y=288)
        buttonConfirmDelete.place(width=282, height=48, x=230, y=64)
        buttonGoCancel.place(width=282, height=48, x=688, y=64)

    def comfirm_delete(self):
        self.data_package.delete_old_one()
        self.data_package.flush_self_variable()
        tkinter.messagebox.showinfo(title="请注意", message=self.settings.page13_finish_delete)
        self.frame.destroy()
        from page08 import Page08
        Page08(self.screen, self.settings, self.data_package)

    def go_cancel(self):
        self.frame.destroy()
        from page09 import Page09
        Page09(self.screen, self.settings, self.data_package)
