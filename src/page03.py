import tkinter
import tkinter.ttk
import tkinter.messagebox


class Page03:
    def __init__(self, screen, settings, data_package):
        self.screen = screen
        self.settings = settings
        self.data_package = data_package
        self.frame = tkinter.Frame(self.screen)

        self.screen.title(settings.page03_title)
        self.frame.pack(fill="both", expand=1)

        # 所有的控件
        labelId = tkinter.Label(self.frame, text="学工号:")
        self.entryId = tkinter.Entry(self.frame, show=None)
        labelIdentity = tkinter.Label(self.frame, text="身份:")
        self.comboboxIdentity = tkinter.ttk.Combobox(self.frame)
        buttonGoNext = tkinter.Button(self.frame, text="下一步", command=self.go_next)
        buttonGoBack = tkinter.Button(self.frame, text="返回", command=self.go_back)

        # 控件子设定
        # # self.entryIdentity设定
        self.comboboxIdentity["values"] = ["请选择身份", "管理员", "学生"]
        self.comboboxIdentity["state"] = "readonly"
        self.comboboxIdentity.current(0)

        # 暂定放置
        self.screen.geometry("480x320")
        labelId.place(x=92, y=47, width=113, height=58)
        self.entryId.place(x=205, y=47, width=183, height=58)
        labelIdentity.place(x=92, y=131, width=113, height=58)
        self.comboboxIdentity.place(x=205, y=131, width=183, height=58)
        buttonGoNext.place(x=92, y=215, width=113, height=58)
        buttonGoBack.place(x=275, y=215, width=113, height=58)

    def go_next(self):
        userId = self.entryId.get()
        combobox_return = self.comboboxIdentity.get()

        if combobox_return == "请选择身份":
            tkinter.messagebox.showinfo(title="对不起", message=self.settings.page03_combobox_not_selected)
        else:
            self.data_package.id = userId
            self.data_package.authority = combobox_return

            if self.data_package.page03_does_id_exist():
                if self.data_package.page03_any_times_left():
                    if self.data_package.page03_any_times_identity_left():
                        self.frame.destroy()
                        from page04 import Page04
                        Page04(self.screen, self.settings, self.data_package)
                    else:
                        tkinter.messagebox.showinfo(title="对不起",
                                                    message=self.settings.page03_any_times_identity_left_message)
                else:
                    tkinter.messagebox.showinfo(title="对不起", message=self.settings.page03_any_times_left_message)
            else:
                tkinter.messagebox.showinfo(title="对不起", message=self.settings.page03_does_id_exist_message)

    def go_back(self):
        self.frame.destroy()
        from page01 import Page01
        Page01(self.screen, self.settings, self.data_package)
