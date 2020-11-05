from tkinter import *


class Window(Frame):

    def __init__(self, master, title="Chat Box"):
        Frame.__init__(self, master)
        self.master = master
        self.init_window(title)

    def init_window(self, title):
        self.master.title(title)
        self.pack(fill=BOTH, expand=1)
        quit_button = Button(self, text="Quit", command=self.client_exit)
        quit_button.place(x=366, y=0)

    def client_exit(self):
        exit()


root = Tk()
root.geometry("400x300")

app = Window(root)
root.mainloop()
