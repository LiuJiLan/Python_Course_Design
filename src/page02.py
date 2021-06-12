import tkinter


class Page02:
    def __init__(self, screen, settings):
        self.screen = screen
        self.frame = tkinter.Frame(self.screen)

        self.screen.title(settings.page02_title)
        self.frame.pack()