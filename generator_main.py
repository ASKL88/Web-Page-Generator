from tkinter import *
import tkinter as tk

import generator_gui
import generator_func

class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.title("Web Page Generator")
        self.master.minsize(500,100) #(Height, Width)
        self.master.maxsize(500,100)


        generator_gui.load_gui(self)






if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
