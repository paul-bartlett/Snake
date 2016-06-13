from tkinter import *
from time import sleep


class Application:
    def __init__(self, master):
        frame = Frame(master)
        root.bind("<Button-1>", self.start)
        frame.pack()
        self.snake = []
        self.head = 0

        self.createWidgets()

    def createWidgets(self):
        # ***** Main Menu *****
        menu = Menu(root)
        root.config(menu=menu)

        # ***** Sub Menu ******
        subMenu = Menu(menu)
        menu.add_cascade(label="File", menu=subMenu)
        subMenu.add_command(label="Exit", command=root.destroy)

        settingsMenu = Menu(menu)
        menu.add_cascade(label="Settings", menu=settingsMenu)
        settingsMenu.add_command(label="Change grid", command=None)
        settingsMenu.add_separator()
        settingsMenu.add_command(label="About", command=None)

        # ***** Buttons *****
        # self.hi_there = Button(self)
        # self.hi_there["text"] = "Hello World\n(click me)"
        # self.hi_there["command"] = self.say_hi
        # self.hi_there.pack(side="top")
        #
        # self.quit_button = Button(self, text="QUIT", fg="red", command=root.destroy)
        # self.quit_button.pack(side="bottom")

    def start(self, event):
        # ***** Canvas *****
        canvas = Canvas(root, width=804, height=804, bg="black")
        canvas.pack()
        boundary = canvas.create_rectangle(22, 22, 782, 782, fill="black", outline="white")

        # paramenters: (x top, y top, x bottom, y bottom)
        snake = [100]
        head = 0
        snake[head] = canvas.create_rectangle(2, 2, 22, 22, fill="white")

        black_box2 = canvas.create_rectangle(22, 2, 42, 22, fill="white")
        # canvas.delete(black_box)
        # canvas.delete(ALL)

        # ***** Status Bar *****
        status = Label(root, text="Welcome to Snake!", bd=1, relief=SUNKEN, anchor=W)
        status.pack(side=BOTTOM, fill=X)
        canvas.delete(snake[head])

root = Tk()
root.title("Snake") # Name the window
root.geometry("850x850") # Change the size of the window
app = Application(root)
root.mainloop()
