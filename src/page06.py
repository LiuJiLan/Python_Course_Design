import tkinter
import tkinter.messagebox


class Page06:
    def __init__(self, screen, settings, data_package):
        self.screen = screen
        self.settings = settings
        self.data_package = data_package
        self.frame = tkinter.Frame(self.screen)

        self.screen.title(settings.page06_title)
        self.frame.pack(fill="both")

        # 控件所需信息
        length_of_res = len(data_package.res)

        # 所有的控件
        labelNumberOfBooks = tkinter.Label(self.frame, text="已经找到信息条数: " + str(length_of_res))
        buttonViewInfo = tkinter.Button(self.frame, text="查看信息", command=self.handle_view_info)
        buttonGoBack = tkinter.Button(self.frame, text="返回", command=self.go_back)
        frameBooksInfo = tkinter.Frame(self.frame)
        scrollbarBooksInfo = tkinter.Scrollbar(frameBooksInfo)
        self.listboxBooksInfo = tkinter.Listbox(frameBooksInfo, yscrollcommand=scrollbarBooksInfo.set)

        # 暂定放置
        labelNumberOfBooks.pack()
        buttonViewInfo.pack()
        buttonGoBack.pack()
        frameBooksInfo.pack()
        self.listboxBooksInfo.pack(side="left", fill="both")
        scrollbarBooksInfo.pack(side="right", fill="y")

        # 控件子设定
        # # self.listboxBooksInfo和scrollbarBooksInfo设定
        if length_of_res == 0:
            self.listboxBooksInfo.insert(tkinter.END, self.settings.page06_number_of_res_is_zero)
        else:
            for info in self.data_package.res:
                self.listboxBooksInfo.insert(tkinter.END, "《" + info[1] + "》\t" + info[2])
            if self.data_package.last_visited_location == -1:
                # 如果记录为-1, 则不设置
                pass
            else:
                if self.data_package.last_visited_location < length_of_res:
                    # 虽然我知道不会越界, 但还是做一个保护
                    self.listboxBooksInfo.selection_set(self.data_package.last_visited_location)
                else:
                    # 越界则无动作
                    pass
        # 虽然对page06而言不可能出现length_of_res为0, 只是为了好直接复用模块
        scrollbarBooksInfo.config(command=self.listboxBooksInfo.yview)

    def handle_view_info(self):
        last_visited_location = self.listboxBooksInfo.curselection()
        if len(last_visited_location) == 0:
            tkinter.messagebox.showinfo(title="对不起", message=self.settings.page06_no_location_selected_message)
        else:
            self.data_package.last_visited_location = last_visited_location[0]
            self.data_package.selected_one = self.data_package.res[self.data_package.last_visited_location][0]
            # 自我提示, 如果在page11, page12等处, 如果一旦数据被修改, 应该也处理self.data_package.res中的内容
            # 同时将self.data_package.last_visited_location置-1
            self.frame.destroy()
            from page07 import Page07
            Page07(self.screen, self.settings, self.data_package)

    def go_back(self):
        # 返回的话要删除有关的搜索信息
        self.data_package.search_key_words = []
        self.data_package.res = []
        self.frame.destroy()
        from page05 import Page05
        Page05(self.screen, self.settings, self.data_package)
