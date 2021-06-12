import tkinter

# 页面转跳测试
class page1():
    def __init__(self, screen):
        self.screen = screen
        self.frame = tkinter.Frame(self.screen)

        # 测试加载
        self.screen.title("Page 1")
        self.screen.geometry('500x300')
        self.frame.pack()

        btn = tkinter.Button(self.frame, text='change', command=self.change)
        btn.pack()

    def change(self, ):
        self.frame.destroy()
        page2(self.screen)


class page2():
    def __init__(self, screen):
        self.screen = screen
        self.frame = tkinter.Frame(self.screen)

        # 测试加载
        self.screen.title("Page 2")
        self.screen.geometry('500x300')
        self.frame.pack()

        e1 = tkinter.Entry(self.frame, show='*', font=('Arial', 14))  # 显示成密文形式
        e2 = tkinter.Entry(self.frame, show=None, font=('Arial', 14))  # 显示成明文形式
        e1.pack()
        e2.pack()


def run_software():
    # 初始化各种需要用的元素
    windows = tkinter.Tk()
    page1(windows)
    windows.mainloop()


if __name__ == '__main__':
    run_software()
