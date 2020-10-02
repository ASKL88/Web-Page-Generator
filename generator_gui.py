from tkinter import *
import tkinter as tk
import generator_main
import generator_func

def load_gui(self):
    
    self.btn_one = tk.Button(self.master,width=15,height=1,text='Click to Insert Text', command=lambda:generator_func.entry(self))
    self.btn_one.grid(row=1,column=0,padx=(15,0),pady=(35,10),sticky=W)
    
    self.txt_one = tk.Entry(self.master, width=50, text='')
    self.txt_one.grid(row=1,column=5,rowspan=1,columnspan=6,padx=(15,0),pady=(30,10),sticky=E)
 


if __name__ == "__main__":
    pass
