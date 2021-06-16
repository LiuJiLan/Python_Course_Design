import tkinter
import tkinter.messagebox


class Page08:
    def __init__(self, screen, settings, data_package):
        self.screen = screen
        self.settings = settings
        self.data_package = data_package
        self.frame = tkinter.Frame(self.screen)

        self.screen.title(settings.page08_title)
        self.frame.pack(fill="both", expand=1)

        # 所有的控件
        buttonShowAll = tkinter.Button(self.frame, text="显示数据库全部书本信息", command=self.show_all)
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
        buttonTestFunctions = tkinter.Button(self.frame, text="测试中功能", command=self.test_functions)

        # 暂定放置
        self.screen.geometry("480x320")
        buttonShowAll.place(width=296, height=24, x=92, y=16)
        labelSearchByTitle.place(width=296, height=15, x=92, y=56)
        self.entrySearchByTitle.place(width=296, height=24, x=92, y=71)
        labelSearchByAuthor.place(width=296, height=15, x=92, y=111)
        self.entrySearchByAuthor.place(width=296, height=24, x=92, y=126)
        labelPreciseSearch.place(width=296, height=15, x=92, y=166)
        labelTitle.place(width=113, height=24, x=92, y=197)
        self.entryTitle.place(width=183, height=24, x=205, y=197)
        labelAuthor.place(width=113, height=24, x=92, y=237)
        self.entryAuthor.place(width=183, height=24, x=205, y=237)
        buttonSearch.place(width=113, height=24, x=92, y=277)
        buttonTestFunctions.place(width=113, height=24, x=275, y=277)

    def show_all(self):
        self.data_package.page08_get_all_from_db()
        self.frame.destroy()
        from page09 import Page09
        Page09(self.screen, self.settings, self.data_package)


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
        self.data_package.search_from_db()
        self.frame.destroy()
        from page09 import Page09
        Page09(self.screen, self.settings, self.data_package)

    def test_functions(self):
        if self.settings.page08_allow_test_functions == "True":
            self.frame.destroy()
            from pagexx import Pagexx
            Pagexx(self.screen, self.settings, self.data_package)
        else:
            tkinter.messagebox.showinfo(title="对不起", message=self.settings.page08_do_not_allow_test_message)

