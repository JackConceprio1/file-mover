import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter.ttk import *
import os

def getfiles():
    lb1.delete(0,tk.END)
    
    selectedDir = filedialog.askdirectory()
    if selectedDir != "":
        Label1.configure(text=selectedDir)
        for path, subdirs, files in os.walk(selectedDir):
            for name in files:
                # add file to the list
                lb1.insert(tk.END,os.path.join(path, name))

def movefiles():
    if lb1.size() == 0:
        messagebox.showerror("Error","you must have files in the list")
    else:
        # ask what directory they want to use
        selectedDir = filedialog.askdirectory()
        if selectedDir == "":
            Label2.configure(text="you did not select a directory")
        else:
            Label2.configure(text=selectedDir)
            value = messagebox.askyesno("askquestion", f"do you want to move your files to this location: \n {selectedDir}")
            if value == True:
                for i, listbox_entry in enumerate(lb1.get(0, tk.END)):
                    d = os.path.basename(listbox_entry)
                    os.replace(listbox_entry, selectedDir+"/"+d)
                messagebox.showinfo("message","all done")
            else:
                messagebox.showinfo("message","no files where moved")

# create the window
window = tk.Tk()

# set the window size
window.geometry("500x500")

Label1 = tk.Label(window,text="Select a folder location")
Label1.pack()

Button1 = tk.Button(window,text="open a folder",command=getfiles)
Button1.pack()

Label2 = tk.Label(window,text="Select a folder location to move your files to")
Label2.pack()

Button2 = tk.Button(window,text="Move files to new location",command=movefiles)
Button2.pack()



Label(text="listed directory").pack()


listDirFrame1 = Frame(window)
listDirFrame1.pack(fill="both",side="top")


lb1 = tk.Listbox(listDirFrame1)
lb1.pack(side="left",fill="both",expand=True)

Scrollbar1 = Scrollbar(listDirFrame1,orient="vertical")
Scrollbar1.config(command=lb1.yview)
Scrollbar1.pack(side="right",fill="y")

Label(text="error messages").pack()

listDirFrame2 = Frame(window)
listDirFrame2.pack(fill="both",side="top")

lb2 = tk.Listbox(listDirFrame2)
lb2.pack(side="left",fill="both",expand=True)

Scrollbar2 = Scrollbar(listDirFrame2,orient="vertical")
Scrollbar2.config(command=lb2.yview)
Scrollbar2.pack(side="right",fill="y")


# create the main loop
window.mainloop()