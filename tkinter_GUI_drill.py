#
# Author: Andy Schultheiss
#
# Description: Python course p. 122: Tkinter GUI Drill
#
# Python version: 3.8.2
#
# Date: 17 April 2020
#
# Tested to work on Windows 10


from tkinter import *
import tkinter as tk

class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__ (self)

        self.master = master
        self.master.minsize(400,170)
        self.master.maxsize(400,170)

        self.master.title('Check files')
        self.master.config(bg='#F0F0F0')

        self.btnBrowse1 = Button(self.master, text="Browse...", width=12, height=1)
        self.btnBrowse1.grid(row=0,column=0,padx=(15,15),pady=(35,5),sticky=N+W)

        self.btnBrowse2 = Button(self.master, text="Browse...", width=12, height=1)
        self.btnBrowse2.grid(row=1,column=0,padx=(15,15),pady=(5,5),sticky=N+W) 

        self.btnFileCheck = Button(self.master, text="Check for files...", width=12, height=2)
        self.btnFileCheck.grid(row=2,column=0,padx=(15,15),pady=(5,10),sticky=N+W)

        self.txt_browse1 = tk.Entry(self.master,text='')
        self.txt_browse1.grid(row=0,column=2,rowspan=1,columnspan=5,ipadx=(60),padx=(10,10),pady=(35,5),sticky=N+E+W)

        self.txt_browse2 = tk.Entry(self.master,text='')
        self.txt_browse2.grid(row=1,column=2,rowspan=1,columnspan=5,ipadx=(60),padx=(10,10),pady=(5,5),sticky=N+E+W)

        self.btnClose = Button(self.master, text="Close Program", width=12, height=2)
        self.btnClose.grid(row=2,column=6,padx=(10,10),pady=(5,10),sticky=E+N)
        

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
    
