import tkinter


class Page05:
    def __init__(self, screen, settings, data_package):
        self.screen = screen
        self.settings = settings
        self.data_package = data_package
        self.frame = tkinter.Frame(self.screen)

        self.screen.title(settings.page05_title)
        self.frame.pack(fill="both")

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
        labelSearchByTitle.pack()
        self.entrySearchByTitle.pack()
        labelSearchByAuthor.pack()
        self.entrySearchByAuthor.pack()
        labelPreciseSearch.pack()
        labelTitle.pack()
        self.entryTitle.pack()
        labelAuthor.pack()
        self.entryAuthor.pack()
        buttonSearch.pack()

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
        pass