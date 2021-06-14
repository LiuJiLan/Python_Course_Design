import tkinter
import tkinter.ttk
import tkinter.messagebox
import db_functions as dbf


class Page03:
    def __init__(self, screen, settings, data_package):
        self.screen = screen
        self.settings = settings
        self.data_package = data_package
        self.frame = tkinter.Frame(self.screen)

        self.screen.title(settings.page03_title)
        self.frame.pack(fill="both")

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
        labelId.pack()
        self.entryId.pack()
        labelIdentity.pack()
        self.comboboxIdentity.pack()
        buttonGoNext.pack()
        buttonGoBack.pack()

    def go_next(self):
        userId = self.entryId.get()
        combobox_return = self.comboboxIdentity.get()
        if combobox_return == "请选择身份":
            tkinter.messagebox.showinfo(title="对不起", message=self.settings.page03_combobox_not_selected)
        else:
            if dbf.page03_does_id_exist(userId):
                if dbf.page03_any_times_left(userId):
                    if dbf.page03_any_times_identity_left(userId, combobox_return):
                        pass
                    else:
                        tkinter.messagebox.showinfo(title="对不起",
                                                    message=self.settings.page03_any_times_identity_left_message)
                else:
                    tkinter.messagebox.showinfo(title="对不起", message=self.settings.page03_any_times_left_message)
            else:
                tkinter.messagebox.showinfo(title="对不起", message=self.settings.page03_does_id_exist_message)

    def go_back(self):
        pass
