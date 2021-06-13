import tkinter

from settings import Settings

from page01 import Page01
from page04 import Page04
from page05 import Page05
from page06 import Page06
from page07 import Page07
from page08 import Page08
from page09 import Page09
from page10 import Page10
from page11 import Page11
from page12 import Page12
from pagexx import Pagexx


def run_software():
    # 初始化各种需要用的元素
    screen = tkinter.Tk()
    sbms_settings = Settings()

    # 主screen的各种设置加载
    screen.title(sbms_settings.screen_title)
    screen.geometry("{}x{}".format(sbms_settings.screen_width, sbms_settings.screen_height))
    screen.configure(bg=sbms_settings.screen_bg_color)

    Page01(screen, sbms_settings)

    # 开始运行
    screen.mainloop()


if __name__ == '__main__':
    run_software()
