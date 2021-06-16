import tkinter
import tkinter.messagebox

class Page05:
    def __init__(self, screen, settings, data_package):
        self.screen = screen
        self.settings = settings
        self.data_package = data_package
        self.frame = tkinter.Frame(self.screen)

        self.screen.title(settings.page05_title)
        self.frame.pack(fill="both", expand=1)

        # 所有的控件
        labelSearchByTitle = tkinter.Label(self.frame, text="根据书名查询: ")
        self.entrySearchByTitle = tkinter.Entry(self.frame, show=None)
        labelSearchByAuthor = tkinter.Label(self.frame, text="根据作者查询: ")
        self.entrySearchByAuthor = tkinter.Entry(self.frame, show=None)
        labelPreciseSearch = tkinter.Label(self.frame, text="通过书名和作者精准查询")
        labelTitle = tkinter.Label(self.frame, text="书名: ")
        self.entryTitle = tkinter.Entry(self.frame, show=None)
        labelAuthor = tkinter.Label(self.frame, text="作者: ")
        self.entryAuthor = tkinter.Entry(self.frame, show=None)
        buttonSearch = tkinter.Button(self.frame, text="查询", command=self.search_books)

        # 暂定放置
        screen.geometry("480x320")
        # 从此处开始使用Adobe XD的数据顺序, 方便誊写
        labelSearchByTitle.place(width=296, height=19, x=92, y=16)
        self.entrySearchByTitle.place(width=296, height=30, x=92, y=35)
        labelSearchByAuthor.place(width=296, height=19, x=92, y=81)
        self.entrySearchByAuthor.place(width=296, height=30, x=92, y=100)
        labelPreciseSearch.place(width=296, height=19, x=92, y=146)
        labelTitle.place(width=113, height=30, x=92, y=181)
        self.entryTitle.place(width=183, height=30, x=205, y=181)
        labelAuthor.place(width=113, height=30, x=92, y=227)
        self.entryAuthor.place(width=183, height=30, x=205, y=227)
        buttonSearch.place(width=96, height=30, x=192, y=273)

    def search_books(self):
        self.data_package.search_key_words = []
        title1 = self.entrySearchByTitle.get()
        title2 = self.entrySearchByAuthor.get()
        author1 = self.entryTitle.get()
        author2 = self.entryAuthor.get()
        if title1 != "":
            self.data_package.search_key_words.append(title1)
        if title2 != "":
            self.data_package.search_key_words.append(title2)
        if author1 != "":
            self.data_package.search_key_words.append(author1)
        if author2 != "":
            self.data_package.search_key_words.append(author2)
        """
        其实这个地方全部扔到数组里再删似乎更优雅, 至少没有那么多if
        但是python的list在删除时要copy以防止index错误
        所以我就这样写了, 一言蔽之就是懒
        """
        self.data_package.search_from_db()
        if len(self.data_package.res) == 0:
            tkinter.messagebox.showinfo(title="对不起", message=self.settings.page05_get_0_res)
        else:
            self.frame.destroy()
            from page06 import Page06
            Page06(self.screen, self.settings, self.data_package)
