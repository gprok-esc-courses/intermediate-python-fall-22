from tkinter import Tk, Frame, Label, Button


class Controller:
    def __init__(self):
        self.window = App(self)

    def show_scene(self, scene_id):
        self.window.show_scene(scene_id)


class App(Tk):
    def __init__(self, controller):
        super(App, self).__init__()
        self.controller = controller

        self.stage = Frame(self)
        self.stage.pack(side="top", fill="both", expand=True)
        self.stage.grid_rowconfigure(0, weight=1)
        self.stage.grid_columnconfigure(0, weight=1)

        self.geometry("400x400")

        self.main_frame = MainFrame(self.stage, self.controller)
        self.main_frame.grid(row=0, column=0, sticky="nsew")

        self.scene1 = Scene1(self.stage, self.controller)
        self.scene1.grid(row=0, column=0, sticky="nsew")

        self.scene2 = Scene2(self.stage, self.controller)
        self.scene2.grid(row=0, column=0, sticky="nsew")

        self.main_frame.tkraise()

    def show_scene(self, scene_id):
        if scene_id == 0:
            self.main_frame.tkraise()
        elif scene_id == 1:
            self.scene1.tkraise()
        elif scene_id == 2:
            self.scene2.tkraise()


class MainFrame(Frame):
    def __init__(self, parent, controller: Controller):
        super(MainFrame, self).__init__(parent)
        label = Label(self, text="Main Frame")
        label.pack()
        button1 = Button(self, text="Scene 1",
                         command=lambda: controller.show_scene(1))
        button1.pack()
        button2 = Button(self, text="Scene 2",
                         command=lambda: controller.show_scene(2))
        button2.pack()


class Scene1(Frame):
    def __init__(self, parent, controller: Controller):
        super(Scene1, self).__init__(parent)
        label = Label(self, text="Scene 1")
        label.pack()
        button1 = Button(self, text="back",
                         command=lambda: controller.show_scene(0))
        button1.pack()


class Scene2(Frame):
    def __init__(self, parent, controller: Controller):
        super(Scene2, self).__init__(parent)
        label = Label(self, text="Scene 2")
        label.pack()
        button1 = Button(self, text="back",
                         command=lambda: controller.show_scene(0))
        button1.pack()


if __name__ == '__main__':
    app = Controller()
    app.window.mainloop()
