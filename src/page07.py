import tkinter
import tkinter.scrolledtext
from tkinter import filedialog
import os


class Page07:
    def __init__(self, screen, settings, data_package):
        self.screen = screen
        self.settings = settings
        self.data_package = data_package
        self.frame = tkinter.Frame(self.screen)

        self.screen.title(settings.page07_title)
        self.frame.pack(fill="both", expand=1)

        # 写缓存
        self.data_package.get_selected_book_info()
        """
        self.book_cover_path = ""
        temp_file_path = self.data_package.write_pic_2_temp()
        if os.path.exists(temp_file_path):
            self.book_cover_path = temp_file_path
        else:
            self.book_cover_path = self.settings.books_cover_not_temp
        """

        # 所有的控件
        buttonSaveTextContent = tkinter.Button(self.frame, text="保存文字内容", command=self.save_text_content)
        # buttonSaveBookCover = tkinter.Button(self.frame, text="保存图片", command=self.save_book_cover)
        buttonGoBack = tkinter.Button(self.frame, text="返回", command=self.go_back)
        labelTitle = tkinter.Label(self.frame, text="书名: " + "《" + self.data_package.selected_book_info[0] + "》")
        labelAuthor = tkinter.Label(self.frame, text="作者: " + self.data_package.selected_book_info[1])
        labelBriefIntro = tkinter.Label(self.frame, text="书本简介: ")
        scrolledtextBriefIntro = tkinter.scrolledtext.ScrolledText(self.frame)

        # 控件子设定
        # # scrolledtextBriefIntro设定
        scrolledtextBriefIntro.insert(tkinter.END, self.data_package.selected_book_info[2])
        scrolledtextBriefIntro.config(state="disable")

        # 暂定放置.pack()
        buttonSaveTextContent.pack()
        # buttonSaveBookCover.pack()
        buttonGoBack.pack()
        labelTitle.pack()
        labelAuthor.pack()
        # labelBookCoverImage.pack()
        labelBriefIntro.pack()
        scrolledtextBriefIntro.pack()

    def save_text_content(self):
        try:
            content = "书名: " + "《" + self.data_package.selected_book_info[0] + "》\n" + "作者: " + self.data_package.selected_book_info[1] + "\n书本简介: " + self.data_package.selected_book_info[2]
            target_dir = filedialog.askdirectory()
            os.chdir(target_dir)
            with open(self.data_package.selected_one + ".txt", 'w', encoding='utf8') as (fp):
                fp.write(content)
        finally:
            pass

    # def save_book_cover(self):
    #    pass

    def go_back(self):
        self.frame.destroy()
        from page06 import Page06
        Page06(self.screen, self.settings, self.data_package)
