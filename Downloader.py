from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from pytube import YouTube
from PIL import ImageTk,Image
import tkinter as tk
from tkinter import ttk

def clickBrowse():
    location_of_download = filedialog.askdirectory()
    getLoc.set(location_of_download)

def clickReset():
    getURL.set("")
    getLoc.set("")
    listbox.delete(0, END)


root = Tk()
root.configure(background='black')
#Set Title
root.title("YouTube Video Downloader")

#Set size of window
root.geometry("855x500")

#Make the Window not Resizeable
root.resizable(False, False)

#Set Labels
img=ImageTk.PhotoImage(file="logo.jpg")
headLabel       = Label(root,image=img).grid(row=0, column=1, padx=10, pady=10)
urlLabel        = Label(root,   text="URL",                 font=("Century Gothic",15)).grid(row=1, column=0, padx=10, pady=10)
qualityLabel    = Label(root,   text="SELECT QUALITY",      font=("Century Gothic",15)).grid(row=2, column=0, padx=10, pady=10)
locLabel        = Label(root,   text="LOCATION",            font=("Century Gothic",15)).grid(row=3, column=0, padx=10, pady=10)

#Get Input
getURL = StringVar()
getLoc = StringVar()

#Set Entry
urlEntry    = Entry(root,   font=("Century Gothic",12), textvariable = getURL, width = 50, bd=3, relief=SOLID, borderwidth=1).grid(row=1,column=1, padx=10, pady=10)
locEntry    = Entry(root,   font=("Century Gothic",12), textvariable = getLoc, width = 50, bd=3, relief=SOLID, borderwidth=1).grid(row=3,column=1, padx=10, pady=10)

#List box for video Quality
listbox     = Listbox(root, font=("Century Gothic",11), width = 56, height = 12, bd=3, relief=SOLID, borderwidth=1)
listbox.grid(row=2,column=1, padx=10, pady=10)

#Set Buttons
urlButton       = Button(root, text = "SEARCH",    font=("Century Gothic",10), width=15, relief=SOLID, borderwidth=1).grid(row=1, column=2, padx=10, pady=10)
browseButton    = Button(root, text = "BROWSE...",     font=("Century Gothic",10), width=15, relief=SOLID, borderwidth=1,command=clickBrowse).grid(row=3, column=2, padx=10, pady=10)
downloadButton  = Button(root, text = "DOWNLOAD",   font=("Century Gothic",10), width=15, relief=SOLID, borderwidth=1).grid(row=4, column=1, padx=10, pady=10)
resetButton     = Button(root, text = "CLEAR ALL",  font=("Century Gothic",10), width=15, relief=SOLID, borderwidth=1,command=clickReset).grid(row=4, column=2, padx=10, pady=10)
root.iconbitmap(default='iconphot.ico')

#Set an infinite loop so window stays in view
root.mainloop()




class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.button = ttk.Button(text="start", command=self.start())
        self.button.pack()
        self.progress = ttk.Progressbar(self, orient="horizontal",
                                        length=200, mode="determinate")
        self.progress.pack()

        self.bytes = 0
        self.maxbytes = 0

    def start(self):
        self.progress["value"] = 0
        self.maxbytes = 50000
        self.progress["maximum"] = 50000
        self.read_bytes()

    def read_bytes(self):
        '''simulate reading 500 bytes; update progress bar'''
        self.bytes += 500
        self.progress["value"] = self.bytes
        if self.bytes < self.maxbytes:
            # read more bytes after 100 ms
            self.after(100, self.read_bytes)

app = SampleApp()
app.mainloop()