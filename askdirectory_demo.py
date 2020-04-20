#
# Author: Andy Schultheiss
#
# Description: Python course p. 123: Tkinter GUI Drill with askdirectory() method
#
# Python version: 3.8.2
#
# Date: 20 April 2020
#
# Tested to work on Windows 10


from tkinter import *
from tkinter import filedialog
import tkinter as tk

class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__ (self)

        self.master = master
        self.master.minsize(540,160)
        self.master.maxsize(540,160)
        self.varDir = StringVar()   # directory string

        self.master.title('Askdirectory demo')
        self.master.config(bg='#F0F0F0')
        
        # instructions label
        self.instrLabel = Label(self.master, text='Press button to browse. Selected directory will appear in entry box below')
        self.instrLabel.grid(row=0,column=0,rowspan=1,columnspan=6,padx=(15,15),pady=(25,5),sticky=N+W)

        self.btnBrowse1 = Button(self.master, text="Browse directories", width=15, height=1, command=self.browse_dir)
        self.btnBrowse1.grid(row=1,column=0,padx=(15,15),pady=(15,5),sticky=N+W)

        self.txt_browse1 = tk.Entry(self.master,text='')
        self.txt_browse1.grid(row=1,column=1,rowspan=1,columnspan=5,ipadx=(120),padx=(10,10),pady=(15,5),sticky=N+E+W)

        self.btnClose = Button(self.master, text="Close Program", width=15, height=1, command=self.cancel)
        self.btnClose.grid(row=2,column=0,padx=(15,15),pady=(15,5),sticky=N+W)
        
    ## browse and display function
    def browse_dir(self):
        self.varDir = filedialog.askdirectory()
        print(self.varDir) # command line display as well
        self.txt_browse1.insert(0,str(self.varDir))

    ## exit program
    def cancel(self):
        self.master.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
    
