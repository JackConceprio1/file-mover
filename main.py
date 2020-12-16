import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter.ttk import *
import os

def getfiles():
    # this will clear the listbox1
    lb1.delete(0,tk.END)
    
    # this will ask the user for a directory 
    selectedDir = filedialog.askdirectory()
    # this will check the response of the user to see if it get a folder path
    if selectedDir != "":
        # this will set the label1 text to the selected directory
        Label1.configure(text=selectedDir)
        # this will loop over all of the directorys and sub directory 
        for path, subdirs, files in os.walk(selectedDir):
            # this will get the files
            for name in files:
                # this will add it to the listbox1
                lb1.insert(tk.END,os.path.join(path, name))

def movefiles():
    # this will check listbox1 items length is equal to 0
    if lb1.size() == 0:
        # this will show a error message when there are no items in the list
        messagebox.showerror("Error","you must have files in the list")
    else:
        # ask what directory they want to use
        selectedDir = filedialog.askdirectory()
        # this will check to see if the folder path is not empty
        if selectedDir != "":
            # this will set label2 text to the selected directory
            Label2.configure(text=selectedDir)
            # this will ask the user if they are certain they want to move the files
            value = messagebox.askyesno("askquestion", f"do you want to move your files to this location: \n {selectedDir}")
            # this will check to see if the user says yes
            if value == True:
                # this will loop over every item
                for i, listbox_entry in enumerate(lb1.get(0, tk.END)):
                    # this will get file name 
                    d = os.path.basename(listbox_entry)
                    if(os.path.exists(listbox_entry) == True and os.path.exists(selectedDir+"/"+d) == False):
                        # this will move the file to the new location
                        os.replace(listbox_entry, selectedDir+"/"+d)
                    else:
                        if os.path.exists(listbox_entry) == False:
                            lb2.insert(tk.END,"Error the old file path dose not exits \n "+listbox_entry)
                        else:
                            lb2.insert(tk.END,"Error there is a file in this folder all ready \n "+selectedDir+"/"+d)

                # when it is done with the loop it will show the user that it is done
                messagebox.showinfo("message","all done")
            else:
                # if they said no show message saying no files haved been movied
                messagebox.showinfo("message","no files where moved")

# create the window
window = tk.Tk()

# set the window size
window.geometry("500x500")


# this will show the users file location 
Label1 = tk.Label(window,text="Select a folder location")
Label1.pack()

# this will get the selected files
Button1 = tk.Button(window,text="open a folder",command=getfiles)
Button1.pack()

# this will show the new file location
Label2 = tk.Label(window,text="Select a folder location to move your files to")
Label2.pack()

# this will moved the files to the new location
Button2 = tk.Button(window,text="Move files to new location",command=movefiles)
Button2.pack()



Label(text="listed directory").pack()


listDirFrame1 = Frame(window)
listDirFrame1.pack(fill="both",side="top")

# this will show a list of the files
lb1 = tk.Listbox(listDirFrame1)
lb1.pack(side="left",fill="both",expand=True)

Scrollbar1 = Scrollbar(listDirFrame1,orient="vertical")
Scrollbar1.config(command=lb1.yview)
Scrollbar1.pack(side="right",fill="y")

Label(text="error messages").pack()

listDirFrame2 = Frame(window)
listDirFrame2.pack(fill="both",side="top")
# this will show errors when somthing happend
lb2 = tk.Listbox(listDirFrame2)
lb2.pack(side="left",fill="both",expand=True)

Scrollbar2 = Scrollbar(listDirFrame2,orient="vertical")
Scrollbar2.config(command=lb2.yview)
Scrollbar2.pack(side="right",fill="y")


# create the main loop
window.mainloop()