import tkinter


def run_software():
    # 函数内导包
    from settings import Settings
    from data_package import Package

    # 初始化各种需要用的元素
    screen = tkinter.Tk()
    sbms_settings = Settings()
    user_info = Package()

    # 主screen的各种设置加载
    screen.title(sbms_settings.screen_title)
    screen.geometry("{}x{}+{}+{}".format(sbms_settings.screen_width, sbms_settings.screen_height, sbms_settings.screen_at_x, sbms_settings.screen_at_y))
    screen.resizable(False, False)
    screen.configure(bg=sbms_settings.screen_bg_color)

    from page01 import Page01
    Page01(screen, sbms_settings, user_info)

    # 开始运行
    screen.mainloop()


if __name__ == '__main__':
    run_software()
