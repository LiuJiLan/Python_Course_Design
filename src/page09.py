import tkinter
import tkinter.messagebox

class Page09:
    def __init__(self, screen, settings, data_package):
        self.screen = screen
        self.settings = settings
        self.data_package = data_package
        self.frame = tkinter.Frame(self.screen)

        self.screen.title(settings.page09_title)
        self.frame.pack(fill="both")

        # 控件所需信息
        length_of_res = len(data_package.res)

        # 所有的控件
        labelNumberOfBooks = tkinter.Label(self.frame, text="已经找到信息条数: " + str(length_of_res))
        buttonViewInfo = tkinter.Button(self.frame, text="查看信息", command=self.handle_view_info)
        buttonAddInfo = tkinter.Button(self.frame, text="增加信息", command=self.handle_add_info)
        buttonChangeInfo = tkinter.Button(self.frame, text="修改信息", command=self.handle_change_info)
        buttonDeleteInfo = tkinter.Button(self.frame, text="删除信息", command=self.handle_delete_info)
        buttonGoBack = tkinter.Button(self.frame, text="返回", command=self.go_back)
        frameBooksInfo = tkinter.Frame(self.frame)
        scrollbarBooksInfo = tkinter.Scrollbar(frameBooksInfo)
        self.listboxBooksInfo = tkinter.Listbox(frameBooksInfo, yscrollcommand=scrollbarBooksInfo.set)

        # 暂定放置
        labelNumberOfBooks.pack()
        buttonViewInfo.pack()
        buttonGoBack.pack()
        buttonAddInfo.pack()
        buttonChangeInfo.pack()
        buttonDeleteInfo.pack()
        frameBooksInfo.pack()
        self.listboxBooksInfo.pack(side="left", fill="both")
        scrollbarBooksInfo.pack(side="right", fill="y")

        # 控件子设定
        # # self.listboxBooksInfo和scrollbarBooksInfo设定
        if length_of_res == 0:
            self.listboxBooksInfo.insert(tkinter.END, self.settings.page09_number_of_res_is_zero)
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
        scrollbarBooksInfo.config(command=self.listboxBooksInfo.yview)


    def handle_view_info(self):
        if len(self.data_package.res) == 0:
            tkinter.messagebox.showinfo(title="对不起", message=self.settings.page09_there_no_result)
        else:
            last_visited_location = self.listboxBooksInfo.curselection()
            if len(last_visited_location) == 0:
                tkinter.messagebox.showinfo(title="对不起", message=self.settings.page09_no_location_selected_message)
            else:
                self.data_package.last_visited_location = last_visited_location[0]
                self.data_package.selected_one = self.data_package.res[self.data_package.last_visited_location][0]
                self.frame.destroy()
                from page10 import Page10
                Page10(self.screen, self.settings, self.data_package)


    def handle_add_info(self):
        self.frame.destroy()
        from page14 import Page14
        Page14(self.screen, self.settings, self.data_package)

    def handle_change_info(self):
        if len(self.data_package.res) == 0:
            tkinter.messagebox.showinfo(title="对不起", message=self.settings.page09_there_no_result)
        else:
            last_visited_location = self.listboxBooksInfo.curselection()
            if len(last_visited_location) == 0:
                tkinter.messagebox.showinfo(title="对不起", message=self.settings.page09_no_location_selected_message)
            else:
                self.data_package.last_visited_location = last_visited_location[0]
                self.data_package.selected_one = self.data_package.res[self.data_package.last_visited_location][0]
                self.frame.destroy()
                from page11 import Page11
                Page11(self.screen, self.settings, self.data_package)

    def handle_delete_info(self):
        if len(self.data_package.res) == 0:
            tkinter.messagebox.showinfo(title="对不起", message=self.settings.page09_there_no_result)
        else:
            last_visited_location = self.listboxBooksInfo.curselection()
            if len(last_visited_location) == 0:
                tkinter.messagebox.showinfo(title="对不起", message=self.settings.page09_no_location_selected_message)
            else:
                self.data_package.last_visited_location = last_visited_location[0]
                self.data_package.selected_one = self.data_package.res[self.data_package.last_visited_location][0]
                self.frame.destroy()
                from page13 import Page13
                Page13(self.screen, self.settings, self.data_package)


    def go_back(self):
        # 返回的话要删除有关的搜索信息
        self.data_package.search_key_words = []
        self.data_package.res = []
        self.data_package.selected_one = ""
        self.data_package.selected_book_info = -1
        self.frame.destroy()
        from page08 import Page08
        Page08(self.screen, self.settings, self.data_package)

